import unittest
from flask import current_app
from app import create_app, db, TITLES
from app.models import Post


class BasicsTestCase(unittest.TestCase):
  def setUp(self):
    db.create_all()
    self.app = create_app('testing')
    self.app_context = self.app.app_context()
    self.app_context.push()

  def tearDown(self):
    db.session.remove()
    db.drop_all()
    self.app_context.pop()

  def test_app_exists(self):
    self.assertFalse(current_app is None)

  def test_app_is_testing(self):
    self.assertTrue(current_app.config['TESTING'])

  def test_app_has_seeded(self):
    posts = Post.query.all()
    self.assertEqual(len(posts), len(TITLES))

    expected_title_set = set(TITLES)
    actual_title_set = set([post.title for post in posts])
    self.assertEqual(expected_title_set, actual_title_set)
