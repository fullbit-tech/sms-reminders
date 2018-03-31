from wtforms import (Form, StringField, DateTimeField, SubmitField,
                     validators as v)
from wtforms.widgets import TextArea


class ReminderForm(Form):
    message = StringField('Message', validators=[
        v.Length(min=1, max=160), v.InputRequired()], widget=TextArea())
    send_on = DateTimeField('Send On', validators=[
        v.InputRequired()], format='%Y/%m/%d %H:%M')
    submit = SubmitField('Create')
