import unittest
from flask import current_app
from app import create_app, db
from app.models import Post


class BasicsTestCase(unittest.TestCase):
  def setUp(self):
    self.app = create_app('testing')
    self.app_context = self.app.app_context()
    self.app_context.push()
    db.create_all()

    self.posts = [{
                'title' : 'Test1',
                'slug' : 'test1',
                'preview' : 'Test 1 preview',
                'body' : 'Test 1 body',
                'date' : '2021-01-01'
              },
              {
                'title' : 'Test2',
                'slug' : 'test2',
                'preview' : 'Test 2 preview',
                'body' : 'Test 2 body',
                'date' : '2021-01-02'
              }]

  def tearDown(self):
    db.session.remove()
    db.drop_all()
    self.app_context.pop()

  def test_app_exists(self):
    self.assertFalse(current_app is None)

  def test_app_is_testing(self):
    self.assertTrue(current_app.config['TESTING'])
