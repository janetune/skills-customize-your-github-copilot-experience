# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a simple REST API using FastAPI. Students will create endpoints, model request data, and return JSON responses while practicing clean Python API design.

## 📝 Tasks

### 🛠️ Create a FastAPI App

#### Description
Set up a small FastAPI application and add a basic root endpoint that responds with a welcome message.

#### Requirements
Completed program should:

- Import and initialize `FastAPI`
- Create an app instance named `app`
- Add a `GET /` endpoint that returns a JSON message
- Explain how to run the app locally with Uvicorn


### 🛠️ Build CRUD-style Endpoints

#### Description
Create endpoints that let a user view and add items in an in-memory list.

#### Requirements
Completed program should:

- Store a small list of sample records in memory
- Add a `GET /items` endpoint to return all items
- Add a `GET /items/{item_id}` endpoint to return one item
- Add a `POST /items` endpoint to create a new item
- Return JSON data with clear field names and values


### 🛠️ Validate Input and Improve Responses

#### Description
Use Pydantic models to validate incoming data and improve the clarity of the API.

#### Requirements
Completed program should:

- Define a `BaseModel` for item data
- Require fields such as `name` and `description`
- Reject invalid request data with useful validation errors
- Add at least one example of a query parameter or path parameter
- Test the API using the built-in FastAPI docs at `/docs`
