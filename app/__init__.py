from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import config

TITLES = ['a', 'b', 'c']
db = SQLAlchemy()


def seed_db():
  db.drop_all()
  db.create_all()
  from .models import Post
  posts = [Post(title=title)
           for title in TITLES]
  db.session.add_all(posts)
  db.session.commit()


def create_app(config_name):
  app = Flask(__name__)
  app.config.from_object(config[config_name])
  config[config_name].init_app(app)
  db.init_app(app)

  ctx = app.app_context()
  ctx.push()
  seed_db()
  ctx.pop()

  return app
