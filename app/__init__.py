from flask import Flask
from flask_mail import Mail

app = Flask(__name__)

app.config['SECRET_KEY'] = '3w3w3w'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '465' # (or try 2525)
app.config['MAIL_USERNAME'] = 'e164dd6603eed9'
app.config['MAIL_PASSWORD'] = '7e3faf2f6e7bba'

mail = Mail(app)
from app import views