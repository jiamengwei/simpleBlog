from app import db, login_manager
from flask_login import UserMixin
from datetime import datetime

class Setting(db.Model):
    __tablename__ = 'setting'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False, default='Simple Blog')
    sign = db.Column(db.String(120), nullable=False, default='Happy everyday')
    add_time = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return '<name %r>' % self.name

class Link(db.Model):
    __tablename__ = 'link'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(120),nullable=False)
    add_time = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return '<address %r>' % self.address

class User(db.Model,UserMixin):
    '''
        http://docs.sqlalchemy.org/en/latest/core/metadata.html#sqlalchemy.schema.Column
    '''
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20), nullable=False,unique=True)
    email = db.Column(db.String(10), nullable=True, unique=True)
    password = db.Column(db.String(100), nullable=False)
    add_time = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return '<email %r>' % self.email

@login_manager.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()

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
    # writer_site = db.Column(db.String(120))
    add_time = db.Column(db.DateTime, default=datetime.now)    
    article_id = db.Column(db.Integer, db.ForeignKey('article.id'))

    def __repr__(self):
        return '<writer %r, content %r>' % (self.writer,self.content)

class Image(db.Model):

    __tablename__='Image'
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(100), nullable=False)
    add_time = db.Column(db.DateTime, default=datetime.now)

