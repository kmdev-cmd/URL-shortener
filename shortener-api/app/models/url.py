from ..database import db
from datetime import datetime

class User(db.Model):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True, index=True)
    email = db.Column(db.String, unique=True, index=True, nullable=False)
    hashed_password = db.Column(db.String, nullable=False)
    
    urls = db.relationship("Url", back_populates="owner")

class Url(db.Model):
    __tablename__ = "urls"
    
    id = db.Column(db.Integer, primary_key=True, index=True)
    original_url = db.Column(db.String, nullable=False)
    short_code = db.Column(db.String, unique=True, index=True, nullable=False)
    clicks = db.Column(db.BigInteger, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    owner_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    
    owner = db.relationship("User", back_populates="urls")
