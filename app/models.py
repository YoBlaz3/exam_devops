from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(20), nullable=False, unique=True)
    last_name = db.Column(db.String(20), nullable=False)
    first_name = db.Column(db.String(20), nullable=False)
    middle_name = db.Column(db.String(20))
    password_hash = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<User: %r>' % self.login

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Inf(db.Model):
    __tablename__ = 'info'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False, unique=True)
    duration = db.Column(db.String(50), nullable=False)
    time = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(100))
    
