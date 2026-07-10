from app import app
from models import db
from models.user import User
from models.note import Note
from faker import Faker

fake=Faker()

with app.app_context():

    db.drop_all()

    db.create_all()

    for i in range(5):

        user=User(username=fake.user_name())

        user.password="password"

        db.session.add(user)

        db.session.commit()

        for j in range(10):

            note=Note(
                title=fake.sentence(),
                content=fake.text(),
                user_id=user.id
            )

            db.session.add(note)

    db.session.commit()

    print("Database seeded")