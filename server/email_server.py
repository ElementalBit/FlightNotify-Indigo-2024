from email.message import EmailMessage
from kafka import KafkaConsumer
from json import loads, JSONDecodeError
import smtplib, ssl
import os
from dotenv import load_dotenv

load_dotenv()

def send_email_notification(data: dict):
    email_sender = os.getenv('EMAIL_SENDER')
    email_password = os.getenv('EMAIL_PASSWORD')
    email_receiver = data["to"]

    subject = data["subject"]
    body = data["body"]

    email = EmailMessage()
    email["From"] = email_sender
    email["to"] = email_receiver
    email["subject"] = subject
    email.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, email.as_string())


if __name__ == "__main__":
    consumer = KafkaConsumer(
        "email",
        bootstrap_servers=["localhost:9092"],
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        group_id="notification-update-group",
        value_deserializer=lambda x: loads(x.decode("utf-8")),
    )

    for message in consumer:
        print("Email sent to: ", message.value["to"])
        send_email_notification(message.value)
