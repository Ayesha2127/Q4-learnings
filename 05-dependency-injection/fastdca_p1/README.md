Name : Ayesha Waseem

Roll num : 00477764

Date : 7-05-2025

Slot: 9-12 Friday

🔗 FastAPI Assignment – Dependency Injection & Custom Logic
📌 Overview
This FastAPI project demonstrates how to use dependency injection for building reusable, secure, and modular routes. 
It covers various scenarios such as injecting simple dependencies, dependencies with parameters, 
authentication logic via query parameters, multiple dependencies, and custom logic using callable classes for dynamic object retrieval.


🚀 Technologies Used
Python 3.10+
FastAPI
Uvicorn (ASGI server)


🧩 Features Implemented
1. Simple Dependency
A reusable function returns a static message. This is injected using FastAPI's Depends system and demonstrates
 how to use dependencies without requiring input from the user.

2. Dependency with Parameters
A dependency function takes a parameter (username) and returns a response using that parameter.
This shows how to create dynamic responses based on function arguments.

3. Dependency with Query Parameters
A login-like functionality is implemented using query parameters (username and password). If both are "admin",
 the login is successful; otherwise, it fails. This is a basic simulation of authentication using dependencies.

4. Multiple Dependencies
Two dependency functions are used together. Each function takes a number, modifies it, and returns the result.
 These results are then used in the main route logic to calculate a total. This demonstrates the use of multiple dependencies in one route.

5. Custom Dependency Class (GetObjectOr404)
A class-based dependency is implemented to simulate database-like object retrieval:


It accepts a dictionary (blogs or users) as a model.
When a request is made to get a blog or user by ID, the class checks if the ID exists.
If not, it raises a 404 error.
This mimics the behavior of get_object_or_404 in Django.



📁 Project Structure
main.py: Contains the FastAPI application and all route logic
README.md: Project documentation


📘 What I Learned
How to implement dependency injection using Depends
How to create parameterized and dynamic dependencies
How to use query parameters in dependencies for login logic
How to handle multiple dependencies in a single route
How to build a custom callable class to mimic object lookup and raise HTTP exceptions
