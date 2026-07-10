from marshmallow import Schema, fields

class NoteSchema(Schema):

    id=fields.Int(dump_only=True)

    title=fields.Str()

    content=fields.Str()

    user_id=fields.Int()