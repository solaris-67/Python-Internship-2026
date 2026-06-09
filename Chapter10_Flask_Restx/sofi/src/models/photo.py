from src.ext import db
from src.models.base import BaseModel

class Photo(BaseModel):
    __tablename__ = 'photos'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False, default="Unknown")
    artist = db.Column(db.String(64))
    img = db.Column(db.String())
    is_active = db.Column(db.Boolean())
    created = db.Column(db.DateTime())
    information = db.Column(db.Text())

    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))

    category = db.relationship("Category", back_populates = "photos")


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())

    photos = db.relationship("Photo", back_populates="category")

    def __repr__(self):
        return f"{self.title}"