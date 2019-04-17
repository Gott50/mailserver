import json

from flask import request
from flask_mail import Message

from config import setup_mail

from settings import app

mail = setup_mail(app)


all_mails = {}
@app.route("/mail/", methods=['POST'])
def send():
    try:
        data = json.loads(request.data)
        app.logger.warning("%s" % data)

        username = data["username"]
        mail_once = data.get("once", False)

        if mail_once:
            if username in all_mails:
                if data in all_mails[username]:
                    result = "already send Mail to %s" % username
                    app.logger.warning(result)
                    return result
                all_mails[username] += [data]
            else:
                all_mails[username] = [data]
            app.logger.warning("all_mails: %s" % all_mails)

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
