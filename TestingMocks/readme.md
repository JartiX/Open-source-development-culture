# TestingMocks - CSV API Testing Project

## Project Overview

TestingMocks is a project that demonstrates how to implement and test a FastAPI-based API for CSV file processing. It consists of:

1. **Server Application**: A FastAPI application that provides endpoints for user registration, CSV file uploads, and data retrieval
2. **Client CLI**: A command-line interface for interacting with the API
3. **Test Suite**: Comprehensive tests for both the server and client components

The project illustrates how to test different components of a web application independently while ensuring that all parts work correctly together.

## 🏗️ Project Structure

```
TestingMocks/
├── app/                        # Server-side code
│   ├── database.py             # Database configuration
│   ├── main.py                 # FastAPI application entry point
│   ├── models.py               # SQLAlchemy ORM models
│   ├── parse_csv.py            # CSV parsing utility
│   ├── schemas.py              # Pydantic models
│   └── routes/                 # API endpoints
│       ├── files.py            # File upload endpoints
│       └── users.py            # User management endpoints
├── cli/                        # Client-side code
│   └── client.py               # Command-line client
├── tests/                      # Automated tests
│   ├── test_client.py          # Client tests with mock HTTP responses
│   └── test_server.py          # Server tests with FastAPI TestClient
└── requirements.txt            # Project dependencies
```

## 🚀 Features

- **User Management**: Register users and retrieve user lists
- **File Processing**: Upload and parse CSV files
- **Data Retrieval**: Retrieve data associated with specific users
- **RESTful API**: Well-structured API with proper error handling
- **CLI Client**: User-friendly command-line interface

## 📋 Requirements

- Python 3.8+
- FastAPI
- SQLAlchemy
- Uvicorn
- Requests
- Pytest

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/JartiX/Open-source-development-culture.git
   cd "Open-source-development-culture/TestingMocks"
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On Unix or MacOS
   source venv/bin/activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🔧 Usage

### Starting the Server

Run the FastAPI server:

```bash
python -m app.main
```

The server will be available at `http://localhost:8000`

### Using the CLI Client

Run the command-line client:

```bash
python -m cli.client
```

The client provides a menu with options to:
1. Register a user
2. Upload a CSV file
3. Get a list of all users
4. Get data for a specific user
5. Exit

## 🧪 Testing

### Running Tests

Run all tests:

```bash
pytest
```

Run specific test files:

```bash
# Test only the client
pytest tests/test_client.py

# Test only the server
pytest tests/test_server.py
```

Run tests with verbose output:

```bash
pytest -v tests/
```

### Test Approach

This project demonstrates two different approaches to testing:

1. **Server Testing**: Uses FastAPI's `TestClient` to test API endpoints without starting a real HTTP server. The tests interact directly with the FastAPI application, making it easy to test routing, request handling, and database interactions.

2. **Client Testing**: Uses the `requests_mock` library to mock HTTP responses, allowing client code to be tested without a running server. This approach isolates the client code from the server and enables testing various scenarios, including error conditions.

### Key Testing Concepts Demonstrated

- **Mocking HTTP requests**: Using `requests_mock` to simulate server responses
- **Input/output capture**: Mocking user input and capturing console output
- **Database testing**: Working with a test database
- **API testing**: Testing RESTful endpoints
- **Test isolation**: Ensuring each test is independent
- **Error handling**: Testing both success and failure scenarios

## 🛠️ Architecture

### Server Components

- **FastAPI Application**: Provides the API endpoints and handles HTTP requests
- **SQLAlchemy ORM**: Manages database interactions and object-relational mapping
- **Pydantic Models**: Validate request and response data
- **CSV Parser**: Processes and validates CSV files

### Client Components

- **Command-line Interface**: Provides a user-friendly way to interact with the API
- **HTTP Client**: Uses the `requests` library to communicate with the server

## 📝 Development Guidelines

- **Server changes**: When adding new endpoints or modifying existing ones, update both the server implementation and the corresponding tests
- **Client changes**: When modifying the client, ensure that the tests are updated to reflect the changes
- **Database schema changes**: Update both the models and the test fixtures

## 📚 Learning Resources

This project serves as a practical demonstration of testing techniques. Here are some resources to learn more:

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pytest Documentation](https://docs.pytest.org/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Requests Mock Documentation](https://requests-mock.readthedocs.io/)