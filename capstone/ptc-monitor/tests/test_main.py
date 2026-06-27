import os

os.environ["APP_NAME"] = "test-app"
os.environ["APP_ENV"] = "test"
os.environ["APP_VERSION"] = "1.0.0"

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_endpoint():
    """Health endpoint should return 200 with healthy status."""
    response = client.get("/health")
    assert response.status_code == 200

    data = response.json()
    assert data["status"] == "healthy"
    assert "timestamp" in data
    assert "version" in data


def test_root_endpoint():
    """Root endpoint should return 200."""
    response = client.get("/")
    assert response.status_code == 200


def test_info_endpoint():
    """Info endpoint should return app metadata."""
    response = client.get("/info")
    assert response.status_code == 200

    data = response.json()
    assert "app_name" in data
    assert "environment" in data
    assert "version" in data


def test_metrics_dashboard():
    """Metrics endpoint should return CPU, memory and disk metrics."""
    response = client.get("/metrics")
    assert response.status_code == 200

    data = response.json()

    assert "timestamp" in data

    # CPU metrics
    assert "cpu" in data
    assert "usage_percentage" in data["cpu"]
    assert "core_count" in data["cpu"]
    assert "core_count_logical" in data["cpu"]

    # Memory metrics
    assert "memory" in data
    assert "total_memory" in data["memory"]
    assert "memory_availabel" in data["memory"]
    assert "memory_usage" in data["memory"]
    assert "usage_percent" in data["memory"]

    # Disk metrics
    assert "disk" in data
    assert "total_gb" in data["disk"]
    assert "used_gb" in data["disk"]
    assert "free_gb" in data["disk"]
    assert "usage_percent" in data["disk"]


def test_cpu_endpoint():
    """CPU endpoint should return usage percent."""
    response = client.get("/metrics/cpu")
    assert response.status_code == 200

    data = response.json()

    assert "usage_percentage" in data
    assert "core_count" in data
    assert "core_count_logical" in data


def test_memory_endpoint():
    """Memory endpoint should return usage data."""
    response = client.get("/metrics/memory")
    assert response.status_code == 200

    data = response.json()

    assert "total_memory" in data
    assert "memory_availabel" in data
    assert "memory_usage" in data
    assert "usage_percent" in data


def test_disk_endpoint():
    """Disk endpoint should return usage data."""
    response = client.get("/metrics/disk")
    assert response.status_code == 200

    data = response.json()

    assert "total_gb" in data
    assert "used_gb" in data
    assert "free_gb" in data
    assert "usage_percent" in data


def test_unknown_endpoint_returns_404():
    """Unknown endpoints should return 404."""
    response = client.get("/nonexistent")
    assert response.status_code == 404