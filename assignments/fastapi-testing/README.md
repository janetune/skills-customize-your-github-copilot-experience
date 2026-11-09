# 📘 Assignment: Automated Testing for FastAPI

## 🎯 Objective

Learn how to verify a FastAPI application with `pytest` and FastAPI's `TestClient`. Students will test successful requests, input validation, and error responses without manually starting a server.

## 📝 Tasks

### 🛠️ Set Up API Tests

#### Description
Use the provided task API and test starter file to make requests directly to the application in your tests.

#### Requirements
Completed program should:

- Install the required packages: `fastapi`, `httpx`, and `pytest`
- Import the app and create a `TestClient`
- Run the test suite with `pytest`
- Write a test that checks the root endpoint's status code and response


### 🛠️ Test Successful Requests

#### Description
Add tests that confirm the API returns the expected data when requests succeed.

#### Requirements
Completed program should:

- Test that `GET /items` returns a list of items
- Test that `GET /items/{item_id}` returns the requested item
- Test that `POST /items` creates an item and returns its data
- Check relevant status codes and response fields


### 🛠️ Test Errors and Validation

#### Description
Check how the API responds to requests for missing items and invalid input.

#### Requirements
Completed program should:

- Test that requesting an unknown item returns `404`
- Test that a request with missing or invalid fields returns `422`
- Check that error responses contain useful details
- Reset the in-memory sample data between tests so tests do not depend on execution order
