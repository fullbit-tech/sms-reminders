from .extensions import db


class Reminder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(160), nullable=False)
    send_on = db.Column(db.DateTime, nullable=False)
    sent_on = db.Column(db.DateTime)
