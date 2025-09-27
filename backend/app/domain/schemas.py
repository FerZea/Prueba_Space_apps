from pydantic import BaseModel
from typing import Any, Dict, List

class SimInput(BaseModel):
    lat: float
    lon: float
    diameter_m: float
    velocity_kms: float

class GeoJson(BaseModel):
    type: str
    features: List[Dict[str, Any]]
