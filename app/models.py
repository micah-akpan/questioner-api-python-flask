from datetime import datetime
from app import db

class Meetup(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  topic = db.Column(db.String(80))
  location = db.Column(db.String(255))
  happeningOn = db.Column(db.DateTime, default=datetime.utcnow)
  createdOn = db.Column(db.DateTime, default=datetime.utcnow)

