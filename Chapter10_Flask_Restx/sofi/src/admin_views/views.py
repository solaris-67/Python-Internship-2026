from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView, expose
from flask_login import current_user, logout_user
from flask import redirect, url_for


class MyAdminIndexView(AdminIndexView):
    @expose('/')
    def index(self):
        if not current_user.is_authenticated:
            return redirect(url_for('auth.login'))
        return self.render('admin/index.html')

class AdminModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login'))