"""Tests for Overpass QL query builder and mirror fallback."""
import pytest
from unittest.mock import patch, AsyncMock
import httpx
from app.services.overpass import build_overpass_query, query_overpass_with_fallback

def test_build_overpass_query_single_category():
    query = build_overpass_query(51.5, -0.12, 2000, ["hospital"])
    assert "nwr(around:2000,51.5,-0.12)" in query
    assert "hospital" in query
    assert "out center body" in query

def test_build_overpass_query_all_categories():
    query = build_overpass_query(40.71, -74.0, 3000, None)
    assert "hospital" in query
    assert "pharmacy" in query
    assert "police" in query
    assert "fire_station" in query
    assert "shelter" in query
    assert "toilets" in query
    assert "out center body" in query

def test_mirror_fallback_on_429_or_failure():
    """Verify that when the first mirror returns 429/504, the system automatically falls back to the next mirror."""
    import asyncio
    async def _run():
        mock_resp_429 = AsyncMock()
        mock_resp_429.status_code = 429

        mock_resp_200 = AsyncMock()
        mock_resp_200.status_code = 200
        mock_resp_200.json = lambda: {
            "elements": [
                {"type": "node", "id": 99, "lat": 51.5, "lon": -0.12, "tags": {"amenity": "hospital", "name": "Fallback Hospital"}}
            ]
        }

        # First mirror fails with 429, second mirror succeeds with 200
        with patch("httpx.AsyncClient.post", side_effect=[mock_resp_429, mock_resp_200]):
            elements, server = await query_overpass_with_fallback(51.5, -0.12, 1000, ["hospital"])
            assert len(elements) == 1
            assert elements[0]["tags"]["name"] == "Fallback Hospital"
            assert server == "overpass-api.de"

    asyncio.run(_run())
