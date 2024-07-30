from twilio.rest import Client
from kafka import KafkaConsumer
from json import loads
import os
from dotenv import load_dotenv

load_dotenv()

def send_sms_notification(data):
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_=os.getenv('TWILIO_NUMBER'), to=data["to"], body=data["body"]
    )

    print(message.sid)


if __name__ == "__main__":
    consumer = KafkaConsumer(
        "sms",
        bootstrap_servers=["localhost:9092"],
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        group_id="notification-update-group",
        value_deserializer=lambda x: loads(x.decode("utf-8")),
    )

    for message in consumer:
        print(message.value)
        send_sms_notification(message.value)
        print("sms sent to: ", message.value["to"])
