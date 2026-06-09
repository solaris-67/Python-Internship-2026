from flask import Flask
from src.config import Config
from src.ext import db, migrate, login_manager, admin
from src.admin_views.views import AdminModelView, MyAdminIndexView
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

    admin.init_app(app, index_view=MyAdminIndexView())
    admin.add_view(AdminModelView(Photo, db.session, name='Photos', endpoint='admin_photo'))
    admin.add_view(AdminModelView(Category, db.session, name='Categories', endpoint='admin_category'))
    admin.add_view(AdminModelView(User, db.session, name='Users', endpoint='admin_user'))

    register_blueprint(app)
    return app


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


def register_blueprint(app):
    for blueprint in blueprints:
        app.register_blueprint(blueprint)