from fastapi.testclient import TestClient
from app.main import app
import io
from app.database import SessionLocal
from app.models import User


client = TestClient(app)


def test_register_user():
    db = SessionLocal()

    user = db.query(User).filter(User.username == "test").first()
    db.delete(user)
    db.commit()

    response = client.post(
        "/users/register", json={"username": "test", "password": "test"})
    
    assert response.status_code == 200
    assert response.json()["message"] == "User registered successfully"


def test_upload_file():
    csv_content = io.BytesIO(b"id,name\n1,Test")

    files = {"file": ("test.csv", csv_content, "text/csv")}
    response = client.post("/files/upload?user_id=1", files=files)
    
    assert response.status_code == 200
    assert response.json()["message"] == "File uploaded successfully"


def test_get_users():
    response = client.get("/users")
    assert response.status_code == 200
    users = response.json()
    assert isinstance(users, list)
    assert all("username" in user and "id" in user for user in users)


def test_get_user_data():
    user_id = 2
    response = client.get(f"/users/{user_id}/data")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert all("id" in entry and "content" in entry for entry in data)