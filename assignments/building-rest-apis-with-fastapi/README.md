# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a simple REST API with FastAPI by creating endpoints, handling request data, and returning JSON responses for a small application.

## 📝 Tasks

### 🛠️ Create a Basic API

#### Description
Build a FastAPI application that exposes a welcome endpoint and a list of items for a simple API.

#### Requirements
Completed program should:

- Create a FastAPI app instance
- Add a `GET /` endpoint that returns a welcome message
- Add a `GET /items` endpoint that returns a list of sample items in JSON format
- Run the app locally and confirm the responses in the browser or API docs

### 🛠️ Add Item Creation and Retrieval

#### Description
Extend the API so clients can create new items and fetch a single item by its ID.

#### Requirements
Completed program should:

- Define a data model for an item using Python classes or Pydantic
- Add a `POST /items` endpoint that accepts item data and returns the created item
- Add a `GET /items/{item_id}` endpoint to return one item by ID
- Return clear JSON payloads and use appropriate status codes

### 🛠️ Validate Input and Document the API

#### Description
Improve the API by validating incoming data and making the project easier to understand through FastAPI’s built-in documentation.

#### Requirements
Completed program should:

- Use Pydantic models to validate item fields such as name and price
- Reject invalid input with helpful validation errors
- Add at least one endpoint that updates or deletes an item
- Confirm that the API docs are available at `/docs` when the app is running

