from . import db


class Post(db.Model):
  __tablename__ = 'posts'
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(256))

  @staticmethod
  def list_json():
    posts = Post.query.all()
    list_json = [{'title': post.title} for post in posts]
    return list_json
