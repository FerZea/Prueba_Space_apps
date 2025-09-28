import httpx
from typing import Dict, Any

class NASANeoClient:
    def __init__(self, api_key: str):
        self.base = "https://api.nasa.gov/neo/rest/v1"
        self.api_key = api_key

    async def feed(self, start_date: str, end_date: str) -> Dict[str, Any]:
        url = f"{self.base}/feed"
        params = {"start_date": start_date, "end_date": end_date, "api_key": self.api_key}
        async with httpx.AsyncClient(timeout=30) as client:
            r = await client.get(url, params=params)
            r.raise_for_status()
            return r.json()
