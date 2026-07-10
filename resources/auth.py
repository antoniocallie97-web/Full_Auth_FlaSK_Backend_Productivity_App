from flask import request, session
from flask_restful import Resource
from models import db
from models.user import User

class Register(Resource):

    def post(self):

        data=request.get_json()

        user=User(username=data["username"])

        user.password=data["password"]

        db.session.add(user)

        db.session.commit()

        return {"message":"User created"},201


class Login(Resource):

    def post(self):

        data=request.get_json()

        user=User.query.filter_by(username=data["username"]).first()

        if user and user.authenticate(data["password"]):

            session["user_id"]=user.id

            return {"message":"Login successful"}

        return {"error":"Invalid credentials"},401