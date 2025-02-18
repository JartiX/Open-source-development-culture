import requests

BASE_URL = "http://127.0.0.1:8000"


def register():
    username = input("Enter username: ")
    password = input("Enter password: ")
    response = requests.post(
        f"{BASE_URL}/users/register", json={"username": username, "password": password})
    print(response.json())


def upload():
    user_id = input("Enter user ID: ")
    file_path = input("Enter CSV file path: ")
    with open(file_path, "rb") as file:
        response = requests.post(
            f"{BASE_URL}/files/upload", files={"file": file}, data={"user_id": user_id})
    print(response.json())


if __name__ == "__main__":
    while True:
        print("\n1. Register\n2. Upload CSV\n3. Exit")
        choice = input("Select option: ")
        if choice == "1":
            register()
        elif choice == "2":
            upload()
        elif choice == "3":
            break
