import httpx
from typing import Dict, Any, Optional
from app.core.config import settings

class NASANeoClient:
    BASE_URL = "https://api.nasa.gov/neo/rest/v1"

    def __init__(self, api_key: Optional[str] = None, timeout: float = 30.0):
        self.api_key = api_key or settings.NASA_API_KEY
        self.timeout = timeout

    async def _get(self, path: str, params: Dict[str, Any]) -> Dict[str, Any]:
        params = {**params, "api_key": self.api_key}
        url = f"{self.BASE_URL}{path}"
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            r = await client.get(url, params=params)
            r.raise_for_status()
            return r.json()

    # 1) Feed por fechas (hasta 7 días por llamada)
    async def feed(self, start_date: str, end_date: str) -> Dict[str, Any]:
        """
        start_date / end_date: 'YYYY-MM-DD'
        Devuelve NEOs cercanos a la Tierra en el rango.
        """
        return await self._get("/feed", {"start_date": start_date, "end_date": end_date})

    # 2) Cercanos hoy (atajo usando feed con un día)
    async def today(self, date: str) -> Dict[str, Any]:
        return await self.feed(date, date)

    # 3) Info por ID de asteroide
    async def lookup(self, neo_id: str) -> Dict[str, Any]:
        return await self._get(f"/neo/{neo_id}", {})

    # 4) Navegar (paginado) por catálogo NEO
    async def browse(self, page: int = 0, size: int = 20) -> Dict[str, Any]:
        return await self._get("/neo/browse", {"page": page, "size": size})
