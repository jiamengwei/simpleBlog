from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user, login_required
from admin.form import LoginForm, RegisterForm
from model import db, User
from app import login_manager

adminView = Blueprint('adminView', __name__,
                        template_folder='templates')

@adminView.route('/wp-admin/')
def admin():
    if not current_user.is_authenticated:
        return redirect(url_for('adminView.login'))
    return render_template('admin.html')

@adminView.route('/logon', methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    error = None
    if form.validate_on_submit():
        print('submit')
        if User.query.filter_by(email=form.email.data).count()>0:
            error = '邮箱已存在'
            return render_template('register.html',form=form, error=error)
        try:
            user = User(name=form.name.data, email=form.email.data,password=form.password.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('adminView.login'))
        except Exception as e:
            print(e)
            error = '注册失败'
    return render_template('register.html', form=form, error=error)

@adminView.route('/login', methods=['POST','GET'])
def login():
    form = LoginForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.name.data, password=form.password.data).first()
        if user:
            login_user(user)
            return redirect(url_for('adminView.admin'))
    return render_template('login.html', form = form)


@adminView.route('/logout/')
@login_required
def logout():
    logout_user()
    form = LoginForm()
    return redirect(url_for('adminView.login'))