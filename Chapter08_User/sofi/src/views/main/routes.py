from flask import render_template, Blueprint
from src.models.photo import Photo

main_bp = Blueprint('main', __name__)

# @main_bp.route('/')
# def index():
#     photos = Photo.query.all()
#     return render_template("main/index.html", title="Gallery", photos=photos)

@main_bp.route('/')
def index():
    photos = Photo.query.all()
    print("Number of photos:", len(photos))
    for p in photos:
        print(p.id, p.title, p.img)
    return render_template("main/index.html", title="Gallery", photos=photos)