Name : Ayesha Waseem
Roll num : 00477764
Date : 7-05-2025
Slot: 9-12 Friday
 
 FastAPI Assignment – Path, Query, and Body Parameters
🔍 Overview
This project is built using FastAPI and demonstrates how to work with path parameters, query parameters, and request body validation using Pydantic models.
The application provides basic CRUD-like functionality for working with item data.


🚀 Technologies Used
Python 3.10+
FastAPI
Pydantic
Uvicorn (for running the development server)


📁 Project Structure
main.py – The main FastAPI application file
README.md – Documentation of the project



✅ API Endpoints Description
1. GET /items/{item_id}
This endpoint is used to fetch an item using a required path parameter called item_id. Validation ensures the ID must be an
integer and greater than or equal to 1.

2. GET /items/
This endpoint is used for searching and paginating items using optional query parameters:
q: a string used for search (optional, must be between 3 and 50 characters)
skip: number of records to skip (default is 0)
limit: number of records to return (default is 10, max 100)

3. PUT /items/validated/{item_id}
This endpoint updates an item by ID. It accepts:
a path parameter item_id (required)
a query parameter q (optional, minimum 3 characters)
a request body (optional), which should be a JSON object including fields like name, description, and price



📘 What I Learned
How to declare and validate Path parameters
How to work with Query parameters for filtering and pagination
How to use Body models with validation using Pydantic
How to build clean and well-structured FastAPI routes
