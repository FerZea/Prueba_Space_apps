import httpx
from typing import Dict, Any
from app.core.config import settings

class NASANeoClient:
    def __init__(self):
        self.base = "https://api.nasa.gov/neo/rest/v1"
        self.api_key = settings.NASA_API_KEY

    async def feed(self, start_date: str, end_date: str):
        async with httpx.AsyncClient(timeout=30) as client:
            r = await client.get(
                f"{self.base}/feed",
                params={"start_date": start_date, "end_date": end_date, "api_key": self.api_key},
            )
            r.raise_for_status()
            return r.json()