"""
index_manager.py

Module for reading, writing, and updating the ent-sol-malawi index.json file.
Designed to work with the output of build_index.py.
"""

import json
from pathlib import Path
from typing import List, Dict, Any

# --- Paths ---
BASE_DIR = Path(__file__).resolve().parent.parent.parent
INDEX_FILE = BASE_DIR / "index.json"


def read_index(index_file: Path = INDEX_FILE) -> Dict[str, Any]:
    """
    Read the index.json file and return its contents.

    Args:
        index_file (Path): Path to the index.json file.

    Returns:
        dict: Dictionary containing all projects.
    """
    if not index_file.exists():
        return {"projects": []}

    with open(index_file, "r", encoding="utf-8") as f:
        return json.load(f)


def write_index(projects: List[Dict[str, Any]], index_file: Path = INDEX_FILE) -> None:
    """
    Write the given list of projects to index.json.

    Args:
        projects (list[dict]): List of project dictionaries.
        index_file (Path): Path to save the index.json.
    """
    data = {"projects": projects}
    with open(index_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Index updated with {len(projects)} projects → {index_file}")


def add_project(project: Dict[str, Any], index_file: Path = INDEX_FILE) -> None:
    """
    Add a new project to the existing index.json.

    Args:
        project (dict): Project dictionary to add.
        index_file (Path): Path to the index.json.
    """
    index_data = read_index(index_file)
    index_data["projects"].append(project)
    write_index(index_data["projects"], index_file)


def get_project_by_id(project_id: str, index_file: Path = INDEX_FILE) -> Dict[str, Any] | None:
    """
    Retrieve a project from index.json by its id.

    Args:
        project_id (str): The id of the project to retrieve.
        index_file (Path): Path to the index.json.

    Returns:
        dict | None: Project dictionary if found, else None.
    """
    index_data = read_index(index_file)
    for project in index_data.get("projects", []):
        if project.get("id") == project_id:
            return project
    return None


# --- CLI usage for testing ---
if __name__ == "__main__":
    data = read_index()
    print(f"Loaded {len(data.get('projects', []))} projects from index.json")
