from flask import Blueprint, render_template, flash
from .models import Reminder


reminders = Blueprint('reminders', __name__, template_folder="templates")


@reminders.route('/')
def index():
    reminders = Reminder.query.all()
    return render_template('index.html', reminders=reminders)
