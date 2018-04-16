from flask import Blueprint, render_template, flash, request, redirect, url_for

from flask_login import login_user, logout_user, login_required

from .extensions import db
from .models import Reminder, User
from .forms import ReminderForm, LoginForm


reminders = Blueprint('reminders', __name__, template_folder="templates")


@reminders.route('/', methods=['GET', 'POST'])
@login_required
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
@login_required
def delete_reminder(reminder_id):
    reminder = Reminder.query.filter_by(id=reminder_id).first_or_404()
    db.session.delete(reminder)
    db.session.commit()
    flash('Reminder deleted!', 'success')
    return redirect(url_for('reminders.index'))


@reminders.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Logged in Sucessfully!', 'success')
            return redirect(url_for('reminders.index'))
        else:
            flash('Wrong email or password', 'danger')
            return redirect(url_for('reminders.login'))
    return render_template('login.html', form=form)


@reminders.route('/logout', methods=['GET'])
def logout():
    logout_user()
    flash('You are not logged out!', 'success')
    return redirect(url_for('reminders.login'))
