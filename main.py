from flask import Flask, render_template, request, redirect
from mail import send_email

app = Flask(__name__)


@app.route("/stream")
def stream():
    return render_template("stream.html")


@app.route("/youneedfacebook")
def fb():
    return "You need a facebook page", {"Refresh": "4; url=/"}


@app.route("/")
def index():
    return render_template("home.html")


@app.route("/confirmation")
def confirmation():
    return render_template("confirmation.html"), {"Refresh": "4; url=/"}


@app.route("/message")
def process_form():
    data = request.args
    name = data.get("Name")
    sender = data.get("Email")
    msg = data.get("Message")
    body = f"{name} at {sender} has sent you a message:\n\n{msg}"
    subject = f"{name} has sent you a message."
    send_email(subject, body)
    return redirect("/confirmation")


if __name__ == "__main__":
    app.run("", 8000, debug=True)
