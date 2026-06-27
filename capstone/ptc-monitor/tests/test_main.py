import os
os.environ["APP_NAME"] = "test-app"
os.environ["APP_ENV"] = "test"
os.environ["APP_VERSION"] = "1.0.0"

import pytest
from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c


def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "timestamp" in data
    assert "version" in data


def test_root_endpoint(client):
    response = client.get("/")
    assert response.status_code == 200


def test_info_endpoint(client):
    response = client.get("/info")
    assert response.status_code == 200
    data = response.json()
    assert "app_name" in data
    assert "environment" in data


def test_metrics_endpoint(client):
    response = client.get("/metrics")
    assert response.status_code == 200
    data = response.json()
    assert "cpu" in data
    assert "memory" in data
    assert "disk" in data


def test_cpu_endpoint(client):
    response = client.get("/metrics/cpu")
    assert response.status_code == 200
    data = response.json()
    assert "usage_percentage" in data
    assert "core_count" in data


def test_memory_endpoint(client):
    response = client.get("/metrics/memory")
    assert response.status_code == 200
    data = response.json()
    assert "total_memory" in data
    assert "usage_percent" in data


def test_disk_endpoint(client):
    response = client.get("/metrics/disk")
    assert response.status_code == 200
    data = response.json()
    assert "total_gb" in data
    assert "usage_percent" in data


def test_unknown_endpoint_returns_404(client):
    response = client.get("/nonexistent")
    assert response.status_code == 404