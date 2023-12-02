from datetime import datetime
from app import db
from app import login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class Users(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    numberQueries = db.Column(db.Integer)
    isAdmin = db.Column(db.Boolean)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_admin(self):
        return self.isAdmin

    def inc_num_queries(self):
        if self.numberQueries is None:
            self.numberQueries = 0
        self.numberQueries += 1

    def get_username(self):
        return self.username

    def inc_num_queries(self):
        if self.numberQueries is None:
            self.numberQueries = 0
        self.numberQueries += 1

    def get_username(self):
        return self.username

    def get_is_admin(self):
        return self.isAdmin


@login.user_loader
def load_user(id):
    return Users.query.get(int(id))
