import sys
from application import db
import datetime


class GitHubUser(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(120))
    github_id = db.Column(db.Integer)
    image_url = db.Column(db.String(250))
    type = db.Column(db.String(250))
    github_url = db.Column(db.String(250))
    create_date = db.Column(db.TIMESTAMP, default=datetime.datetime.now())

    def __init__(self, username, github_id, image_url, type, github_url):
        self.username = username
        self.github_id = github_id
        self.image_url = image_url
        self.type = type
        self.github_url = github_url

    @property
    def serialize(self):
       """Return object data in easily serializable format"""
       return {
           'id'         : self.id,
           'username': self.username,
           'github_id': self.github_id,
           'image_url': self.image_url,
           'type': self.type,
           'github_url': self.github_url,

       }

    def __repr__(self):
        return '<GitHubUser %r %s>' % (self.id, self.username)
