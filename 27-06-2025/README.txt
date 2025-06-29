# User Management REST API with Flask

## Overview

This project is a Flask-based REST API for managing user data with a web interface. It provides both API endpoints and HTML pages to perform CRUD (Create, Read, Update, Delete) operations on user records.

 Features

- REST API Endpoints:
  - GET `/api/users` - Retrieve all users
  - GET `/api/users/<id>` - Retrieve a specific user
  - POST `/api/users` - Create a new user
  - PUT `/api/users/<id>` - Update an existing user
  - DELETE `/api/users/<id>` - Delete a user

- web Interface:
  - View all users in a responsive table
  - Add new users through a form
  - Edit existing user information
  - Delete users with confirmation

- Styling:
  - Clean, modern interface with CSS styling
  - Color-coded buttons for different actions
  - Hover effects for better user experience
  - Responsive design

## Installation

1. Clone the repository:
   
   git clone https://github.com/yourusername/flask-user-management-api.git
   cd flask-user-management-api
 

2. Create and activate a virtual environment (recommended):
   
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`


3. Install the required dependencies:
   
   pip install flask
  

## Running the Application

1. Start the Flask development server:
   
   python api.py
   

2. Access the application in your browser:
 
   http://localhost:5000
  
 Project Structure


flask-user-management-api/
├── api.py                # Main Flask application
├── static/
│   └── style.css         # CSS stylesheet
├── templates/
│   ├── index.html        # Main page with user list
│   ├── add_user.html     # Form to add new users
│   └── edit_user.html    # Form to edit existing users
└── README.md             # This file


API Documentation

 Get All Users

GET /api/users

Response:
json
[
    {
        "id": 1,
        "name": "John Doe",
        "email": "john@example.com"
    },
    {
        "id": 2,
        "name": "Jane Smith",
        "email": "jane@example.com"
    }
]
 Get Single User

GET /api/users/<id>

*Response (Success):

{
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com"
}
Response (Error):

{
    "error": "User not found"
}
 Create User

POST /api/users

Request Body:

{
    "name": "New User",
    "email": "new@example.com"
}

Response:

{
    "id": 3,
    "name": "New User",
    "email": "new@example.com"
}
Update User

PUT /api/users/<id>
Request Body:

{
    "name": "Updated Name",
    "email": "updated@example.com"
}

Response:

{
    "id": 1,
    "name": "Updated Name",
    "email": "updated@example.com"
}


Delete User

DELETE /api/users/<id>

Response:

{
    "message": "User deleted successfully"
}

Technologies Used:
- Python 3
- Flask
- HTML5
- CSS3


