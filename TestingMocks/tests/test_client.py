import requests
import requests_mock


def test_register():
    with requests_mock.Mocker() as m:
        m.post("http://127.0.0.1:8000/users/register",
               json={"message": "User registered successfully"})

        response = requests.post(
            "http://127.0.0.1:8000/users/register", json={"username": "test", "password": "test"})

        assert response.json()["message"] == "User registered successfully"


def test_upload():
    with requests_mock.Mocker() as m:
        m.post("http://127.0.0.1:8000/files/upload",
               json={"message": "File uploaded successfully"})

        with open("test.csv", "w") as f:
            f.write("id,name\n1,Test")

        with open("test.csv", "rb") as file:
            response = requests.post(
                "http://127.0.0.1:8000/files/upload", files={"file": file}, data={"user_id": "1"})

        assert response.json()["message"] == "File uploaded successfully"


def test_get_users():
    with requests_mock.Mocker() as m:
        m.get("http://127.0.0.1:8000/users", json=[
            {"id": 1, "username": "user1"},
            {"id": 2, "username": "user2"},
        ])

        response = requests.get("http://127.0.0.1:8000/users")

        assert response.status_code == 200

        users = response.json()
        assert isinstance(users, list)
        assert all("username" in user and "id" in user for user in users)


def test_get_user_data():
    user_id = 2

    with requests_mock.Mocker() as m:
        m.get(f"http://127.0.0.1:8000/users/{user_id}/data", json=[
            {"id": 1, "content": "data1"},
            {"id": 2, "content": "data2"},
        ])

        response = requests.get(f"http://127.0.0.1:8000/users/{user_id}/data")

        assert response.status_code == 200

        data = response.json()
        assert isinstance(data, list)
        assert all("id" in entry and "content" in entry for entry in data)
