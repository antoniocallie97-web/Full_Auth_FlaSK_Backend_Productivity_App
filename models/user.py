from . import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):

    __tablename__="users"

    id=db.Column(db.Integer,primary_key=True)

    username=db.Column(db.String(80),unique=True)

    password_hash=db.Column(db.String(255))

    notes=db.relationship("Note",back_populates="user",cascade="all, delete")

    @property
    def password(self):
        raise AttributeError

    @password.setter
    def password(self,password):
        self.password_hash=generate_password_hash(password)

    def authenticate(self,password):
        return check_password_hash(self.password_hash,password)