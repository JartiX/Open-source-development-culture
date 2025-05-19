import os
import sys
import unittest.mock as mock
import io
import requests_mock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cli.client import register, upload, get_users, get_user_data, BASE_URL


def test_register():
    """
    Tests the user registration function from the client module.
    
    This test mocks user input and HTTP requests to verify that the register function
    works correctly with the mocked API.
    """
    with requests_mock.Mocker() as m:
        m.post(f"{BASE_URL}/users/register", 
               json={"message": "User registered successfully"},
               status_code=200)
        
        with mock.patch('builtins.input', side_effect=["test_user", "test_password"]):
            original_stdout = sys.stdout
            sys.stdout = io.StringIO()
            
            register()
            
            output = sys.stdout.getvalue()
            sys.stdout = original_stdout
            
            assert m.last_request.json() == {"username": "test_user", "password": "test_password"}
            
            assert "User registered successfully" in output


def test_register_error():
    """
    Tests the register function with an error response from the API.
    
    This test verifies that the client properly handles and displays error messages
    from the API when registration fails.
    """
    with requests_mock.Mocker() as m:
        m.post(f"{BASE_URL}/users/register", 
               json={"detail": "Username already exists"}, 
               status_code=400)
        
        with mock.patch('builtins.input', side_effect=["existing_user", "password"]):
            original_stdout = sys.stdout
            sys.stdout = io.StringIO()
            
            register()
            
            output = sys.stdout.getvalue()
            sys.stdout = original_stdout
            
            assert "Username already exists" in output


def test_upload():
    """
    Tests the file upload function from the client module.
    
    This test mocks user input, file operations, and HTTP requests to verify that
    the upload function works correctly with the mocked API.
    """
    with requests_mock.Mocker() as m:
        m.post(f"{BASE_URL}/files/upload", 
               json={"message": "File uploaded successfully"},
               status_code=200)

        with mock.patch('builtins.input', side_effect=["1", "test.csv"]):
            mock_file = mock.mock_open(read_data=b"id,name\n1,Test")
            
            original_stdout = sys.stdout
            sys.stdout = io.StringIO()
            
            with mock.patch('builtins.open', mock_file):
                upload()
            
            output = sys.stdout.getvalue()
            sys.stdout = original_stdout
            
            assert "user_id" in m.last_request.text
            assert "1" in m.last_request.text
            
            assert "File uploaded successfully" in output


def test_upload_error():
    """
    Tests the upload function with an error response from the API.
    
    This test verifies that the client properly handles and displays error messages
    from the API when file upload fails.
    """
    with requests_mock.Mocker() as m:
        m.post(f"{BASE_URL}/files/upload", 
               json={"detail": "File format not supported"}, 
               status_code=400)
        
        with mock.patch('builtins.input', side_effect=["1", "invalid.txt"]):
            mock_file = mock.mock_open(read_data=b"invalid data")
            
            original_stdout = sys.stdout
            sys.stdout = io.StringIO()
            
            with mock.patch('builtins.open', mock_file):
                upload()
            
            output = sys.stdout.getvalue()
            sys.stdout = original_stdout
            
            assert "File format not supported" in output


def test_get_users():
    """
    Tests the get_users function from the client module.
    
    This test mocks HTTP requests to verify that the get_users function
    works correctly and displays the list of users.
    """
    with requests_mock.Mocker() as m:
        users_data = [
            {"id": "1", "username": "user1"},
            {"id": "2", "username": "user2"}
        ]
        m.get(f"{BASE_URL}/users", json=users_data, status_code=200)
        
        original_stdout = sys.stdout
        sys.stdout = io.StringIO()
        
        get_users()
        
        output = sys.stdout.getvalue()
        sys.stdout = original_stdout
        
        assert "user1" in output
        assert "user2" in output


def test_get_users_error():
    """
    Tests the get_users function with an error response from the API.
    
    This test verifies that the client properly handles and displays error messages
    when retrieving the list of users fails.
    """
    with requests_mock.Mocker() as m:
        m.get(f"{BASE_URL}/users", 
              json={"detail": "Server error"}, 
              status_code=500)
        
        original_stdout = sys.stdout
        sys.stdout = io.StringIO()
        
        get_users()
        
        output = sys.stdout.getvalue()
        sys.stdout = original_stdout
        
        assert "Server error" in output


def test_get_user_data():
    """
    Tests the get_user_data function from the client module.
    
    This test mocks user input and HTTP requests to verify that the get_user_data function
    works correctly and displays the user's data.
    """
    with requests_mock.Mocker() as m:
        user_data = [
            {"id": "1", "content": "id,name\n1,Test1"},
            {"id": "2", "content": "id,name\n2,Test2"}
        ]
        m.get(f"{BASE_URL}/users/2/data", json=user_data, status_code=200)
        
        with mock.patch('builtins.input', return_value="2"):
            original_stdout = sys.stdout
            sys.stdout = io.StringIO()
            
            get_user_data()
            
            output = sys.stdout.getvalue()
            sys.stdout = original_stdout
            
            assert "Test1" in output
            assert "Test2" in output


def test_get_user_data_error():
    """
    Tests the get_user_data function with an error response from the API.
    
    This test verifies that the client properly handles and displays error messages
    when retrieving a user's data fails.
    """
    with requests_mock.Mocker() as m:
        m.get(f"{BASE_URL}/users/999/data", 
              json={"detail": "User not found"}, 
              status_code=404)
        
        with mock.patch('builtins.input', return_value="999"):
            original_stdout = sys.stdout
            sys.stdout = io.StringIO()
            
            get_user_data()
            
            output = sys.stdout.getvalue()
            sys.stdout = original_stdout
            
            assert "User not found" in output