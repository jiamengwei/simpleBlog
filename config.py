

class Config():

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:mysqlpassword@localhost:3306/simpleBlog?charset=utf8mb4'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = 'qwer'