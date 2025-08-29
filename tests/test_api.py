"""
Test suite for Oreus API
"""
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root_endpoint():
    """Test the root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "status" in data
    assert data["status"] == "running"


def test_health_check():
    """Test health check endpoint"""
    response = client.get("/v1/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "environment" in data
    assert "version" in data
    assert "services" in data


def test_config_endpoint():
    """Test configuration endpoint"""
    response = client.get("/v1/config")
    assert response.status_code == 200
    data = response.json()
    assert "environment" in data
    assert "aws_region" in data
    assert "project_name" in data


def test_providers_endpoint():
    """Test AI providers endpoint"""
    response = client.get("/v1/providers")
    assert response.status_code == 200
    data = response.json()
    assert "providers" in data
    providers = data["providers"]
    assert "openai" in providers
    assert "anthropic" in providers
    assert "xai" in providers


def test_editor_endpoint():
    """Test code editor endpoint"""
    response = client.get("/v1/editor")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]


def test_projects_list_empty():
    """Test projects list when empty"""
    response = client.get("/v1/projects")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


def test_ai_completion_invalid_provider():
    """Test AI completion with invalid provider"""
    response = client.post(
        "/v1/ai/completion",
        json={
            "provider": "invalid",
            "model": "test-model",
            "prompt": "Hello world"
        }
    )
    assert response.status_code == 400