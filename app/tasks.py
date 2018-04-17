from datetime import datetime

from flask import current_app
from sqlalchemy import and_
from twilio.rest import Client

from .extensions import celery, db
from .models import Reminder


@celery.task()
def send_reminders():
    client = Client(current_app.config['TWILIO_AUTH_ID'],
                    current_app.config['TWILIO_AUTH_TOKEN'])
    now = datetime.now()
    reminders = Reminder.query.filter(
        and_(Reminder.send_on <= now,
             Reminder.sent_on == None)).all()

    for reminder in reminders:
        client.messages.create(
            from_=current_app.config['TWILIO_FROM_NUMBER'],
            to=current_app.config['TWILIO_TO_NUMBER'],
            body=reminder.message)
        reminder.sent_on = now
        db.session.add(reminder)
        db.session.commit()
