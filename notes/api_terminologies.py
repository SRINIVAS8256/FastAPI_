"""
3. IMPORTANT API TERMINOLOGIES
================================


3.1 API
-------

API stands for Application Programming Interface.

An interface that allows different software applications
to communicate and exchange data.

Example:
    A Flutter application retrieves student information
    from a FastAPI backend.


3.2 ENDPOINT
------------

An endpoint is a specific URL through which a client
accesses a particular API operation.

Example:

    http://127.0.0.1:8000/students

This endpoint retrieves student information.


3.3 HTTP
--------

HTTP stands for Hypertext Transfer Protocol.

It is a communication protocol used by clients and servers
to exchange requests and responses over a network.

Example:
    A browser sends an HTTP GET request to retrieve
    student data.


3.4 HTTP REQUEST
----------------

A request is a message sent by a client to a server
asking it to perform a particular operation.

A request commonly contains:

    1. HTTP Method
    2. URL
    3. Headers
    4. Query Parameters
    5. Request Body (when applicable)

Example:

    GET /students

This requests the list of students from the server.


3.5 HTTP RESPONSE
-----------------

A response is the message returned by the server
after processing a client request.

A response commonly contains:

    1. Status Code
    2. Headers
    3. Response Body

Example:

    {
        "id": 1,
        "name": "Rahul",
        "age": 21
    }

The server returns this JSON data to the client.


3.6 HTTP METHODS
----------------

HTTP methods define what operation the client wants
the server to perform.

    GET:
        Retrieves data.
        Example: Get all students.

    POST:
        Creates new data.
        Example: Add a new student.

    PUT:
        Replaces an existing resource.
        Example: Update all student details.

    PATCH:
        Partially updates an existing resource.
        Example: Update only the student's age.

    DELETE:
        Deletes an existing resource.
        Example: Delete a student.

Example Endpoints:

    GET     /students       -> Get all students
    GET     /students/1     -> Get student with ID 1
    POST    /students       -> Create a student
    PUT     /students/1     -> Replace student details
    PATCH   /students/1     -> Partially update a student
    DELETE  /students/1     -> Delete a student


3.7 JSON
--------

JSON stands for JavaScript Object Notation.

It is a lightweight data-interchange format commonly
used by APIs to exchange information between clients
and servers.

Example:

    {
        "id": 1,
        "name": "Rahul",
        "age": 21,
        "course": "Computer Science"
    }

JSON supports the following data types:

    1. Strings
    2. Numbers
    3. Booleans (true / false)
    4. Arrays
    5. Objects
    6. Null values

Note:
    JSON uses true, false and null.
    Python uses True, False and None.


3.8 HTTP STATUS CODES
---------------------

HTTP status codes indicate the result of an HTTP request.

SUCCESSFUL RESPONSES:

    200 - OK
          Request completed successfully.

    201 - Created
          A new resource was successfully created.

    204 - No Content
          Request succeeded, but there is no response body.

CLIENT ERROR RESPONSES:

    400 - Bad Request
          The request contains invalid information.

    401 - Unauthorized
          Authentication is required or invalid.

    403 - Forbidden
          The client does not have permission to access
          the requested resource.

    404 - Not Found
          The requested resource does not exist.

    422 - Unprocessable Content
          The request data failed validation.

SERVER ERROR RESPONSES:

    500 - Internal Server Error
          An unexpected error occurred on the server.


3.9 HEADERS
-----------

Headers contain additional information about an HTTP
request or response.

They provide metadata about the communication.

Example:

    Content-Type: application/json

This indicates that the request or response body
contains JSON data.

Other examples:

    Authorization: Bearer <token>
    Accept: application/json


3.10 QUERY PARAMETERS
---------------------

Query parameters are optional values passed through
a URL to filter, sort or customize API results.

They appear after the question mark (?) in a URL.

Example:

    /students?course=CSE&age=21

Here:

    course = CSE
    age    = 21

The ampersand (&) separates multiple query parameters.

Another example:

    /students?limit=10&offset=0

This can be used to retrieve the first 10 students.


3.11 PATH PARAMETERS
--------------------

Path parameters are values included directly in the
URL path to identify a particular resource.

Example:

    /students/10

Here:

    10 = Student ID

The server uses this ID to retrieve the specific student.

Another example:

    /students/25


3.12 REQUEST BODY
-----------------

The request body contains data sent by the client
to the server.

It is commonly used when creating or updating resources.

Example:

    {
        "name": "Srinivas",
        "age": 22,
        "course": "CSE"
    }

For example, when a client sends a POST request to
/students, the student information can be included
in the request body.

FastAPI commonly uses Pydantic models to validate
and process request body data.


3.13 API DOCUMENTATION
---------------------

API documentation explains the available endpoints,
HTTP methods, request formats, parameters and responses.

FastAPI automatically generates interactive API
documentation using OpenAPI.

FastAPI provides two documentation interfaces:

    1. Swagger UI

       URL:
       http://127.0.0.1:8000/docs

       Allows developers to explore and test API
       endpoints directly from the browser.

    2. ReDoc

       URL:
       http://127.0.0.1:8000/redoc

       Provides a structured documentation interface
       for understanding API endpoints.


IMPORTANT TAKEAWAYS
===================

1. API allows different applications to communicate.

2. Endpoint represents a specific API URL.

3. HTTP is the communication protocol.

4. Request is sent by the client.

5. Response is returned by the server.

6. HTTP methods define the operation to perform.

7. JSON is a commonly used data-interchange format.

8. Status codes indicate the result of a request.

9. Headers provide additional request and response metadata.

10. Query parameters are used to filter or customize results.

11. Path parameters identify specific resources.

12. Request body carries data from the client to the server.

13. FastAPI automatically generates API documentation.

"""
