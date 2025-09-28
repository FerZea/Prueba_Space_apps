# backend/app/domain/schemas.py
from typing import Dict, Any
from pydantic import BaseModel

class SimInput(BaseModel):
    lat: float
    lon: float
    diameter_m: float
    velocity_kms: float

class SimResult(BaseModel):
    geojson: Dict[str, Any]
    energy_mt: float
    damage_radii_km: Dict[str, float]

__all__ = ["SimInput", "SimResult"]



#class GeoJson(BaseModel):
#    type: str
#    features: List[Dict[str, Any]]
