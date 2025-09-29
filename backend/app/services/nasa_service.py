# backend/app/services/nasa_service.py
from datetime import date
from typing import List, Dict, Any, Optional
from app.clients.nasa_neo import NASANeoClient

async def get_neos_by_day(day: Optional[str] = None) -> List[Dict[str, Any]]:
    """Devuelve la lista de NEOs para una fecha dada (YYYY-MM-DD). Si no se pasa fecha, usa hoy."""
    target = day or date.today().isoformat()
    client = NASANeoClient()
    feed = await client.today(target)  # usa el feed con start=end=target
    return feed.get("near_earth_objects", {}).get(target, [])
