import sqlalchemy as sa
import sqlalchemy.orm as so
from app import app, db
from app.models import User, Post

# Context function to return the objects we need when using the Flask shell:
@app.shell_context_processor
def make_shell_context():
    return {'sa': sa, 'so':so, 'db':db, 'User':User, 'Post':Post}