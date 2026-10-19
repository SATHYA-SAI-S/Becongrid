"""Normalizer service for converting raw OSM elements into honest resource models."""
import math
from typing import List, Dict, Any, Optional
from app.schemas import ResourceItem

def haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Calculate the great circle distance in meters between two points on Earth."""
    R = 6371000  # Earth radius in meters
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = (math.sin(delta_phi / 2) ** 2 +
         math.cos(phi1) * math.cos(phi2) *
         math.sin(delta_lambda / 2) ** 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

def determine_category(tags: Dict[str, Any]) -> Optional[str]:
    """Map OSM tags to standard application category."""
    amenity = tags.get("amenity", "")
    healthcare = tags.get("healthcare", "")
    social_facility = tags.get("social_facility", "")
    man_made = tags.get("man_made", "")
    emergency = tags.get("emergency", "")

    if amenity == "hospital" or healthcare == "hospital" or emergency == "hospital":
        return "hospital"
    if amenity in ("clinic", "doctors") or healthcare in ("clinic", "doctor", "centre"):
        return "clinic"
    if amenity == "pharmacy" or healthcare == "pharmacy":
        return "pharmacy"
    if amenity == "police":
        return "police"
    if amenity == "fire_station":
        return "fire_station"
    if amenity == "shelter" or social_facility == "shelter" or emergency == "shelter":
        return "shelter"
    if amenity in ("drinking_water", "water_point") or man_made == "water_tap":
        return "drinking_water"
    if social_facility in ("food_bank", "soup_kitchen"):
        return "food_bank"
    if amenity == "toilets":
        return "toilets"

    return None

def format_address(tags: Dict[str, Any]) -> Optional[str]:
    """Extract clean address from OSM addr tags. Returns None if no address data exists."""
    parts = []
    street = tags.get("addr:street")
    housenumber = tags.get("addr:housenumber")
    city = tags.get("addr:city")
    postcode = tags.get("addr:postcode")

    if housenumber and street:
        parts.append(f"{housenumber} {street}")
    elif street:
        parts.append(street)

    if city:
        parts.append(city)
    if postcode:
        parts.append(postcode)

    if not parts:
        return None
    return ", ".join(parts)

def generate_fallback_name(category: str, tags: Dict[str, Any]) -> str:
    """Generate a descriptive name when OSM record lacks a formal name tag."""
    fallbacks = {
        "hospital": "Hospital / Medical Center",
        "clinic": "Health Clinic",
        "pharmacy": "Pharmacy",
        "police": "Police Station",
        "fire_station": "Fire Station",
        "shelter": "Emergency Shelter",
        "drinking_water": "Public Drinking Water Point",
        "food_bank": "Food Bank / Meal Center",
        "toilets": "Public Toilet"
    }
    operator = tags.get("operator")
    base = fallbacks.get(category, "Emergency Resource")
    if operator:
        return f"{base} ({operator})"
    return base

def normalize_osm_elements(
    elements: List[Dict[str, Any]], 
    query_lat: float, 
    query_lon: float,
    allowed_categories: Optional[List[str]] = None
) -> List[ResourceItem]:
    """
    Transforms raw Overpass elements into normalized ResourceItem objects.
    Adheres strictly to Data Integrity Rules:
    - Never fabricates phone numbers, ratings, or hours.
    - Omit missing fields (sets to None).
    """
    results: List[ResourceItem] = []
    seen_ids = set()

    for el in elements:
        osm_type = el.get("type", "node")
        osm_id = el.get("id")
        if not osm_id:
            continue

        unique_id = f"{osm_type}/{osm_id}"
        if unique_id in seen_ids:
            continue

        # Extract coordinates (ways might have center object)
        lat = el.get("lat")
        lon = el.get("lon")
        if lat is None or lon is None:
            center = el.get("center")
            if center and isinstance(center, dict):
                lat = center.get("lat")
                lon = center.get("lon")

        if lat is None or lon is None:
            continue

        tags = el.get("tags") or {}
        category = determine_category(tags)
        if not category:
            continue

        if allowed_categories and category not in allowed_categories:
            continue

        seen_ids.add(unique_id)

        # Distance calculation
        dist = haversine_distance(query_lat, query_lon, float(lat), float(lon))

        # Real tags extraction
        name = tags.get("name") or tags.get("name:en") or generate_fallback_name(category, tags)
        phone = tags.get("phone") or tags.get("contact:phone") or None
        address = format_address(tags)
        opening_hours = tags.get("opening_hours") or None
        emergency = tags.get("emergency") or None
        wheelchair = tags.get("wheelchair") or None
        operator = tags.get("operator") or tags.get("brand") or None

        item = ResourceItem(
            id=unique_id,
            osm_type=osm_type,
            osm_id=osm_id,
            category=category,
            name=name,
            lat=round(float(lat), 6),
            lon=round(float(lon), 6),
            distance_meters=round(dist, 1),
            address=address,
            phone=phone,
            emergency=emergency,
            opening_hours=opening_hours,
            wheelchair=wheelchair,
            operator=operator,
            tags_raw=tags
        )
        results.append(item)

    # Sort strictly by distance ascending
    results.sort(key=lambda x: x.distance_meters)
    return results
