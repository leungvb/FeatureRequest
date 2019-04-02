import os

POSTGRES_USER = os.environ.get('POSTGRES_USER')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
POSTGRES_DB = os.environ.get('POSTGRES_DB')


class Config:
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'itsasecret'
    SQLALCHEMY_DATABASE_URI = f"postgres://{POSTGRES_USER}:" \
                              f"{POSTGRES_PASSWORD}@localhost:5432/{POSTGRES_DB}"


class ProductionConfig(Config):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = f"postgres://{POSTGRES_USER}:" \
                              f"{POSTGRES_PASSWORD}@localhost:5432/{POSTGRES_DB}"
