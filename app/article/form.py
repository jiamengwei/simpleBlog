from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, Field
from wtforms.validators import DataRequired, InputRequired, Optional

class ArticleForm(FlaskForm):

    title = StringField('名称', validators=[InputRequired()])
    writer = StringField('作者', validators=[InputRequired()])
    category_id = SelectField('分类',coerce=int)


