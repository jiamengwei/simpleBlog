import sys
sys.path.append("..")
import app.model as model
from app.__init__ import create_app
from app.__init__ import db

app = create_app()
app.test_request_context().push()

# db.create_all()

jack = model.Article(title='biao ti',writer='jack',content='wo shi content')
db.session.add(jack)
db.session.commit()

# c = model.Comment.query.all()
# print(c)

# a = model.Article.query.first()
# print(a)
# print(a.category)
# print(a.category.all())

# id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(20), nullable=False)
#     writer = db.Column(db.String(10), nullable=False)
#     content = db.Column(db.Text, nullable=False)
#     add_time = db.Column(db.DateTime,  default=datetime.now)
#     category = db.relationship('Category', backref='article', lazy='dynamic')
#     comment = db.relationship(