import sys, os
pathOfAppDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(pathOfAppDir)
from flask import render_template, request, url_for, redirect, flash, current_app
from model import db, Article
from flask import Blueprint
from flask_login import login_required
from article.form import ArticleForm
from model import db, Article, Category, Image
import json, time


adminArticleView = Blueprint('adminArticleView', __name__, template_folder='templates')

@adminArticleView.route('/<page>')
@login_required
def article_list(page):
    pagination = Article.query.order_by(db.desc('add_time')).paginate(int(page),20,True)
    articles = pagination.items
    return render_template('adminArticle.html', articles=articles, pagination=pagination)

@adminArticleView.route('/add/', methods=['GET','POST'])
@login_required
def article_add():
    categories = Category.query.all()
    if request.method == 'POST':
        writer = current_app.config.get('WRITER')
        article = Article(title=request.form['title'],content=request.form['content'],
                                writer=writer,category_id=request.form['category_id'])
        db.session.add(article)
        try:
            db.session.commit()
            flash('添加成功', 'alert-success')
        except Exception as e:
            db.session.rollback()
            flash('错误信息：'+str(e), 'alert-danger')

    return render_template('editArticle.html', categories=categories)

@adminArticleView.route('/add/upload', methods=['POST'])
@login_required
def article_imageUpload(): 
    files = request.files
    imageType=set(['png','jpg','jpeg'])
    imagesUrl = []
    errno = 1
    for f in files:
        file = request.files[f]
        upload_folder = current_app.config.get('UPLOAD_FOLDER')
        try:
            file.save(os.path.join(upload_folder, file.filename))
            fileUrl = upload_folder+file.filename
            image = Image(path=fileUrl)
            db.session.add(image)
            db.session.commit()
            imagesUrl.append(fileUrl)
            errno = 0
        except Exception as e:
            error = 1
    returnInfo = json.dumps({'errno':errno, 'imagesUrl':imagesUrl})
    return returnInfo

@adminArticleView.route('/change/<int:id>', methods=['POST','GET'])
@login_required
def article_change(id):
    categories = Category.query.all()
    article = Article.query.filter_by(id=id).first_or_404()
    if request.method == 'POST':
        writer = current_app.config.get('WRITER')
        article.title = request.form['title']
        article.content=request.form['content']
        article.writer = writer
        article.add_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
        article.category_id = request.form['category_id']
        try:
            db.session.commit()
            flash('修改成功', 'alert-success')
        except Exception as e:
            db.session.rollback()
            flash('错误信息：'+str(e), 'alert-danger')
    return render_template('changeArticle.html',article=article, categories=categories)

@adminArticleView.route('/delete/<int:id>')
@login_required
def article_delete(id):
    print(id)
    try:
        article = Article.query.filter_by(id=id).first_or_404()
        db.session.delete(article)
        db.session.commit()
        flash('文章：'+str(article.title)+'已成功删除', 'alert-success')
    except Exception as e:
        flash('except:'+str(e),'alert-warning')
    return redirect(url_for('adminArticleView.article_list',page=1))

@adminArticleView.route('/select')
@login_required
def article_select(id):
    return 'article_select'