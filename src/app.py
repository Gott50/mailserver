import json

from flask import request
from flask_mail import Message

from config import setup_mail

from settings import app

mail = setup_mail(app)


@app.route("/mail/wrong_login_data/", methods=['POST'])
def wrong_login_data():
    try:
        data = json.loads(request.data)
        email = data["email"]
        username = data["username"]

        msg = Message(body="Please check your password settings",
                      recipients=[email],
                      subject="Wrong Login Data"
                      )
        mail.send(msg)


        return "send mail to %s: %s" % (email, username)


    except KeyError as e:
        return 600 # TODO research right status code


if __name__ == '__main__':
    app.run(port=7070)
