import os
import datetime
import logging

from fastapi import FastAPI, HTTPException

from metrics import (
    get_all_metrics,
    get_cpu_metrics,
    get_disk_metrics,
    get_memory_metrics,
)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="PTC Devops Monitoring Dashboard",
    description="Real-time system metrics API build with python , docker , kubernetes , fastapi",
    version=os.environ.get("APP_VERSION","1.0.0"),
)

@app.on_event("startup")
async def startup_event():
    logger.info(f"Starting PTC Monitor v{os.environ.get('APP_VERSION','1.0.0')}")
    logger.info(f"Environment: {os.environ.get('APP_ENV','development')}")
    logger.info("ALL Endpoints are ready")

@app.get("/health")
def health_check():
    """
    Kubernetes liveness probe endpoint.
    Returns 200 if app is running correctly.
    """
    return {
        "status":"healthy",
        "timestamp": datetime.datetime.now().isoformat(),
        "version": os.environ.get("APP_VERSION", "1.0.0"),
    }

@app.get("/info")
def get_info():
    """Returns application metadata."""
    return {
        "app_name": os.environ.get("APP_NAME", "PTC Monitor"),
        "version": os.environ.get("APP_VERSION", "1.0.0"),
        "environment": os.environ.get("APP_ENV", "development"),
        "built_by": "Yash Kanawade",
        "stack": ["Python", "FastAPI", "Docker", "Kubernetes"],
    }

@app.get("/metrics")
def get_metrics():
    """returns all system metrics"""
    logger.info("Fetching all metrics")
    return get_all_metrics()

@app.get("/metrics/cpu")
def get_cpu():
    """Returns all cpu metrics"""
    logger.info("Fetching CPU metrics")
    return get_cpu_metrics()

@app.get("/metrics/memory")
def get_memory():
    """Return all memory metrics"""
    logger.info("Fetching memory metrics")
    return get_memory_metrics()

@app.get("/metrics/disk")
def get_disk():
    """Return all disk metrics"""
    logger.info("Fetching disk metrics")
    return get_disk_metrics()


@app.get("/")
def root():
    return{
        "message":"PTC Devops Monitoring Dashboard",
        "docs":"/docs",
        "health":"/health",
        "metrics":"/metrics",
    }