"""
FASTAPI – INTRODUCTION
======================

1. WHAT IS AN API?
------------------

API stands for Application Programming Interface.

An API is a mechanism that allows two different software
applications to communicate and exchange data.

An API acts as a bridge between a client and a server.


2. REAL-WORLD EXAMPLE: RESTAURANT
---------------------------------

Imagine visiting a restaurant:

Customer:
    Requests food.

Waiter:
    Takes the order and communicates with the kitchen.

Kitchen:
    Prepares the food and returns it.

Here:

    Customer = Client
    Waiter   = API
    Kitchen  = Server

Similarly, a frontend application communicates with a
backend application through APIs.


3. SOFTWARE EXAMPLE
-------------------

Consider a Student Management Application.

1. User clicks on "View Students".
2. Frontend sends an HTTP request to the backend API.
3. FastAPI receives the request.
4. FastAPI retrieves student information from the database.
5. FastAPI returns the data in JSON format.
6. Frontend displays the student information.


4. IMPORTANT TAKEAWAY
---------------------

An API acts as an interface between different software
applications, allowing them to exchange information
without needing to know each other's internal implementation.

"""