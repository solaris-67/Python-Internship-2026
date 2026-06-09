from flask import render_template, url_for, redirect, Blueprint
from os import path
from flask_login import login_required

from src.ext import db
from src.config import Config
from src.models.photo import Photo, Category
from src.views.photo.forms import PhotoForm


photo_bp = Blueprint('photo', __name__)

@photo_bp.route('/photos')
def photos():
    photos = Photo.query.all()
    return render_template('photo/photos.html', photos=photos)


@photo_bp.route('/photos/<int:id>')
def photo(id):
    p = Photo.query.get_or_404(id)
    return render_template("photo/photo.html", photo=p)


@photo_bp.route('/delete/<int:id>')
@login_required
def delete(id):
    photo = Photo.query.get_or_404(id)
    db.session.delete(photo)
    db.session.commit()
    return redirect(url_for('photo.photos'))

@photo_bp.route('/submit', methods=['GET', 'POST'])
@login_required
def submit():
    form = PhotoForm()
    form.category.choices = [(c.id, c.title) for c in Category.query.all()]

    if form.validate_on_submit():
        img = form.img.data
        img.save(path.join(Config.UPLOAD_PATH, img.filename))
        new_photo = Photo(
            title=form.title.data,
            artist=form.artist.data,
            img=path.join('static', 'uploads', img.filename),
            category_id=form.category.data
        )
        photo.create()
        return redirect(url_for('photos'))
    else:
        print(form.errors)
    return render_template("photo/submit.html", form=form)


@photo_bp.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    photo = Photo.query.get_or_404(id)
    form = PhotoForm()

    if form.validate_on_submit():
        img = form.img.data
        img.save(path.join(Config.UPLOAD_PATH, img.filename))
        photo.title = form.title.data
        photo.artist = form.artist.data
        photo.img = path.join('static', 'uploads', img.filename)
        photo.save()
        return redirect(url_for('photos'))
    else:
        print(form.errors)

    return render_template("photo/submit.html", form=form)

@photo_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        print(form.name.data)
        print(form.password.data)
        print(form.password2.data)
        print(form.countries.data)
        print(form.remember_me.data)
    else:
        print(form.errors)

    return render_template("auth/register.html", form=form)

