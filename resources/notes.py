from flask import request, session
from flask_restful import Resource
from models import db
from models.note import Note
from schemas.note_schema import NoteSchema

schema=NoteSchema()
many_schema=NoteSchema(many=True)

class NoteListResource(Resource):

    def get(self):

        if "user_id" not in session:
            return {"error":"Unauthorized"},401

        page=request.args.get("page",1,type=int)

        per_page=request.args.get("per_page",5,type=int)

        pagination=Note.query.filter_by(user_id=session["user_id"]).paginate(page=page,per_page=per_page,error_out=False)

        return {
            "notes":many_schema.dump(pagination.items),
            "page":page,
            "pages":pagination.pages,
            "total":pagination.total
        }

    def post(self):

        if "user_id" not in session:
            return {"error":"Unauthorized"},401

        data=request.get_json()

        note=Note(
            title=data["title"],
            content=data["content"],
            user_id=session["user_id"]
        )

        db.session.add(note)

        db.session.commit()

        return schema.dump(note),201


class NoteResource(Resource):

    def get(self,id):

        note=Note.query.filter_by(id=id,user_id=session.get("user_id")).first()

        if not note:
            return {"error":"Not found"},404

        return schema.dump(note)

    def patch(self,id):

        note=Note.query.filter_by(id=id,user_id=session.get("user_id")).first()

        if not note:
            return {"error":"Not found"},404

        data=request.get_json()

        note.title=data.get("title",note.title)

        note.content=data.get("content",note.content)

        db.session.commit()

        return schema.dump(note)

    def delete(self,id):

        note=Note.query.filter_by(id=id,user_id=session.get("user_id")).first()

        if not note:
            return {"error":"Not found"},404

        db.session.delete(note)

        db.session.commit()

        return {},204