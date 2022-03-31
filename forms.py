from flask_wtf import FlaskForm as Form
from wtforms.fields import StringField, SubmitField
from wtforms.validators import Required, InputRequired

class LoginForm(Form):
    name = StringField('Name', validators=[InputRequired()])
    room = StringField('Room', validators=[InputRequired()])
    submit = SubmitField('Enter Chatroom')