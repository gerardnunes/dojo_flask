from app import core
from datetime import datetime
from app import core
from app.core import db
from models import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(250))
    last_name = db.Column(db.String(250))
    age = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now())
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.now())