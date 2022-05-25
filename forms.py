from flask_wtf import FlaskForm as Form
from wtforms.fields import StringField, SubmitField
from wtforms import validators

class LoginForm(Form):
    name = StringField('Name', validators=[validators.DataRequired()])
    room = StringField('Room', validators=[validators.DataRequired()])
    submit = SubmitField('Enter Chatroom')