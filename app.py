from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate

from config import Config
from models import db
from resources.auth import Register, Login
from resources.notes import NoteListResource, NoteResource

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

migrate = Migrate(app, db)

api = Api(app)


# Home Route
@app.route("/")
def home():
    return {
        "message": "Welcome to the Productivity App API",
        "status": "running",
        "version": "1.0",
        "available_endpoints": {
            "Register": "POST /register",
            "Login": "POST /login",
            "Get Notes": "GET /notes?page=1&per_page=5",
            "Create Note": "POST /notes",
            "Get Single Note": "GET /notes/<id>",
            "Update Note": "PATCH /notes/<id>",
            "Delete Note": "DELETE /notes/<id>"
        }
    }, 200


# Authentication Routes
api.add_resource(Register, "/register")
api.add_resource(Login, "/login")

# Notes Routes
api.add_resource(NoteListResource, "/notes")
api.add_resource(NoteResource, "/notes/<int:id>")


if __name__ == "__main__":
    app.run(debug=True)