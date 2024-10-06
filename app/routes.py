from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    # Hardcoded user:
    user = {'username': 'frarlo'}
    # Hardcoded posts:
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'What a sunny day in Valencia!'
        },
        {
            'author': {'username': 'Susie'},
            'body': 'Has anyone seen Toto?'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
