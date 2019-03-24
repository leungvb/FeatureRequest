import os

basedir = os.path.abspath(os.path.dirname(__file__))
devDB = 'feature.db'
prodDB = 'feature.db'


class Config:
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'itsasecretkey'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'\
                              + os.path.join(basedir, devDB)


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'\
                              + os.path.join(basedir, prodDB)
