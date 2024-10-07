from datetime import datetime, timezone
from operator import index
from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db

# Class to define a User in our DB:
class User(db.Model):
    # Defining the User's ID as the PK:
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    # The rest of the fields:
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(128), index=True, unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))

    # The user has many posts in the table:
    posts: so.WriteOnlyMapped['Post'] = so.relationship(back_populates='author')

    # Prints the object of this class:
    def __repr__(self):
        return '<User {}>'.format(self.username)

# Class to define a Post made by a User:
class Post(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    body: so.Mapped[str] = so.mapped_column(sa.String(140))
    timestamp: so.Mapped[datetime] = so.mapped_column(
        index=True, default=lambda: datetime.now(timezone.utc))

    # The Post has only one author, and therefore only one user_id:
    user_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(User.id), index=True)
    author: so.Mapped[str] = so.relationship(back_populates='posts')

    def __repr__(self):
        return '<Post {}>'.format(self.body)