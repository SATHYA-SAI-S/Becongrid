"""Application configuration and service URLs."""
import os

# Overpass API mirrors for high availability fallback (worldwide coverage)
OVERPASS_MIRRORS = [
    "https://overpass.kumi.systems/api/interpreter",
    "https://overpass-api.de/api/interpreter",
    "https://lz4.overpass-api.de/api/interpreter",
    "https://overpass.private.coffee/api/interpreter",
]

# Nominatim Geocoding API (OSM Foundation Usage Policy compliant)
NOMINATIM_URL = "https://nominatim.openstreetmap.org/search"
USER_AGENT = "EmergencyResourceMap/1.0 (Emergency Resource Locator; OpenStreetMap-compliant)"

# Public OSRM routing endpoint (car/driving)
OSRM_DRIVING_URL = "https://router.project-osrm.org/route/v1/driving"
OSRM_WALKING_URL = "https://router.project-osrm.org/route/v1/foot"

# Cache TTL settings (in seconds)
RESOURCE_CACHE_TTL = 600     # 10 minutes cache to respect Overpass servers
GEOCODE_CACHE_TTL = 86400    # 24 hours cache for geocoded queries
ROUTE_CACHE_TTL = 3600       # 1 hour cache for routes

# Query limits
DEFAULT_RADIUS = 3500        # meters
MAX_RADIUS = 10000           # 10km maximum to prevent upstream overload
DEFAULT_TIMEOUT = 12.0       # seconds for external requests
