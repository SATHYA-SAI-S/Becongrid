"""Tests for routing service and external navigation fallbacks."""
import pytest
from unittest.mock import patch, AsyncMock
from app.services.routing import get_route

def test_get_route_success():
    import asyncio
    async def _run():
        mock_osrm_json = {
            "routes": [
                {
                    "distance": 1420.5,
                    "duration": 210.0,
                    "geometry": {
                        "type": "LineString",
                        "coordinates": [[-0.1278, 51.5074], [-0.1250, 51.5080]]
                    }
                }
            ]
        }

        mock_resp = AsyncMock()
        mock_resp.status_code = 200
        mock_resp.json = lambda: mock_osrm_json

        with patch("httpx.AsyncClient.get", return_value=mock_resp):
            res = await get_route(51.5074, -0.1278, 51.5080, -0.1250, profile="driving")
            assert res.status == "ok"
            assert res.distance_meters == 1420.5
            assert res.duration_seconds == 210.0
            assert res.geometry["type"] == "LineString"
            assert "disclaimer" in res.model_dump()

    asyncio.run(_run())
