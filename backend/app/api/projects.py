from fastapi import APIRouter, HTTPException
import json
from pathlib import Path

router = APIRouter()

INDEX_PATH = Path(__file__).resolve().parents[2] / "index.json"

@router.get("/")
async def list_projects():
    """Return all projects from index.json"""
    if not INDEX_PATH.exists():
        raise HTTPException(status_code=404, detail="index.json not found")
    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

@router.get("/{project_id}")
async def get_project(project_id: str):
    """Return a single project by ID"""
    if not INDEX_PATH.exists():
        raise HTTPException(status_code=404, detail="index.json not found")
    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    project = next((p for p in data if p.get("id") == project_id), None)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project
