import os
basedir = os.path.abspath(os.path.dirname(__file__))

# Class to store configuration variables:
class Config:
    # For learning purposes. In a real app, a "secret" key is never meant to be shared or hardcoded:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # Getting the DB config var, if it is not defined we default it:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    # Email data to register errors:
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['your-email@example.com']
    # Posts per page:
    POSTS_PER_PAGE = 20