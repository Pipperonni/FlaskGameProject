from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    user_items = db.relationship('UsersItems', backref='uitems', lazy=True)
    user_tokens = db.relationship('UsersTokens', backref='utokens', lazy=True)

    def __repr__(self):
        return f'User: {self.username}'

class UsersItems(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_item = db.Column(db.String)
    date_item_aquired = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'User: {self.user_item}'

class UsersTokens(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_tokens = db.Column(db.Integer, nullable=False, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'User: {self.user_tokens}'