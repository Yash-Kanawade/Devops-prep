# DevOps Prep — Yash Kanawade

8-week DevOps preparation before joining PTC Software as a DevOps Intern.

## Structure

### week1-linux/
Bash scripting and Linux fundamentals.
- `log_analyser.sh` — analyses application logs, reports HEALTHY/UNHEALTHY status

### week2-docker/
Docker projects built during Docker week.
- `python-app/` — Python app containerized with Docker
- `compose-app/` — Multi-container app with Docker Compose
- `health-server/` — HTTP health check server in Docker

### capstone/ptc-monitor/
**Main project** — DevOps Monitoring Dashboard built with Python FastAPI, Docker, and Kubernetes.
- Real-time system metrics: CPU, memory, disk
- Endpoints: /health, /metrics, /docs
- Production-grade Dockerfile with non-root user
- Docker Compose setup with health checks
- Docker Hub: hub.docker.com/r/yashkanawade/ptc-monitor

## Tech Stack
Python · FastAPI · Docker · Kubernetes · Linux · Bash · Git
