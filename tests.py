import os
# NOT USING 'PRODUCTION' DB:
os.environ['DATABASE_URL'] = 'sqlite://'

from datetime import datetime, timezone, timedelta
import unittest
from app import app, db
from app.models import User, Post

class UserModelCase(unittest.TestCase):
    # Orchestration of the test:
    def setUp(self):
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()

    # Dismantling the test:
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    # Tests the password hashing:
    def test_password_hashing(self):
        u = User(username = 'susan', email = 'susan@example.com')
        u.set_password('cat')
        self.assertFalse(u.check_password('dog'))
        self.assertTrue(u.check_password('cat'))

    # Tests the avatar function:
    def test_avatar(self):
        u = User(username = 'john', email = 'john@example.com')
        self.assertEqual(u.avatar(128), ('https://www.gravatar.com/avatar/'
                                         'd4c74594d841139328695756648b6bd6'
                                         '?d=identicon&s=128'))

    # Test the follow function and the following/followers count:
    def test_follow(self):
        # We create two users and add them to the DB:
        u1 = User(username = 'john', email = 'john@example.com')
        u2 = User(username = 'susan', email = 'susan@example.com')
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()

        # Assert that both users does not follow or are followed.
        following = db.session.scalars(u1.following.select()).all()
        followers = db.session.scalars(u2.following.select()).all()
        self.assertEqual(following, [])
        self.assertEqual(followers, [])

        # Make user1 to follow user2 and assert their following/followed counts:
        u1.follow(u2)
        db.session.commit()
        self.assertTrue(u1.is_following(u2))
        self.assertEqual(u1.following_count(), 1)
        self.assertEqual(u2.followers_count(), 1)
        u1_following = db.session.scalars(u1.following.select()).all()
        u2_followers = db.session.scalars(u2.followers.select()).all()
        self.assertEqual(u1_following[0].username, 'susan')
        self.assertEqual(u2_followers[0].username, 'john')

        # Unfollow and assert that the counts are updated accordingly:
        u1.unfollow(u2)
        db.session.commit()
        self.assertFalse(u1.is_following(u2))
        self.assertEqual(u1.following_count(), 0)
        self.assertEqual(u2.followers_count(), 0)

    # Test to assert the posts of each user:
    def test_follow_posts(self):
        # Creation of four users and adding them to the DB:
        u1 = User(username = 'john', email = 'john@example.com')
        u2 = User(username = 'susan', email = 'susan@example.com')
        u3 = User(username = 'maría', email = 'maria@example.com')
        u4 = User(username = 'fer', email = 'fer@example.com')
        db.session.add_all([u1, u2, u3, u4])

        # Creation of four posts and adding them to the DB:
        now = datetime.now(timezone.utc)
        p1 = Post(body = 'Post from John.', author = u1,
                  timestamp = now + timedelta(seconds = 1))
        p2 = Post(body='Post from Susan.', author=u2,
                  timestamp=now + timedelta(seconds=4))
        p3 = Post(body='Post de Jesús.', author=u3,
                  timestamp=now + timedelta(seconds=3))
        p4 = Post(body='Post de Fer.', author=u4,
                  timestamp=now + timedelta(seconds=2))
        db.session.add_all([p1, p2, p3, p4])
        db.session.commit()

        # Setting up the followers:
        u1.follow(u2)                   # John follows Susan
        u1.follow(u4)                   # John follows Fer
        u2.follow(u3)                   # Susan follows María
        u3.follow(u4)                   # María follows Fer
        db.session.commit()

        # Checking the following posts of each user:
        f1 = db.session.scalars(u1.following_posts()).all()
        f2 = db.session.scalars(u2.following_posts()).all()
        f3 = db.session.scalars(u3.following_posts()).all()
        f4 = db.session.scalars(u4.following_posts()).all()
        self.assertEqual(f1, [p2, p4, p1])
        self.assertEqual(f2, [p2, p3])
        self.assertEqual(f3, [p3, p4])
        self.assertEqual(f4, [p4])

if __name__ == '__main__':
    unittest.main(verbosity = 2)