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


if __name__ == '__main__':
    app.run()
