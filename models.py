import os
from flask_sqlalchemy import SQLAlchemy


DB_PATH = os.environ.get("SQLALCHEMY_DATABASE_URI")
DB_TEST_PATH = os.environ.get("SQLALCHEMY_TEST_DATABASE_URI")

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, test=True):

    if test:
        db_path = DB_TEST_PATH
    else:
        db_path = DB_PATH
    app.config["SQLALCHEMY_DATABASE_URI"] = db_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


class Table:
    """Base class for models in this module
    Defines common operations"""

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def rollback(self):
        db.session.rollback()


class User(db.Model, Table):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    joined_ts = db.Column(db.TIMESTAMP, nullable=False)
    tweet = db.relationship("Tweet", backref="tweet", lazy='dynamic')

    def describe(self):
        return {
            "username": self.username,
            "user id": self.id,
            "joined": self.joined_ts
        }


class Tweet(db.Model, Table):
    __tablename__ = 'tweet'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False)
    tweet_ts = db.Column(db.TIMESTAMP, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def describe(self):
        return {
            "tweet": self.text,
            "tweet id": self.id,
            "tweet timestamp": self.tweet_ts,
            "posted user": self.user_id
        }
