import os
basedir = os.path.abspath(os.path.dirname(__file__))

# Class to store configuration variables:
class Config:
    # For learning purposes. In a real app, a "secret" key is never meant to be shared or hardcoded:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # Getting the DB config var, if it is not defined we default it:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')