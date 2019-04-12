import json

from flask import request
from flask_mail import Message

from config import setup_mail

from settings import app

mail = setup_mail(app)


@app.route("/")
def index():
    msg = Message(body="Hello",
                  recipients=["to@example.com"],
                  subject="test"
                  )
    mail.send(msg)


@app.route("/mail/wrong_login_data/", methods=['POST'])
def wrong_login_data():
    try:
        data = json.loads(request.data)
        email = data["email"]
        username = data["username"]

        return "%s: %s" % (email, username)


    except KeyError as e
        return 600 # TODO research right status code


if __name__ == '__main__':
    app.run()
