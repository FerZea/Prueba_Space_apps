from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes_simulation import router as sim_router

app = FastAPI(title="Meteor Impact API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(sim_router, prefix="/api/simulate", tags=["simulate"])
