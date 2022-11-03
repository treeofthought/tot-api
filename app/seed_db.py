import os
import yaml

from . import db
from .models import Post

TITLES = [{'title': 'a', 'preview': 'aPREVIEW'},
          {'title': 'b'}, {'title': 'c'}]


def read_body(root, name):
  body_path = os.path.join(root, name, 'body.md')
  with open(body_path, 'rb') as post_file:
    body = post_file.read()
    body = body.decode('UTF-8')
  return body


def read_config(root, name):
  config_path = os.path.join(root, name, 'config.yaml')
  with open(config_path, 'rb') as config_file:
    config = yaml.safe_load(config_file)
    config['slug'] = name
    return config


def seed_db(app):
  # Dev?
  with app.app_context():
    db.drop_all()
    db.create_all()

    basedir = os.path.abspath(os.path.dirname(__file__))
    postdir = os.path.join(basedir, '../posts')
    configs = []

    for root, dirs, files in os.walk(postdir):
      for name in dirs:
        body = read_body(root, name)
        config = read_config(root, name)
        config['body'] = body
        configs.append(config)

    posts = [Post(**config) for config in configs]
    db.session.add_all(posts)
    db.session.commit()
