from flask import Blueprint, render_template, request, redirect, url_for, current_app
from flask_login import login_required
from model import Setting, Article, Category, db, Comment
from home.form import CommentForm 

homeView = Blueprint('homeView',__name__,static_folder='templates')

@homeView.route('/', defaults={'page': 1})
@homeView.route('/<page>')
def index(page=1):
	blog = Setting.query.first()
	pagination = Article.query.order_by(db.desc('add_time')).paginate(int(page),10,True)
	articles = pagination.items
	categories = Category.query.all()
	return render_template('index.html', blog=blog, articles=articles, pagination=pagination, categories=categories)

@homeView.route('/article/<category_name>/<page>')
def article_category(category_name,page):
	category_id = Category.query.filter_by(name=category_name).first().id
	pagination = Article.query.filter_by(category_id=category_id).order_by(db.desc('add_time')).paginate(int(page),10,True)
	articles = pagination.items
	categories = Category.query.all()
	return render_template('categoryArticles.html', articles=articles, pagination=pagination, categories=categories, category_name=category_name)


@homeView.route('/article/<article_id>')
def article_detail(article_id):
	form = CommentForm()
	blogName = current_app.config.get('BLOG_NAME')
	comments = Comment.query.filter_by(article_id=article_id).order_by(db.desc('add_time')).all() 
	article = Article.query.filter_by(id=article_id).first_or_404()
	return render_template('article.html', article=article, comments=comments,blogName=blogName, form=form)

@homeView.route('/article/comment/<article_id>', methods=['POST'])
def article_comment(article_id):
	form = CommentForm()
	if form.validate_on_submit():
		print(article_id)
		try:
			comment = Comment(writer=request.form['writer'], writer_email=request.form['writer_email'],content=request.form['content'],article_id=article_id)
			db.session.add(comment)
			db.session.commit()
		except Exception as e:
			print(str(e))
			
	return redirect(url_for('homeView.article_detail', article_id=article_id))
 