from datetime import datetime

from flask import current_app
from sqlalchemy import and_

from .extensions import celery, db
from .models import Reminder


@celery.task()
def send_reminders():
    now = datetime.now()
    reminders = Reminder.query.filter(
        and_(Reminder.send_on <= now,
             Reminder.sent_on == None)).all()

    for reminder in reminders:
        # TODO - Send SMS Reminder message
        reminder.sent_on = now
        db.session.add(reminder)
        db.session.commit()
