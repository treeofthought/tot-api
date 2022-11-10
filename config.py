import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
  IMG_ROOT = 'http://127.0.0.1:5000/static'

  @staticmethod
  def init_app(app):
    pass


class TestingConfig(Config):
  TESTING = True

class HerokuConfig(Config):
  heroku_db_url = os.environ.get('DATABASE_URL')
  sqlalchemy_support = heroku_db_url.replace('postgres://', 'postgresql://')
  SQLALCHEMY_DATABASE_URI = sqlalchemy_support
  IMG_ROOT = 'https://tot-api.herokuapp.com/static'

config = {
    'default': Config,
    'development': Config,
    'production': Config,
    'testing': TestingConfig,
    'heroku': HerokuConfig
}
