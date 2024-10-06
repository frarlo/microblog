import os

# Class to store configuration variables:
class Config:
    # For learning purposes. In a real app, a "secret" key is never meant to be shared or hardcoded:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'