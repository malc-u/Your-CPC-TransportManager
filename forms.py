from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

class ContactForm(FlaskForm):
    name = StringField('Your name:', validators=[DataRequired()])
    email = StringField('Your e-mail:', validators=[DataRequired()])
    message = TextAreaField('Massage to us:', validators=[DataRequired(), Length(max=800)])
    bot = BooleanField('Click here to confirm the above:', validators=[DataRequired()])
    submit = SubmitField('Send')