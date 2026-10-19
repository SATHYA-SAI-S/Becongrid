"""FastAPI main application entrypoint."""
import os
import time
from datetime import datetime, timezone
from typing import Optional, List
from fastapi import FastAPI, Query, HTTPException, Request
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from app.config import DEFAULT_RADIUS, MAX_RADIUS, RESOURCE_CACHE_TTL
from app.cache import resource_cache
from app.schemas import ResourcesResponse, MetaInfo, GeocodeResponse, RouteResponse
from app.services.overpass import query_overpass_with_fallback
from app.services.normalizer import normalize_osm_elements
from app.services.geocoding import search_locations
from app.services.routing import get_route

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_DIR = os.path.join(BASE_DIR, "static")

app = FastAPI(
    title="Emergency Resource Map API",
    description="Real-time map-first API for emergency & essential resource discovery using OpenStreetMap.",
    version="1.0.0"
)

# Enable CORS for local testing and cross-origin access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files directory
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

@app.get("/", include_in_schema=False)
@app.get("/index.html", include_in_schema=False)
async def serve_index():
    """Serves the BeaconGrid landing page interface."""
    index_path = os.path.join(STATIC_DIR, "index.html")
    if not os.path.exists(index_path):
        raise HTTPException(status_code=404, detail="Frontend index.html not found")
    return FileResponse(index_path)

@app.get("/map", include_in_schema=False)
@app.get("/map.html", include_in_schema=False)
async def serve_map():
    """Serves the Live Emergency Resource Map & Disaster Management Dashboard."""
    map_path = os.path.join(STATIC_DIR, "map.html")
    if not os.path.exists(map_path):
        raise HTTPException(status_code=404, detail="Frontend map.html not found")
    return FileResponse(map_path)

@app.get("/api/health")
async def health_check():
    """Service health and cache metrics."""
    return {
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "cache": {
            "resource_hits": resource_cache.hits,
            "resource_misses": resource_cache.misses
        }
    }

@app.get("/api/resources", response_model=ResourcesResponse)
async def get_emergency_resources(
    lat: float = Query(..., ge=-90.0, le=90.0, description="Latitude in decimal degrees"),
    lon: float = Query(..., ge=-180.0, le=180.0, description="Longitude in decimal degrees"),
    radius: int = Query(DEFAULT_RADIUS, ge=100, le=MAX_RADIUS, description="Search radius in meters"),
    categories: Optional[str] = Query(None, description="Comma-separated category filters")
):
    """
    Find nearby emergency and essential facilities from OpenStreetMap.
    Guaranteed data honesty: No fake places, no fabricated hours, no synthetic phone numbers.
    """
    category_list: Optional[List[str]] = None
    if categories:
        category_list = [c.strip().lower() for c in categories.split(",") if c.strip()]
        category_list.sort()

    cat_key = ",".join(category_list) if category_list else "all"
    cache_key = f"res:{round(lat, 3)}:{round(lon, 3)}:r{round(radius, -2)}:c{cat_key}"

    # 1. Check TTL cache
    cached_entry = resource_cache.get(cache_key)
    if cached_entry:
        cached_payload, age_seconds = cached_entry
        # Recalculate distances from exact requested point for high precision
        meta = MetaInfo(
            lat=lat,
            lon=lon,
            radius_meters=radius,
            cached=True,
            retrieved_at=cached_payload["retrieved_at"],
            cache_age_seconds=round(age_seconds, 1),
            upstream_server=cached_payload["server"],
            attribution="Data © OpenStreetMap contributors, ODbL 1.0"
        )
        return ResourcesResponse(
            status="ok",
            meta=meta,
            count=len(cached_payload["items"]),
            data=cached_payload["items"],
            disclaimer="Aggregated from OpenStreetMap. In a life-threatening emergency, call local emergency services immediately (911/112)."
        )

    # 2. Query upstream Overpass with automatic mirror fallback
    try:
        raw_elements, mirror_host = await query_overpass_with_fallback(
            lat=lat,
            lon=lon,
            radius_meters=radius,
            categories=category_list
        )
    except Exception as err:
        # Honest error: Never invent results when upstream fails
        raise HTTPException(
            status_code=503,
            detail=f"OpenStreetMap upstream service unavailable: {str(err)}. Please retry shortly."
        )

    # 3. Normalize elements into honest records
    normalized_items = normalize_osm_elements(
        elements=raw_elements,
        query_lat=lat,
        query_lon=lon,
        allowed_categories=category_list
    )

    now_iso = datetime.now(timezone.utc).isoformat()
    cache_record = {
        "items": normalized_items,
        "server": mirror_host,
        "retrieved_at": now_iso
    }
    resource_cache.set(cache_key, cache_record, ttl_seconds=RESOURCE_CACHE_TTL)

    meta = MetaInfo(
        lat=lat,
        lon=lon,
        radius_meters=radius,
        cached=False,
        retrieved_at=now_iso,
        cache_age_seconds=0.0,
        upstream_server=mirror_host,
        attribution="Data © OpenStreetMap contributors, ODbL 1.0"
    )

    return ResourcesResponse(
        status="ok",
        meta=meta,
        count=len(normalized_items),
        data=normalized_items,
        disclaimer="Aggregated from OpenStreetMap. In a life-threatening emergency, call local emergency services immediately (911/112)."
    )

@app.get("/api/geocode", response_model=GeocodeResponse)
async def geocode_location(
    q: str = Query(..., min_length=2, description="Search query string"),
    lat: Optional[float] = Query(None, ge=-90.0, le=90.0),
    lon: Optional[float] = Query(None, ge=-180.0, le=180.0)
):
    """Geocode an address, landmark, or city name."""
    results = await search_locations(q, lat, lon)
    return GeocodeResponse(status="ok", results=results)

@app.get("/api/route", response_model=RouteResponse)
async def get_route_directions(
    start_lat: float = Query(..., ge=-90.0, le=90.0),
    start_lon: float = Query(..., ge=-180.0, le=180.0),
    dest_lat: float = Query(..., ge=-90.0, le=90.0),
    dest_lon: float = Query(..., ge=-180.0, le=180.0),
    profile: str = Query("driving", pattern="^(driving|walking)$")
):
    """Calculate driving or walking route from start to destination using OSRM."""
    try:
        route = await get_route(start_lat, start_lon, dest_lat, dest_lon, profile)
        return route
    except Exception as err:
        raise HTTPException(
            status_code=502,
            detail=f"Route calculation failed: {str(err)}"
        )
