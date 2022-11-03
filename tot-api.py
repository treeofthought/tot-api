import os
from flask import jsonify
from flask_migrate import Migrate

from app import create_app, db, seed_db
from app.models import Post


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)

@app.route('/blog-list')
def blog_list():
  """List all posts"""
  return jsonify(Post.list_json())

@app.route('/blog-latest')
def blog_latest():
  """List most recent blog post"""
  return jsonify(Post.most_recent_json())

@app.route('/blogs/<slug>')
def blogs(slug):
  p = Post.query.filter_by(slug=slug).first()
  return p.to_json()

@app.shell_context_processor
def make_shell_context():
  return dict(db=db, Post=Post)


@app.cli.command()
def test():
  """Run the unit tests."""
  import unittest
  tests = unittest.TestLoader().discover('tests')
  unittest.TextTestRunner(verbosity=2).run(tests)


@app.cli.command()
def lint():
  """Run the linter"""
  os.system('flake8')


@app.cli.command()
def seed():
  """Populate the database"""
  seed_db()
