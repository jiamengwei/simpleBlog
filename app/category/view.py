from flask import Blueprint,render_template, request, redirect, flash, url_for
from flask_login import login_required
from app.category.form import CategoryForm
from model import db, Category

adminCategoryView = Blueprint('adminCategoryView', __name__, static_folder='templates')

@adminCategoryView.route('/')
@login_required
def category():
    categories = Category.query.all()
    return render_template('adminCategory.html', categories=categories)  

@adminCategoryView.route('/add', methods=['POST', 'GET'])
@login_required
def category_add():
    form = CategoryForm()
    if form.validate_on_submit():
        category = Category()
        category.name = form.name.data
        category.description = form.description.data
        db.session.add(category)
        db.session.commit()
        return 'add success'
    return render_template('editCategory.html', form = form)

@adminCategoryView.route('/change')
@login_required
def category_change():
    return 'category category_change'

@adminCategoryView.route('/delete/<int:id>')
@login_required
def category_delete(id):
    if id == 1:
        flash('Warning:无法删除默认分类','alert-warning')
        return redirect(url_for('adminCategoryView.category'))
    try:
        category = Category.query.filter_by(id=id).first_or_404()
        db.session.delete(category)
        db.session.commit()
        flash('删除成功','alert-success')
    except Exception as e:
        flash(str(e))
    return redirect(url_for('adminCategoryView.category'))


@adminCategoryView.route('/select')
@login_required
def category_select():
    return 'category select'