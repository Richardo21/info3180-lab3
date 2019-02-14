from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, TextField
#from flask.ext.wtf import Form
from wtforms.validators import DataRequired

class ContactForm(FlaskForm):
    name = TextField('Name', validators=[DataRequired()])
    email = TextField('E-mail', validators=[DataRequired()])
    subject = TextField('Subject', validators=[DataRequired()])
    message = TextAreaField('Message', validators= [DataRequired()])