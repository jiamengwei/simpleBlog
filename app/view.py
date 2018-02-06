from __init__ import create_app, db, login_manager
from flask import render_template
from flask_admin import Admin, AdminIndexView, helpers, expose
from flask_admin.contrib.sqla import ModelView
from model import User, Article, Category, Comment, Setting
from admin.view import MyAdminIndexView
app = create_app()


@login_manager.user_loader
def load_user(user_id):
    return User()

admin = Admin(app, 'Example: Auth', index_view=MyAdminIndexView(), base_template='my_master.html')
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Article, db.session))
admin.add_view(ModelView(Comment, db.session))
admin.add_view(ModelView(Category, db.session))
admin.add_view(ModelView(Setting, db.session))

@app.route('/')
def index():
   return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True,host='0.0.0.0', port=8000)