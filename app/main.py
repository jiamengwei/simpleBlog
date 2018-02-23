from __init__ import create_app, login_manager
from flask import Flask, render_template, Response, request, current_app, Blueprint
from admin.view import adminView
from article.view import adminArticleView
from category.view import adminCategoryView
from comment.view import adminCommentView
from home.view import homeView
from model import User, Setting, Article, Category, db

@login_manager.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()

app = create_app()
app.register_blueprint(homeView)
app.register_blueprint(adminView)
app.register_blueprint(adminArticleView, url_prefix='/wp-admin/article')
app.register_blueprint(adminCategoryView, url_prefix='/wp-admin/category')
app.register_blueprint(adminCommentView, url_prefix='/wp-admin/comment')

@app.route('/images/user/<imageName>')
def image_upload(imageName):
	image = open(app.config.get('UPLOAD_FOLDER')+imageName,'rb').read()
	resp = Response(image, mimetype="image/jpeg")
	return resp

if __name__ == '__main__':
	app.run()