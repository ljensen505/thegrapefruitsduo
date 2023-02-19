import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
from os import getenv

HOST = "grapefruitswebsite@gmail.com"


def send_email(subject: str, body: str):
    load_dotenv()
    password = password = getenv("app_password")
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = HOST
    smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    smtp_server.login(HOST, password)
    smtp_server.sendmail(HOST, [getenv("email")], msg.as_string())
    smtp_server.quit()


if __name__ == "__main__":
    load_dotenv()
    subject = "TEST"
    body = "Hello world!"
    sender = "grapefruitswebsite@gmail.com"
    recipient = "lucas.p.jensen10@gmail.com"
    password = getenv("app_password")
    print(password)
    send_email(subject, body, sender, recipient, password)
