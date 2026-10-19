"""Nominatim geocoding proxy with User-Agent compliance and caching."""
import logging
import httpx
from typing import List, Dict, Any, Optional
from app.config import NOMINATIM_URL, USER_AGENT, DEFAULT_TIMEOUT, GEOCODE_CACHE_TTL
from app.cache import geocode_cache
from app.schemas import GeocodeResult

logger = logging.getLogger(__name__)

async def search_locations(query: str, lat: Optional[float] = None, lon: Optional[float] = None) -> List[GeocodeResult]:
    """
    Query Nominatim geocoder with caching and User-Agent compliance.
    """
    clean_query = query.strip().lower()
    cache_key = f"geo:{clean_query}"
    cached_val = geocode_cache.get(cache_key)
    if cached_val:
        data, _ = cached_val
        return data

    params = {
        "q": query.strip(),
        "format": "jsonv2",
        "limit": 5,
        "addressdetails": 1
    }
    if lat is not None and lon is not None:
        params["viewbox"] = f"{lon-0.5},{lat+0.5},{lon+0.5},{lat-0.5}"

    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/json"
    }

    try:
        async with httpx.AsyncClient(timeout=DEFAULT_TIMEOUT) as client:
            resp = await client.get(NOMINATIM_URL, params=params, headers=headers)
            if resp.status_code != 200:
                logger.warning(f"Nominatim returned {resp.status_code}")
                return []
            
            raw_items = resp.json()
            results = []
            for item in raw_items:
                name = item.get("name") or item.get("display_name", "").split(",")[0]
                results.append(GeocodeResult(
                    place_id=item.get("place_id"),
                    name=name,
                    display_name=item.get("display_name", ""),
                    lat=float(item.get("lat")),
                    lon=float(item.get("lon")),
                    type=item.get("type"),
                    boundingbox=item.get("boundingbox")
                ))

            geocode_cache.set(cache_key, results, ttl_seconds=GEOCODE_CACHE_TTL)
            return results
    except Exception as err:
        logger.error(f"Geocoding error for '{query}': {err}")
        return []
