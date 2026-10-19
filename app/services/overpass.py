"""Overpass API query builder and mirror fallback client with optimized single-pass queries."""
import logging
import httpx
from typing import List, Dict, Any, Tuple, Optional
from app.config import OVERPASS_MIRRORS, USER_AGENT, DEFAULT_TIMEOUT

logger = logging.getLogger(__name__)

CATEGORY_AMENITY_MAP = {
    "hospital": ["hospital"],
    "clinic": ["clinic", "doctors"],
    "pharmacy": ["pharmacy"],
    "police": ["police"],
    "fire_station": ["fire_station"],
    "shelter": ["shelter"],
    "drinking_water": ["drinking_water", "water_point"],
    "toilets": ["toilets"],
}

CATEGORY_HEALTHCARE_MAP = {
    "hospital": ["hospital"],
    "clinic": ["clinic", "doctor", "centre"],
    "pharmacy": ["pharmacy"],
}

CATEGORY_SOCIAL_MAP = {
    "shelter": ["shelter"],
    "food_bank": ["food_bank", "soup_kitchen"],
}

ALL_CATEGORIES = [
    "hospital", "clinic", "pharmacy", "police", 
    "fire_station", "shelter", "drinking_water", "food_bank", "toilets"
]

def build_overpass_query(lat: float, lon: float, radius_meters: int, categories: Optional[List[str]] = None) -> str:
    """
    Constructs an ultra-fast Overpass QL query using nwr (nodes, ways, relations)
    grouped regex matching. Executes in 1-4 passes across Overpass's spatial index.
    """
    target = set(categories) if (categories and len(categories) > 0) else set(ALL_CATEGORIES)

    amenities = set()
    for cat in target:
        for a in CATEGORY_AMENITY_MAP.get(cat, []):
            amenities.add(a)

    healthcares = set()
    for cat in target:
        for h in CATEGORY_HEALTHCARE_MAP.get(cat, []):
            healthcares.add(h)

    socials = set()
    for cat in target:
        for s in CATEGORY_SOCIAL_MAP.get(cat, []):
            socials.add(s)

    subclauses = []
    if amenities:
        regex_amenity = "|".join(sorted(amenities))
        subclauses.append(f'nwr(around:{radius_meters},{lat},{lon})["amenity"~"^({regex_amenity})$"];')

    if healthcares:
        regex_healthcare = "|".join(sorted(healthcares))
        subclauses.append(f'nwr(around:{radius_meters},{lat},{lon})["healthcare"~"^({regex_healthcare})$"];')

    if socials:
        regex_social = "|".join(sorted(socials))
        subclauses.append(f'nwr(around:{radius_meters},{lat},{lon})["social_facility"~"^({regex_social})$"];')

    if "drinking_water" in target:
        subclauses.append(f'nwr(around:{radius_meters},{lat},{lon})["man_made"="water_tap"];')

    if "shelter" in target:
        subclauses.append(f'nwr(around:{radius_meters},{lat},{lon})["emergency"="shelter"];')

    if "hospital" in target:
        subclauses.append(f'nwr(around:{radius_meters},{lat},{lon})["emergency"="hospital"];')

    union_body = "\n  ".join(subclauses)
    query = f"""[out:json][timeout:20];
(
  {union_body}
);
out center body qt 250;
"""
    return query

async def query_overpass_with_fallback(
    lat: float, 
    lon: float, 
    radius_meters: int, 
    categories: Optional[List[str]] = None
) -> Tuple[List[Dict[str, Any]], str]:
    """
    Queries Overpass API with automatic fallback across the mirror pool.
    Returns (raw_elements, successful_mirror_host).
    Raises RuntimeError if all mirrors fail.
    """
    query_str = build_overpass_query(lat, lon, radius_meters, categories)
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/json"
    }

    last_error = None

    async with httpx.AsyncClient(timeout=DEFAULT_TIMEOUT) as client:
        for mirror_url in OVERPASS_MIRRORS:
            try:
                logger.info(f"Querying Overpass mirror: {mirror_url}")
                response = await client.post(
                    mirror_url,
                    data={"data": query_str},
                    headers=headers
                )

                if response.status_code == 200:
                    data = response.json()
                    elements = data.get("elements", [])
                    server_host = mirror_url.split("//")[-1].split("/")[0]
                    return elements, server_host
                elif response.status_code in (429, 504, 502, 503, 500):
                    logger.warning(f"Overpass mirror {mirror_url} returned HTTP {response.status_code}. Attempting next mirror.")
                    last_error = f"HTTP {response.status_code} from {mirror_url}"
                    continue
                else:
                    last_error = f"HTTP {response.status_code}: {response.text[:200]}"
            except (httpx.TimeoutException, httpx.RequestError) as err:
                logger.warning(f"Mirror {mirror_url} connection error: {err}. Attempting next mirror.")
                last_error = str(err)
                continue

    raise RuntimeError(f"All Overpass mirrors failed or timed out. Last error: {last_error}")
