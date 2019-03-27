import os

basedir = os.path.abspath(os.path.dirname(__file__))
devDB = 'feature.db'
prodDB = 'feature.db'


class Config:
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'itsasecret'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'\
                              + os.path.join(basedir, devDB)


class ProductionConfig(Config):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'itsasecret'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'\
                              + os.path.join(basedir, prodDB)
