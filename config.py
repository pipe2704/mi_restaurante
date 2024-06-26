import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://restaurant_user:felipechaves2704@@localhost/restaurant_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = Config()
