"""
2. CLIENT-SERVER ARCHITECTURE
==============================

Client-server architecture is a model in which two systems
communicate with each other over a network.


CLIENT
------

The client is an application that sends requests to a server.

Examples:
    - Web browsers
    - Flutter applications
    - React applications
    - Mobile applications


SERVER
------

The server receives requests, processes them and sends
responses back to the client.

Examples:
    - FastAPI application
    - Django application
    - Node.js application


DATABASE
--------

A database is used to store and manage application data.

Examples:
    - MySQL
    - PostgreSQL
    - MongoDB


ARCHITECTURE
------------

        Flutter / React
             (Client)
                |
                |
          HTTP Request
                |
                v
        FastAPI Application
          (Backend / API)
                |
                |
          Database Query
                |
                v
        MySQL / PostgreSQL
            (Database)
                |
                |
          Database Result
                |
                v
        FastAPI Application
                |
                |
         HTTP Response
              (JSON)
                |
                v
        Flutter / React
             (Client)


IMPORTANT POINTS
----------------

1. The client communicates with the backend through HTTP requests.

2. The backend processes the request and communicates with
   the database when necessary.

3. The database stores and retrieves application data.

4. The backend sends the response to the client, commonly
   in JSON format.

5. The client displays the received information to the user.


KEY TAKEAWAY
------------

The client normally communicates with the backend API,
while the backend communicates with the database.

The client does not need to know how the backend internally
processes requests or manages database operations.

"""