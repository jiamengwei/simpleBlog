class Config():

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:mysqlpassword@localhost:3306/simpleBlog?charset=utf8mb4'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    UPLOAD_FOLDER = 'images/user/'
    SECRET_KEY = 'qwer'
    BLOG_NAME = 'SimpleBlog'
    WRITER = 'JiaMengwei'