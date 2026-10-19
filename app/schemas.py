"""Pydantic schemas and data validation models."""
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field

class ResourceItem(BaseModel):
    id: str = Field(description="Unique identifier (e.g. node/123456 or way/78910)")
    osm_type: str = Field(description="OSM element type: node, way, or relation")
    osm_id: int = Field(description="OSM numerical ID")
    category: str = Field(description="Normalized category id: hospital, clinic, pharmacy, etc.")
    name: str = Field(description="Facility or resource name")
    lat: float = Field(description="Latitude in decimal degrees")
    lon: float = Field(description="Longitude in decimal degrees")
    distance_meters: float = Field(description="Calculated distance in meters from search point")
    address: Optional[str] = Field(default=None, description="Physical address if reported in OSM")
    phone: Optional[str] = Field(default=None, description="Contact phone number if reported in OSM")
    emergency: Optional[str] = Field(default=None, description="Emergency service flag (e.g. 'yes' for ER)")
    opening_hours: Optional[str] = Field(default=None, description="Reported operating hours")
    wheelchair: Optional[str] = Field(default=None, description="Wheelchair accessibility status")
    operator: Optional[str] = Field(default=None, description="Managing organisation or operator")
    tags_raw: Dict[str, Any] = Field(default_factory=dict, description="Complete raw tags from OSM for transparency")

class MetaInfo(BaseModel):
    lat: float
    lon: float
    radius_meters: int
    cached: bool
    retrieved_at: str
    cache_age_seconds: float
    upstream_server: str
    attribution: str

class ResourcesResponse(BaseModel):
    status: str = "ok"
    meta: MetaInfo
    count: int
    data: List[ResourceItem]
    disclaimer: str

class GeocodeResult(BaseModel):
    place_id: Optional[int] = None
    name: str
    display_name: str
    lat: float
    lon: float
    type: Optional[str] = None
    boundingbox: Optional[List[str]] = None

class GeocodeResponse(BaseModel):
    status: str = "ok"
    results: List[GeocodeResult]

class RouteResponse(BaseModel):
    status: str = "ok"
    distance_meters: float
    duration_seconds: float
    geometry: Dict[str, Any]
    disclaimer: str
