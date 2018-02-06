from flask import Blueprint, render_template, abort, redirect, url_for, request
import sys
sys.path.append(".")
# from view import app
from __init__ import db
from model import User
from flask_admin import Admin, AdminIndexView, helpers, expose
from flask_login import logout_user, login_user, login_required, current_user
from .form import LoginForm, RegistrationForm
from werkzeug.security import generate_password_hash, check_password_hash

class MyAdminIndexView(AdminIndexView):

    @expose('/')
    def index(self):
        if not current_user.is_authenticated:
            return redirect(url_for('.login_view'))
        return super(MyAdminIndexView, self).index()
# 登录视图
    @expose('/login/', methods=('GET', 'POST'))
    def login_view(self):

        form = LoginForm(request.form)
        print(form.email.data)
        if helpers.validate_form_on_submit(form):
            print(LoginForm.validate_login(form)) 
            user = User()
            form.populate_obj(user)           
            if LoginForm.validate_email(user):
                login_user(user)
            return redirect(url_for('.login_view'))
        if current_user.is_authenticated:
            return redirect(url_for('.index'))
        
        link = '<p>Don\'t have an account? <a href="' + url_for('.register_view') + '">Click here to register.</a></p>'

        self._template_args['form'] = form
        self._template_args['link'] = link
        return super(MyAdminIndexView, self).index()
# 注册视图
    @expose('/register/', methods=('GET', 'POST'))
    def register_view(self):
        form = RegistrationForm(request.form)
        if helpers.validate_form_on_submit(form):
            user = User()
            form.populate_obj(user)
            print(type(user))
            RegistrationForm.validate_email(user)
            user.password = generate_password_hash(form.password.data)

            db.session.add(user)
            db.session.commit()

            login_user(user)
            return redirect(url_for('.index'))
        link = '<p>Already have an account? <a href="' + url_for('.login_view') + '">Click here to log in.</a></p>'
        self._template_args['form'] = form
        self._template_args['link'] = link
        return super(MyAdminIndexView, self).index()
# 注销视图
    @expose('/logout/')
    def logout_view(self):
        logout_user()
        return redirect(url_for('.index'))