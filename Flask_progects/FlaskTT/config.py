class Configure(object):
    DEBUG = True
    SECRET_KEY = 'password'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///mydb.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
