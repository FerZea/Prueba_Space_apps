from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes_simulation import router as sim_router
from app.api.routes_nasa import router as nasa_router

app = FastAPI(title="Meteor Impact API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(sim_router, prefix="/api", tags=["simulate"])
app.include_router(nasa_router, prefix="/api", tags=["nasa"])

@app.get("/api/health")
def health():
    return {"ok": True}
