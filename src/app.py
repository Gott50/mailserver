import json

from flask import request
from flask_mail import Message

from config import setup_mail

from settings import app

mail = setup_mail(app)


@app.route("/mail/", methods=['POST'])
def send():
    try:
        data = json.loads(request.data)
        app.logger.warning("%s" % data)

        email = data["email"]
        subject = data["subject"]
        body = data["body"]
        msg = Message(body=body,
                      recipients=[email],
                      subject=subject)
        mail.send(msg)

        result = "send Mail to: %s; with subject: %s; with body: %s" % (email, subject, body)
        app.logger.warning(result)
        return result

    except KeyError as e:
        app.logger.error("KeyError: %s" % e)
        return "KeyError", 501  # Not Implemented


if __name__ == '__main__':
    app.run(port=7070)
