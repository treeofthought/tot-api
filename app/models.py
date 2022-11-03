from . import db


class Post(db.Model):
  __tablename__ = 'posts'
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(256))
  slug = db.Column(db.String(128))
  preview = db.Column(db.Text)
  body = db.Column(db.Text)
  date = db.Column(db.Date)

  def to_json(self):
    out = {
        'title': self.title,
        'body': self.body
    }
    return out

  # def to_summary_json(self):
    out = {
        'title': self.title,
        'preview': self.preview,
        'date': self.date.strftime('%b %d, %Y'),
        'blogSlug': self.slug
    }

  #   return out

  @staticmethod
  def list_json():
    posts = Post.query.order_by(Post.date.desc()).all()
    list_json = [post.to_summary_json() for post in posts]
    return list_json

  @staticmethod
  def most_recent_json():
    p = Post.query.order_by(Post.date.desc()).first()
    return p.to_summary_json()
