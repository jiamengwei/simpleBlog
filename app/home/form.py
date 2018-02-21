from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, TextAreaField

class CommentForm(FlaskForm):

	writer = StringField('昵称', validators=[DataRequired()])
	writer_email = StringField('邮箱', validators=[DataRequired()])
	content = TextAreaField('评论', validators=[DataRequired()])



		