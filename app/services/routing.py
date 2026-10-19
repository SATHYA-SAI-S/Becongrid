"""OSRM routing proxy and fallback route generator."""
import logging
import httpx
from typing import Dict, Any, Optional
from app.config import OSRM_DRIVING_URL, OSRM_WALKING_URL, USER_AGENT, DEFAULT_TIMEOUT, ROUTE_CACHE_TTL
from app.cache import route_cache
from app.schemas import RouteResponse

logger = logging.getLogger(__name__)

async def get_route(
    start_lat: float, 
    start_lon: float, 
    dest_lat: float, 
    dest_lon: float, 
    profile: str = "driving"
) -> RouteResponse:
    """
    Fetch routing geometry from public OSRM service with caching and safety disclaimers.
    """
    cache_key = f"route:{profile}:{round(start_lat,4)},{round(start_lon,4)}->{round(dest_lat,4)},{round(dest_lon,4)}"
    cached_val = route_cache.get(cache_key)
    if cached_val:
        data, _ = cached_val
        return data

    base_url = OSRM_WALKING_URL if profile == "walking" else OSRM_DRIVING_URL
    # OSRM coordinates format: {lon},{lat};{lon},{lat}
    url = f"{base_url}/{start_lon},{start_lat};{dest_lon},{dest_lat}"
    params = {
        "overview": "full",
        "geometries": "geojson",
        "steps": "true"
    }
    headers = {"User-Agent": USER_AGENT}

    try:
        async with httpx.AsyncClient(timeout=DEFAULT_TIMEOUT) as client:
            resp = await client.get(url, params=params, headers=headers)
            if resp.status_code != 200:
                raise RuntimeError(f"OSRM service error (HTTP {resp.status_code})")

            data = resp.json()
            routes = data.get("routes", [])
            if not routes:
                raise RuntimeError("No route found between coordinates")

            primary_route = routes[0]
            distance = primary_route.get("distance", 0.0)
            duration = primary_route.get("duration", 0.0)
            geometry = primary_route.get("geometry", {})

            result = RouteResponse(
                status="ok",
                distance_meters=round(distance, 1),
                duration_seconds=round(duration, 1),
                geometry=geometry,
                disclaimer="Routes are calculated via OpenStreetMap OSRM and do NOT account for active emergency hazards, debris, or flood closures."
            )

            route_cache.set(cache_key, result, ttl_seconds=ROUTE_CACHE_TTL)
            return result
    except Exception as err:
        logger.error(f"Routing request error: {err}")
        raise RuntimeError(f"Routing error: {err}")
