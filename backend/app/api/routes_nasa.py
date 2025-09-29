from fastapi import APIRouter, HTTPException, Query
from typing import Optional
from app.services.nasa_service import get_neos_by_day

router = APIRouter(prefix="/nasa", tags=["nasa"])

@router.get("/today")
async def nasa_today(day: Optional[str] = Query(None, description="YYYY-MM-DD; por defecto hoy")):
    try:
        items = await get_neos_by_day(day)
        return {"date": day, "count": len(items), "items": items}
    except Exception as e:
        raise HTTPException(status_code=502, detail=str(e))
