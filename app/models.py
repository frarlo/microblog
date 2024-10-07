from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db

# Class to define a user in our DB:
class User(db.Model):
    # Defining the User's ID as the PK:
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    # The rest of the fields:
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(128), index=True, unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))

    # Prints the object of this class:
    def __repr__(self):
        return '<User {}>'.format(self.username)