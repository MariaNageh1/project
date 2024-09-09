from flask_sqlalchemy import SQLAlchemy # type: ignore
from flask_login import UserMixin # type: ignore

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    address = db.Column(db.String(250), nullable=False)
    specialization = db.Column(db.String(150), nullable=False)
    area = db.Column(db.String(150), nullable=False)
