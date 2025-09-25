# Entertainment Solutions Malawi (Ent-Sol-Malawi)

A centralized hub for documenting, showcasing, and automating creative-tech projects in Malawi. This repository combines Python (FastAPI) and SvelteKit to provide a dynamic platform for media, case studies, guides, and automation tools.

---

## Table of Contents
1. [Overview](#overview)  
2. [Directory Structure](#directory-structure)  
3. [Features](#features)  
4. [Getting Started](#getting-started)  
5. [Scripts & Automation](#scripts--automation)  
6. [Contributing](#contributing)  
7. [License](#license)  

---

## Overview
Ent-Sol-Malawi is designed to be the central repository for all entertainment and technology projects in Malawi. It stores project media, documentation, and metadata while providing automation scripts for indexing and thumbnail generation. The SvelteKit frontend provides an interactive interface for browsing and filtering projects, while the Python backend powers data processing and API endpoints.

---

## Directory Structure
ent-sol-malawi/
├─ docs/ # MkDocs site / case studies + guides
├─ backend/
│ ├─ app/
│ │ ├─ main.py # FastAPI app
│ │ └─ api/ # Endpoints for projects, media, reports
│ ├─ requirements.txt
│ └─ scripts/
│ ├─ build_index.py # Scan media & build index.json/db
│ └─ thumb_generator.py # Generate thumbnails automatically
├─ frontend/
│ ├─ svelte.config.js
│ ├─ package.json
│ └─ src/
│ ├─ routes/ # Pages & API endpoints
│ ├─ lib/ # Reusable components
│ ├─ stores/ # State management
│ └─ assets/ # CSS, images, icons
├─ media/
│ ├─ project-a/
│ │ ├─ screenshot-1.png
│ │ └─ meta.yaml
│ └─ ...
├─ .github/
│ └─ workflows/ci.yml # CI/CD workflow
├─ README.md
└─ index.json # Generated index of projects

yaml
Copy code

---

## Features
- **Central Repository**: Organize all projects, media, and metadata in one location.  
- **Automation**: Scripts for indexing projects (`build_index.py`) and generating thumbnails (`thumb_generator.py`).  
- **Interactive Frontend**: Browse, filter, and explore projects with SvelteKit.  
- **Documentation**: MkDocs-powered case studies, guides, and tutorials.  
- **Extensible**: Easily add new projects, features, and automation scripts.

---

## Getting Started
### Prerequisites
- Python 3.10+  
- Node.js 20+  
- Git  

### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
Frontend Setup

 
cd frontend
npm install
npm run dev
Building Project Index



cd backend/scripts
python build_index.py
python thumb_generator.py
Scripts & Automation
build_index.py: Scans media/ folders, reads meta.yaml metadata, and generates index.json.

thumb_generator.py: Automatically generates thumbnails for media assets to be displayed in the frontend.

These scripts can also be imported and called programmatically from FastAPI endpoints for live updates.

Contributing
Contributions are welcome!

Fork the repository

Create a new branch (git checkout -b feature/your-feature)

Commit your changes (git commit -m "Add feature")

Push to the branch (git push origin feature/your-feature)

Open a Pull Request

License
This project is licensed under the MIT License.

Maintainer: Entertainment Solutions Malawi Team

pgsql
Copy code

---

If you want, I can **also add a “dynamic project showcase” section** in this README that pulls from `index.json` and shows each project’s title, tags, and thumbnail, so the README itself feels interactive when browsing on GitHub. This is often done with badges or linked images.  


Do you want me to do that?
