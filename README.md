# Full Auth Flask Backend – Productivity App

## Overview

This project is a secure RESTful API built with Flask for a Productivity App. It implements user authentication, user-owned resources, CRUD operations, pagination, and database management using SQLAlchemy and Flask-Migrate.

The application allows users to register, log in, and manage their own notes. Each user can only access, update, and delete their own records.

---

## Features

* User Registration
* User Login
* Password Hashing using Werkzeug
* Session-Based Authentication
* User-Owned Notes Resource
* Full CRUD Operations
* Pagination Support
* SQLite Database
* Flask-Migrate Database Migrations
* Database Seeding with Faker
* RESTful API Design
* Secure Authorization (Users can only access their own notes)

---

## Technologies Used

* Python 3.8+
* Flask 2.2.2
* Flask-RESTful
* Flask-SQLAlchemy
* Flask-Migrate
* Marshmallow
* Werkzeug
* Faker
* SQLite
* Pipenv

---

## Project Structure

```
Full_Auth_FlaSK_Backend_Productivity_App/

│── app.py
│── config.py
│── seed.py
│── Pipfile
│── README.md
│── .gitignore
│
├── models/
│   ├── __init__.py
│   ├── user.py
│   └── note.py
│
├── resources/
│   ├── auth.py
│   └── notes.py
│
├── schemas/
│   ├── __init__.py
│   ├── user_schema.py
│   └── note_schema.py
│
├── migrations/
│
└── instance/
    └── app.db
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/your-username/Full_Auth_FlaSK_Backend_Productivity_App.git

cd Full_Auth_FlaSK_Backend_Productivity_App
```

---

### Install dependencies

```bash
pipenv install
```

Activate the virtual environment:

```bash
pipenv shell
```

---

## Database Setup

Initialize migrations:

```bash
flask db init
```

Create a migration:

```bash
flask db migrate -m "Initial migration"
```

Apply the migration:

```bash
flask db upgrade
```

---

## Seed the Database

Populate the database with sample users and notes:

```bash
python seed.py
```

---

## Run the Application

```bash
python app.py
```

The API will be available at:

```
http://127.0.0.1:5000
```

---

## Authentication

This application uses **session-based authentication**.

A user must:

1. Register an account.
2. Log in.
3. Access protected endpoints.

Passwords are securely hashed using Werkzeug before being stored in the database.

---

## API Endpoints

### Home

| Method | Endpoint | Description |
| ------ | -------- | ----------- |
| GET    | `/`      | API status  |

### Authentication

| Method | Endpoint    | Description         |
| ------ | ----------- | ------------------- |
| POST   | `/register` | Register a new user |
| POST   | `/login`    | Login a user        |

### Notes

| Method | Endpoint      | Description                               |
| ------ | ------------- | ----------------------------------------- |
| GET    | `/notes`      | Retrieve all notes for the logged-in user |
| POST   | `/notes`      | Create a new note                         |
| GET    | `/notes/<id>` | Retrieve a specific note                  |
| PATCH  | `/notes/<id>` | Update a note                             |
| DELETE | `/notes/<id>` | Delete a note                             |

---

## Pagination

The notes endpoint supports pagination.

Example:

```
GET /notes?page=1&per_page=5
```

Response includes:

* Current page
* Total pages
* Total records
* Notes for the requested page

---

## Security

The application ensures that:

* Passwords are hashed before storage.
* Users must authenticate before accessing protected resources.
* Users can only access their own notes.
* Unauthorized access returns appropriate HTTP status codes.

---

## Example JSON Request

### Register

```json
{
    "username": "antony",
    "password": "password123"
}
```

### Login

```json
{
    "username": "antony",
    "password": "password123"
}
```

### Create Note

```json
{
    "title": "Study Flask",
    "content": "Complete the authentication lab."
}
```

---

## HTTP Status Codes

| Code | Meaning            |
| ---- | ------------------ |
| 200  | Success            |
| 201  | Resource Created   |
| 204  | Resource Deleted   |
| 400  | Bad Request        |
| 401  | Unauthorized       |
| 404  | Resource Not Found |

---

## Future Improvements

* JWT Authentication
* User Logout Endpoint
* Search and Filter Notes
* Note Categories
* File Attachments
* Unit and Integration Tests
* Docker Deployment
* PostgreSQL Support

---

## Author

**Antony Mutai**

---

## License

This project was developed for educational purposes as part of the **Full Auth Flask Backend – Productivity App** summative lab.
