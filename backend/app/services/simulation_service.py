# backend/app/services/simulation_service.py
from app.domain.schemas import SimInput, SimResult
from app.domain.physics.impact import kinetic_energy_megatons, damage_radii_km, circle_geojson

async def run_simulation(p: SimInput) -> SimResult:
    energy_mt = kinetic_energy_megatons(p.diameter_m, p.velocity_kms)
    radii = damage_radii_km(energy_mt)

    features = [
        {"type": "Feature", "geometry": {"type": "Point", "coordinates": [p.lon, p.lat]},
         "properties": {"type": "impact_point", "energy_mt": energy_mt}},
        circle_geojson(p.lon, p.lat, radii["severe"]),
        circle_geojson(p.lon, p.lat, radii["moderate"]),
        circle_geojson(p.lon, p.lat, radii["light"]),
    ]
    geojson = {"type": "FeatureCollection", "features": features}
    return SimResult(geojson=geojson, energy_mt=energy_mt, damage_radii_km=radii)
