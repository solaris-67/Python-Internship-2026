from flask import Flask
from src.config import Config
from src.ext import db, migrate, login_manager
from src.models.photo import Photo, Category
from src.models.user import User

from src.views.main.routes import main_bp
from src.views.auth.routes import auth_bp
from src.views.photo.routes import photo_bp
import os

blueprints = [main_bp, auth_bp, photo_bp]


def create_app():
    app = Flask(__name__,
                template_folder=os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates')),
                static_folder=os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'static')))

    print("Template folder:", app.template_folder)
    print("Static folder:", app.static_folder)

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    register_blueprint(app)
    return app


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


def register_blueprint(app):
    for blueprint in blueprints:
        app.register_blueprint(blueprint)