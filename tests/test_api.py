"""Integration tests for FastAPI endpoints."""
import pytest
from unittest.mock import patch, AsyncMock
from fastapi.testclient import TestClient
from app.main import app
from app.cache import resource_cache

client = TestClient(app)

def setup_function():
    resource_cache.clear()

def test_health_check_endpoint():
    response = client.get("/api/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "cache" in data

def test_index_html_served():
    response = client.get("/")
    assert response.status_code == 200
    assert "Emergency Resource Map" in response.text
    assert "<!DOCTYPE html>" in response.text

def test_resources_validation_errors():
    # Missing lat/lon
    res = client.get("/api/resources")
    assert res.status_code == 422

    # Lat out of range
    res = client.get("/api/resources?lat=95.0&lon=0.0")
    assert res.status_code == 422

    # Radius out of range (> 10000m)
    res = client.get("/api/resources?lat=51.5&lon=-0.12&radius=50000")
    assert res.status_code == 422

def test_resources_upstream_failure_returns_honest_503():
    """Verify that if upstream Overpass fails, API returns an honest 503 instead of invented data."""
    with patch("app.main.query_overpass_with_fallback", side_effect=RuntimeError("Connection timed out")):
        res = client.get("/api/resources?lat=51.5074&lon=-0.1278")
        assert res.status_code == 503
        data = res.json()
        assert "OpenStreetMap upstream service unavailable" in data["detail"]

def test_resources_live_and_cached_flow():
    mock_elements = [
        {
            "type": "node",
            "id": 555,
            "lat": 51.5075,
            "lon": -0.1279,
            "tags": {
                "amenity": "hospital",
                "name": "Central London Hospital",
                "emergency": "yes",
                "phone": "+44 20 7946 0000"
            }
        }
    ]

    with patch("app.main.query_overpass_with_fallback", return_value=(mock_elements, "overpass-api.de")):
        # First query: Cache MISS (live from OSM)
        res1 = client.get("/api/resources?lat=51.5074&lon=-0.1278&categories=hospital")
        assert res1.status_code == 200
        data1 = res1.json()
        assert data1["meta"]["cached"] is False
        assert data1["meta"]["upstream_server"] == "overpass-api.de"
        assert data1["count"] == 1
        assert data1["data"][0]["name"] == "Central London Hospital"
        assert data1["data"][0]["phone"] == "+44 20 7946 0000"

        # Second identical query: Cache HIT (cached=True)
        res2 = client.get("/api/resources?lat=51.5074&lon=-0.1278&categories=hospital")
        assert res2.status_code == 200
        data2 = res2.json()
        assert data2["meta"]["cached"] is True
        assert data2["meta"]["cache_age_seconds"] >= 0.0
        assert data2["count"] == 1
        assert data2["data"][0]["id"] == "node/555"

def test_geocode_endpoint():
    mock_results = [
        {"place_id": 1, "name": "London", "display_name": "London, Greater London, England", "lat": 51.5074, "lon": -0.1278}
    ]
    with patch("app.main.search_locations", return_value=mock_results):
        res = client.get("/api/geocode?q=London")
        assert res.status_code == 200
        data = res.json()
        assert data["status"] == "ok"
        assert len(data["results"]) == 1
        assert data["results"][0]["name"] == "London"
