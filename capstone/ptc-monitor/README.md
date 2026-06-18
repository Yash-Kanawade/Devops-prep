# PTC DevOps Monitoring Dashboard

A real-time system metrics API built with Python FastAPI, containerized 
with Docker, and designed for Kubernetes deployment.

## Tech Stack
- **Python 3.11** + **FastAPI** — REST API
- **psutil** — System metrics collection
- **Docker** + **Docker Compose** — Containerization
- **Kubernetes** — Orchestration (coming next)

## Endpoints

| Endpoint | Description |
|----------|-------------|
| `GET /` | Root — links to all endpoints |
| `GET /health` | Kubernetes liveness probe |
| `GET /info` | App metadata |
| `GET /metrics` | All system metrics |
| `GET /metrics/cpu` | CPU usage |
| `GET /metrics/memory` | Memory usage |
| `GET /metrics/disk` | Disk usage |
| `GET /docs` | Interactive API documentation |

## Run locally

### With Docker Compose (recommended)
```bash
docker compose up -d
open http://localhost:8000/docs
```

### Without Docker
```bash
pip install -r requirements.txt
APP_NAME=PTC-Monitor APP_ENV=development uvicorn app.main:app --reload
```

## Project structure