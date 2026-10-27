
"""Tests for the FastAPI application."""

from fastapi.testclient import TestClient
from api.main import app


client = TestClient(app)


def test_home():
    """Check the home endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Bienvenue sur mon API Python !"
    }


def test_health():
    """Check the health endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
