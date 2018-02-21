from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class CategoryForm(FlaskForm):
    name = StringField('名称', validators=[DataRequired()])
    description = StringField('说明', validators=[DataRequired()])