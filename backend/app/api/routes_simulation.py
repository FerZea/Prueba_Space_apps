from fastapi import APIRouter, HTTPException
from app.domain.schemas import SimInput, SimResult
from app.services.simulation_service import run_simulation

router = APIRouter(prefix="/simulate", tags=["simulate"])



#Plantilla basica 


@router.post("/impact", response_model=SimResult)
async def simulate_impact(body: SimInput):
    try:
        return await run_simulation(body)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


#Con esto es para que funcione la simulacion de impacto

'''
@router.post("/impact", response_model=GeoJson)
async def simulate_impact(payload: SimInput):
    import math
    lon, lat = payload.lon, payload.lat
    r_km = max(2.0, min(25.0, payload.diameter_m / 20.0))
    steps = 32
    coords = []
    for i in range(steps + 1):
        ang = 2 * math.pi * i / steps
        dlat = (r_km / 111.32) * math.cos(ang)
        dlon = (r_km / (111.32 * math.cos(math.radians(lat)))) * math.sin(ang)
        coords.append([lon + dlon, lat + dlat])
    return {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {"type": "Polygon", "coordinates": [coords]},
                "properties": {"diameter_m": payload.diameter_m, "velocity_kms": payload.velocity_kms},
            },
            {"type": "Feature", "geometry": {"type": "Point", "coordinates": [lon, lat]}, "properties": {"label": "Impact"}},
        ],
    }
'''