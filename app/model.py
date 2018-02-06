# import sys,os
# print(sys.path)
# a = os.path.dirname(os.path.abspath(__file__))
# sys.path.append(a)
from __init__ import db
from flask_login import UserMixin
from datetime import datetime

class Setting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False, default='Simple Blog')
    sign = db.Column(db.String(120), nullable=False, default='Happy everyday')
    imagepath = db.Column(db.String(80))
    add_time = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return '<name %r>' % self.name

class User(db.Model,UserMixin):

    '''
        http://docs.sqlalchemy.org/en/latest/core/metadata.html#sqlalchemy.schema.Column
    '''
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(10), nullable=False, unique = True)
    password = db.Column(db.String(100), nullable=False)
    iconpath = db.Column(db.String(80)) 
    add_time = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return '<email %r>' % self.email


class Article(db.Model):

    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    writer = db.Column(db.String(10), nullable=False)
    content = db.Column(db.Text, nullable=False)
    add_time = db.Column(db.DateTime,  default=datetime.now)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    comment = db.relationship('Comment', backref='article', lazy='dynamic')
    ''' 
        db.relationship参数说明

            http://docs.sqlalchemy.org/en/latest/orm/relationship_api.html#sqlalchemy.orm.relationship
            Category:表示一个映射的类，表示关系的目标,也就是下面的Category类
            backref:表示将在相关的映射类上放置一个属性的字符串名称，该属性将在另一个方向处理该关系
            dynamic:返回一个预配置的查询对象，用于所有的读操作，在迭代结果之前可以应用进一步的过滤操作
    '''
    def __repr__(self):
        return '<title %r>' % self.title

class Category(db.Model):

    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), nullable=False,unique=True)
    description = db.Column(db.String(120), nullable=False)
    add_time = db.Column(db.DateTime, default=datetime.now)
    articel = db.relationship('Article', backref='category', lazy='dynamic')
    '''
        db.ForeignKey参数说明

            http://docs.sqlalchemy.org/en/latest/core/constraints.html#sqlalchemy.schema.ForeignKey
    '''
    def __repr__(self):
        return '<name %r>' % self.name

class Comment(db.Model):

    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True)
    writer = db.Column(db.String(20), nullable=False)
    content = db.Column(db.String(255), nullable=False)
    writer_email = db.Column(db.String(80), nullable=False)
    writer_site = db.Column(db.String(120), nullable=False)
    add_time = db.Column(db.DateTime, default=datetime.now)    
    article_id = db.Column(db.Integer, db.ForeignKey('article.id'))

    def __repr__(self):
        return '<writer %r, content %r>' % (self.writer,self.content)