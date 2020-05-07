import os


basedir = os.path.abspath(os.path.dirname(__file__)) # в переменной __file__  лежит имя файла


class Config():
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')