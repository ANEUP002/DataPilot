from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.endpoints import router
from app.core.database import create_db_and_tables

app = FastAPI(title="DataPilot Backend", version="0.1.0")

# CORS middleware for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# Include API routes
app.include_router(router, prefix="/api", tags=["data"])

@app.get("/")
def read_root():
    return {"message": "Welcome to DataPilot API"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
