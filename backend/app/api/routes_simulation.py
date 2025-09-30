# app/api/routes_simulation.py
from fastapi import APIRouter, HTTPException
from app.domain.schemas import SimInput, SimResult
from app.services.simulation_service import run_simulation

router = APIRouter(
    prefix="/simulate",
    tags=["simulate"]
)

@router.post(
    "/impact",
    response_model=SimResult,
    summary="Simula el impacto de un meteorito",
    description=(
        "Recibe parámetros de entrada (lat, lon, diámetro en metros y velocidad en km/s), "
        "ejecuta los cálculos de física/geométricos en domain/ y devuelve un GeoJSON con las "
        "zonas de daño (FeatureCollection), además de la energía (Mt) y radios estimados (km)."
    ),
)
async def simulate_impact(body: SimInput) -> SimResult:
    """
    Endpoint principal de simulación.
    - Valida el payload (Pydantic)
    - Delega la orquestación a services/
    - Devuelve un SimResult tipado para el frontend
    """
    try:
        result = await run_simulation(body)
        return result
    except ValueError as e:
        # Errores de validación/calculo de dominio
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        # Cualquier otro error inesperado
        raise HTTPException(status_code=500, detail="Simulation failed")
