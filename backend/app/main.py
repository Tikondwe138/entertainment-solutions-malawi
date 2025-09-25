from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import routers
from app.api import projects, media, reports

# Create FastAPI instance
app = FastAPI(
    title="Entertainment Solutions Malawi API",
    description="Backend API for Ent-Sol-Malawi project repository",
    version="0.1.0"
)

# CORS setup (adjust as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # replace with ["http://localhost:5173"] for SvelteKit
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(projects.router, prefix="/api/projects", tags=["Projects"])
app.include_router(media.router, prefix="/api/media", tags=["Media"])
app.include_router(reports.router, prefix="/api/reports", tags=["Reports"])

@app.get("/")
async def root():
    return {"message": "Welcome to Entertainment Solutions Malawi API"}
