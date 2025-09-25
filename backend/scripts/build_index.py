"""
build_index.py

Scans the /media directory for all projects, reads their metadata from meta.yaml,
collects associated media files, and generates a centralized index.json.

Can be run as a script or imported as a module for API use.
"""

import json
from pathlib import Path
from datetime import datetime
import yaml

# --- Paths ---
BASE_DIR = Path(__file__).resolve().parent.parent.parent
MEDIA_DIR = BASE_DIR / "media"
OUTPUT_FILE = BASE_DIR / "index.json"


def scan_media(media_dir: Path = MEDIA_DIR) -> list[dict]:
    """
    Scan the media directory for project folders, read metadata, and collect media files.

    Args:
        media_dir (Path): Path to the media directory.

    Returns:
        list[dict]: List of project entries with metadata and media references.
    """
    projects = []

    for project_path in sorted(media_dir.iterdir()):
        if not project_path.is_dir():
            continue

        meta_file = project_path / "meta.yaml"
        if not meta_file.exists():
            print(f"Skipping {project_path.name}: no meta.yaml found")
            continue

        # Load metadata
        try:
            with open(meta_file, "r", encoding="utf-8") as f:
                metadata = yaml.safe_load(f) or {}
        except yaml.YAMLError as e:
            print(f"Error reading {meta_file}: {e}")
            continue

        # Collect media files
        media_files = [
            file.name
            for file in project_path.iterdir()
            if file.suffix.lower() in {".png", ".jpg", ".jpeg", ".gif", ".mp4"}
        ]

        project_entry = {
            "id": project_path.name,
            "title": metadata.get("title", project_path.name),
            "description": metadata.get("description", ""),
            "tags": metadata.get("tags", []),
            "date": metadata.get("date", str(datetime.today().date())),
            "url": metadata.get("url", ""),
            "media": media_files,
        }

        projects.append(project_entry)

    return projects


def build_index(output_file: Path = OUTPUT_FILE) -> None:
    """
    Build the centralized index.json from the media directory.

    Args:
        output_file (Path): Path to save the generated index.json
    """
    projects = scan_media()
    data = {"projects": projects}

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Index built with {len(projects)} projects → {output_file}")


# --- CLI usage ---
if __name__ == "__main__":
    build_index()
