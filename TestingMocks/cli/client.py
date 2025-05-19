import requests

# Base URL of the FastAPI server
BASE_URL = "http://127.0.0.1:8000"

def register():
    """
    Registers a new user by sending a POST request to the API.

    This function prompts the user for a username and password, then sends
    the credentials to the `/users/register` endpoint.

    Input:
        - Username: The desired username for registration.
        - Password: The password for the new account.

    API Request:
        POST /users/register
        JSON Payload: {"username": "example", "password": "securepassword"}

    Output:
        Prints the server's response, typically a success message or error details.
    """
    username = input("Enter username: ")
    password = input("Enter password: ")
    response = requests.post(
        f"{BASE_URL}/users/register", json={"username": username, "password": password})
    print(response.json())

def upload():
    """
    Uploads a CSV file for a specific user by sending a POST request.

    This function prompts the user for their user ID and a file path, then 
    uploads the file to the `/files/upload` endpoint.

    Input:
        - User ID: The ID of the user who owns the file.
        - CSV file path: The local path of the CSV file to be uploaded.

    API Request:
        POST /files/upload
        Form Data:
            - user_id: <provided user ID>
            - file: <CSV file>

    Output:
        Prints the server's response, which typically contains success confirmation
        or an error message.
    """
    user_id = input("Enter user ID: ")
    file_path = input("Enter CSV file path: ")
    with open(file_path, "rb") as file:
        response = requests.post(
            f"{BASE_URL}/files/upload", files={"file": file}, data={"user_id": user_id})
    print(response.json())

def get_users():
    """
    Retrieves a list of all registered users.
    """
    response = requests.get(f"{BASE_URL}/users")
    print(response.json())


def get_user_data():
    """
    Retrieves CSV data for a specific user.
    """
    user_id = input("Enter user ID: ")
    response = requests.get(f"{BASE_URL}/users/{user_id}/data")
    print(response.json())
    
if __name__ == "__main__":
    """
    Simple command-line interface to interact with the API.

    The script presents a menu with the following options:
        1. Register a new user.
        2. Upload a CSV file.
        3. Get users
        4. Get user data
        5. Exit the program.

    The user selects an option, and the corresponding function is executed.
    """
    while True:
        print("\n1. Register\n2. Upload CSV\n3. Get Users\n4. Get User Data\n5. Exit")
        choice = input("Select option: ")
        if choice == "1":
            register()
        elif choice == "2":
            upload()
        elif choice == "3":
            get_users()
        elif choice == "4":
            get_user_data()
        elif choice == "5":
            break
