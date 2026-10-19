"""Tests for normalization logic and data integrity rules."""
import pytest
from app.services.normalizer import (
    haversine_distance,
    determine_category,
    format_address,
    generate_fallback_name,
    normalize_osm_elements
)

def test_haversine_distance():
    # Distance between London Eye (51.5033, -0.1195) and Big Ben (51.5007, -0.1246) is ~460m
    dist = haversine_distance(51.5033, -0.1195, 51.5007, -0.1246)
    assert 400 < dist < 550

def test_determine_category_all_types():
    assert determine_category({"amenity": "hospital"}) == "hospital"
    assert determine_category({"healthcare": "hospital"}) == "hospital"
    assert determine_category({"amenity": "clinic"}) == "clinic"
    assert determine_category({"amenity": "doctors"}) == "clinic"
    assert determine_category({"amenity": "pharmacy"}) == "pharmacy"
    assert determine_category({"amenity": "police"}) == "police"
    assert determine_category({"amenity": "fire_station"}) == "fire_station"
    assert determine_category({"amenity": "shelter"}) == "shelter"
    assert determine_category({"social_facility": "shelter"}) == "shelter"
    assert determine_category({"amenity": "drinking_water"}) == "drinking_water"
    assert determine_category({"man_made": "water_tap"}) == "drinking_water"
    assert determine_category({"social_facility": "food_bank"}) == "food_bank"
    assert determine_category({"amenity": "toilets"}) == "toilets"
    # Unrelated tags return None
    assert determine_category({"amenity": "restaurant"}) is None

def test_data_integrity_no_fabricated_fields():
    """Ensure missing tags in OSM are NEVER hallucinated or fabricated."""
    raw_elements = [
        {
            "type": "node",
            "id": 1001,
            "lat": 51.5074,
            "lon": -0.1278,
            "tags": {
                "amenity": "pharmacy"
                # Missing name, phone, opening_hours, addr, etc.
            }
        }
    ]

    normalized = normalize_osm_elements(raw_elements, 51.5074, -0.1278)
    assert len(normalized) == 1
    item = normalized[0]

    assert item.id == "node/1001"
    assert item.category == "pharmacy"
    assert item.name == "Pharmacy"  # Clean honest fallback descriptor
    assert item.phone is None       # Crucial: never invent phone number!
    assert item.opening_hours is None # Crucial: never claim open/hours!
    assert item.address is None     # Crucial: never invent address!
    assert item.wheelchair is None
    assert item.operator is None

def test_element_way_with_center_and_real_tags():
    raw_elements = [
        {
            "type": "way",
            "id": 2002,
            "center": {"lat": 51.5080, "lon": -0.1290},
            "tags": {
                "amenity": "hospital",
                "name": "St Thomas Hospital",
                "emergency": "yes",
                "phone": "+44 20 7188 7188",
                "opening_hours": "24/7",
                "addr:street": "Westminster Bridge Rd",
                "addr:housenumber": "249",
                "addr:city": "London",
                "operator": "NHS Foundation Trust"
            }
        }
    ]

    normalized = normalize_osm_elements(raw_elements, 51.5074, -0.1278)
    assert len(normalized) == 1
    item = normalized[0]

    assert item.id == "way/2002"
    assert item.osm_type == "way"
    assert item.category == "hospital"
    assert item.name == "St Thomas Hospital"
    assert item.emergency == "yes"
    assert item.phone == "+44 20 7188 7188"
    assert item.opening_hours == "24/7"
    assert item.address == "249 Westminster Bridge Rd, London"
    assert item.operator == "NHS Foundation Trust"
    assert item.lat == 51.508
    assert item.lon == -0.129

def test_results_sorted_by_distance_ascending():
    raw_elements = [
        {
            "type": "node",
            "id": 1,
            "lat": 51.5200, # Further away
            "lon": -0.1278,
            "tags": {"amenity": "police", "name": "Far Police"}
        },
        {
            "type": "node",
            "id": 2,
            "lat": 51.5080, # Closer
            "lon": -0.1278,
            "tags": {"amenity": "police", "name": "Near Police"}
        }
    ]

    normalized = normalize_osm_elements(raw_elements, 51.5074, -0.1278)
    assert len(normalized) == 2
    assert normalized[0].name == "Near Police"
    assert normalized[1].name == "Far Police"
    assert normalized[0].distance_meters < normalized[1].distance_meters
