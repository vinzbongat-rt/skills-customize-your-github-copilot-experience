# 📘 Assignment: Mini Weather API

## 🎯 Objective

Build a small REST API that serves weather information for different cities using Python and FastAPI. Students will practice creating routes, returning JSON responses, and handling simple data validation.

## 📝 Tasks

### 🛠️ Create the API Endpoints

#### Description
Set up a FastAPI app with a root endpoint and a city weather endpoint that returns weather information in JSON.

#### Requirements
Completed program should:

- Create a FastAPI app instance
- Add a `GET /` endpoint that returns a welcome message
- Add a `GET /weather/{city}` endpoint that returns weather data for a city
- Return data as JSON, such as city name, temperature, and condition

### 🛠️ Add Weather Data Storage

#### Description
Use a small in-memory list or dictionary to store sample weather records for several cities.

#### Requirements
Completed program should:

- Store at least three cities with sample temperature and condition values
- Return the matching city data when a valid city name is requested
- Return a friendly error message when the requested city is not found

### 🛠️ Validate Input and Improve the API

#### Description
Improve the user experience by validating request data and making the API easier to interact with.

#### Requirements
Completed program should:

- Accept only valid city names or requested values in a clear format
- Add at least one `POST /weather` endpoint that allows creating a new weather record
- Return helpful JSON responses for both success and error cases
- Confirm the API documentation loads correctly at `/docs`
