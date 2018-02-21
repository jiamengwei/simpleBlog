from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_required
from model import db, Comment

adminCommentView = Blueprint('adminCommentView', __name__, static_folder='templates')

@adminCommentView.route('/')
@login_required
def comment():
    comments = Comment.query.all()
    return render_template('adminComment.html',comments=comments)

@adminCommentView.route('/delete/<id>')
@login_required
def comment_delete(id):
	comment = Comment.query.filter_by(id=id).first_or_404()
	db.session.delete(comment)
	try:
		db.session.commit()
		flash('删除成功', 'alert-success')
	except Exception as e:
		flash('error :'+str(e))
	return redirect(url_for('adminCommentView.comment'))

@adminCommentView.route('/setting')
@login_required
def comment_setting():
    return 'comment setting'

