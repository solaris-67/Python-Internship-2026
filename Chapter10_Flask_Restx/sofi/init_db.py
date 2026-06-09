from app import app
from src.ext import db
from src.models.photo import Photo, Category
from src.models.user import User

with app.app_context():
    db.drop_all()
    db.create_all()

    category1 = Category(title='Street Art')
    category2 = Category(title='Street Detail')
    category3 = Category(title='Street Architecture')
    db.session.add_all([category1, category2, category3])
    db.session.commit()

    photo1 = Photo(title="Hand mosaic", artist="Unknown", img="uploads/a2.png", category_id=category1.id)
    photo2 = Photo(title="Street Number Plate", artist="Unknown", img="uploads/a3.png", category_id=category2.id)
    photo3 = Photo(title="Flower Sculpture Relief", artist="Unknown", img="uploads/a4.png", category_id=category3.id)
    photo4 = Photo(title="Park Bench Decoration", artist="Unknown", img="uploads/a5.png", category_id=category1.id)
    photo5 = Photo(title="Wall Decoration", artist="Lironism", img="uploads/a6.png", category_id=category2.id)
    photo6 = Photo(title="Cat Paw Print", artist="Some random cat", img="uploads/a7.png", category_id=category3.id)

    db.session.add_all([photo1, photo2, photo3, photo4, photo5, photo6])
    db.session.commit()

    print("Database seeded successfully!")