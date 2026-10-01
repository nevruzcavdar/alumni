import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_swagger_ui_endpoint():
    """Verify Swagger UI is accessible at /api/swagger."""
    response = client.get("/api/swagger")
    assert response.status_code == 200
    assert "swagger-ui" in response.text.lower() or "openapi" in response.text.lower() or "html" in response.headers.get("content-type", "")


def test_docs_redirect_to_swagger():
    """Verify /docs redirects to /api/swagger."""
    response = client.get("/docs", follow_redirects=False)
    assert response.status_code in (307, 308, 302, 301)
    assert response.headers["location"] == "/api/swagger"


def test_crud_lifecycle_for_users():
    """Verify full CRUD lifecycle on /api/users."""
    # 1. CREATE (POST)
    new_user_data = {
        "email": "test.graduate@university.edu",
        "full_name": "Test Graduate",
        "role": "alumni",
        "graduation_year": 2022,
        "major": "Computer Engineering",
        "company": "Antigravity Labs",
        "position": "Junior Engineer",
        "bio": "Alumni member test bio.",
        "is_active": True,
    }
    create_resp = client.post("/api/users", json=new_user_data)
    assert create_resp.status_code == 201
    created_user = create_resp.json()
    user_id = created_user["id"]
    assert created_user["email"] == new_user_data["email"]

    # 2. READ ALL (GET)
    list_resp = client.get("/api/users")
    assert list_resp.status_code == 200
    users_list = list_resp.json()
    assert any(u["id"] == user_id for u in users_list)

    # 3. READ ONE (GET /{id})
    get_resp = client.get(f"/api/users/{user_id}")
    assert get_resp.status_code == 200
    assert get_resp.json()["id"] == user_id
    assert get_resp.json()["email"] == new_user_data["email"]

    # 4. UPDATE (PUT /{id})
    update_data = {
        "position": "Mid-level Engineer",
        "company": "DeepMind",
    }
    put_resp = client.put(f"/api/users/{user_id}", json=update_data)
    assert put_resp.status_code == 200
    updated_user = put_resp.json()
    assert updated_user["position"] == "Mid-level Engineer"
    assert updated_user["company"] == "DeepMind"

    # 5. DELETE (DELETE /{id})
    del_resp = client.delete(f"/api/users/{user_id}")
    assert del_resp.status_code == 200

    # 6. VERIFY NOT FOUND (GET /{id})
    missing_resp = client.get(f"/api/users/{user_id}")
    assert missing_resp.status_code == 404
