from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import UserMixin

from .extensions import db


class Reminder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(160), nullable=False)
    send_on = db.Column(db.DateTime, nullable=False)
    sent_on = db.Column(db.DateTime)

    @property
    def status(self):
        return 'delivered' if self.sent_on else 'pending'


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(75), unique=True)
    password = db.Column(db.String(150))

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
