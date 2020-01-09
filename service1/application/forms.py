from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class NameForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Generate')