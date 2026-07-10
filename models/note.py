from . import db

class Note(db.Model):

    __tablename__="notes"

    id=db.Column(db.Integer,primary_key=True)

    title=db.Column(db.String(100))

    content=db.Column(db.Text)

    user_id=db.Column(db.Integer,db.ForeignKey("users.id"))

    user=db.relationship("User",back_populates="notes")