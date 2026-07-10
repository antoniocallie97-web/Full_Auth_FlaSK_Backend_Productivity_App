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

api.add_resource(Register, "/register")
api.add_resource(Login, "/login")

api.add_resource(NoteListResource, "/notes")
api.add_resource(NoteResource, "/notes/<int:id>")

if __name__ == "__main__":
    app.run(debug=True)