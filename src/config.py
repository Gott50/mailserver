import os


class BaseConfig(object):
    DEBUG = os.environ['DEBUG']

# At top of file
from flask_mail import Mail


# After 'Create app'
def setup_mail(app):
    app.config['MAIL_DEFAULT_SENDER'] = os.environ['SECURITY_EMAIL_SENDER']
    app.config['MAIL_SERVER'] = os.environ['MAIL_SERVER']
    app.config['MAIL_PORT'] = os.environ['MAIL_PORT']
    app.config['MAIL_USE_SSL'] = os.environ.get('MAIL_USE_SSL', True)
    app.config['MAIL_USERNAME'] = os.environ['MAIL_USERNAME']
    app.config['MAIL_PASSWORD'] = os.environ['MAIL_PASSWORD']
    app.config['MAIL_DEBUG'] = 1 if app.debug else 0
    mail = Mail(app)
    return mail
