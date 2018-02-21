from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators
from wtforms.validators import DataRequired
from model import User
from werkzeug.security import generate_password_hash, check_password_hash

class LoginForm(FlaskForm):
    name = StringField('用户名', validators=[DataRequired()])
    password = PasswordField('密码', validators=[DataRequired()])

    # user: a User object
    def validatName(self,field):
        user = self.getUser()
        if user is None:
            raise validators.ValidationError('用户不存在')
        # we're comparing the plaintext pw with the the hash from the db
        # if not check_password_hash(user.password, self.password.data):
        # to compare plain text passwords use
        if user.password != self.password.data:
            raise validators.ValidationError('密码错误')
        return True
    def getUser(self):
        return User.query.filter_by(email=self.email.data).first()

class RegisterForm(FlaskForm):
    name = StringField('用户名', validators=[DataRequired()])
    email = StringField('邮箱', validators=[DataRequired()])
    password = PasswordField('密码', validators=[DataRequired()])