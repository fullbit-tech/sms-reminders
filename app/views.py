from flask import Blueprint, render_template, flash, request, redirect, url_for

from .extensions import db
from .models import Reminder
from .forms import ReminderForm


reminders = Blueprint('reminders', __name__, template_folder="templates")


@reminders.route('/', methods=['GET', 'POST'])
def index():
    form = ReminderForm(request.form)

    if request.method == 'POST' and form.validate():
        reminder = Reminder()
        form.populate_obj(reminder)
        db.session.add(reminder)
        db.session.commit()
        flash('Reminder created!', 'success')
        redirect(url_for('reminders.index'))

    reminders = Reminder.query.all()
    return render_template('index.html', reminders=reminders, form=form)


@reminders.route('/reminder/<reminder_id>/delete', methods=['GET'])
def delete_reminder(reminder_id):
    reminder = Reminder.query.filter_by(id=reminder_id).first_or_404()
    db.session.delete(reminder)
    db.session.commit()
    flash('Reminder deleted!', 'success')
    return redirect(url_for('reminders.index'))
