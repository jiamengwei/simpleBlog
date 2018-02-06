import sys
sys.path.append('..')
from model import User
from flask_wtf import FlaskForm
from wtforms import StringField, fields, validators
from wtforms.validators import DataRequired
from werkzeug.security import generate_password_hash, check_password_hash


class LoginForm(FlaskForm):

    email = fields.StringField('邮箱', validators = [DataRequired()])
    password = fields.StringField('密码', validators = [DataRequired()])

    def validate_email(self,field):
        user = self.get_user()
        if user is None:
            raise validators.ValidationError('用户不存在')
        # we're comparing the plaintext pw with the the hash from the db
        if not check_password_hash(user.password, self.password.data):
        # to compare plain text passwords use
        # if user.password != self.password.data:
            raise validators.ValidationError('密码错误')

    def get_user(self):
        return User.query.filter_by(email=self.email.data).first()


class RegistrationForm(FlaskForm):
    
    email = fields.StringField('邮箱', validators = [DataRequired()])
    password = fields.StringField('密码',validators = [DataRequired()])

    def validate_email(self,field):
        if User.query.filter_by(email=self.email.data).count() > 0:
            raise validators.ValidationError('邮箱已存在')