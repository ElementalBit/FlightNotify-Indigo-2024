from kafka import KafkaConsumer
from json import loads, dumps, JSONDecodeError
import datetime

import requests

from db_connect import get_database


def generate_delay_notification(user, flight, update):
    prev_time = flight["departure_time"]
    new_time = datetime.datetime.fromisoformat(update["departure_time"]).replace(
        tzinfo=None
    )

    delay_minutes = new_time - prev_time
    message = f"Dear {user['name']}, your flight {flight['flight_number']} scheduled from {flight['departure_airport']} to {flight['arrival_airport']} is delayed by {delay_minutes} minutes. New departure time: {new_time}."

    return message


def generate_cancellation_notification(user, flight):
    message = f"Dear {user['name']}, we regret to inform you that your flight {flight['flight_number']} scheduled from {flight['departure_airport']} to {flight['arrival_airport']} has been cancelled. Please contact support for further assistance."
    return message


def generate_gate_change_notification(user, flight, new_gate):
    message = f"Dear {user['name']}, there has been a gate change for your flight {flight['flight_number']} scheduled from {flight['departure_airport']} to {flight['arrival_airport']}. The new gate is {new_gate}."
    return message


if __name__ == "__main__":
    db = get_database()
    flight = db.flights

    consumer = KafkaConsumer(
        "flight-update",
        bootstrap_servers=["localhost:9092"],
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        group_id="flight-update-group",
        value_deserializer=lambda x: loads(x.decode("utf-8")),
    )

    for message in consumer:
        try:
            decoded_message = message.value

            flight_details = flight.aggregate(
                [
                    {"$match": {"flight_number": decoded_message["flight_number"]}},
                    {
                        "$lookup": {
                            "from": "users",
                            "localField": "passengers",
                            "foreignField": "_id",
                            "as": "passengers",
                        }
                    },
                    {"$project": {"passengers": {"tickets": 0}}},
                ]
            )

            flight_details = list(flight_details)[0]
            passengers = flight_details["passengers"].copy()
            del flight_details["passengers"]

            for passenger in passengers:
                if decoded_message["status"] == "Delayed":
                    msg = generate_delay_notification(
                        passenger, flight_details, decoded_message
                    )
                elif decoded_message["status"] == "Cancelled":
                    msg = generate_cancellation_notification(passenger, flight_details)
                elif decoded_message["status"] == "Gate-Change":
                    msg = generate_gate_change_notification(
                        passenger, flight_details, decoded_message["gate"]
                    )
                else:
                    msg = ""

                if passenger["notification_preferences"]["email"]:
                    payload = {
                        "to": passenger["email"],
                        "subject": f"{flight_details['flight_number']} {decoded_message['status']}",
                        "body": msg,
                    }
                    email_notification = requests.post(
                        "http://127.0.0.1:5000/api/notifications/email",
                        headers={"Content-Type": "application/json"},
                        data=dumps(payload),
                    )
                if passenger["notification_preferences"]["sms"]:
                    payload = {
                        "to": passenger["phone_number"],
                        "title": f"{flight_details['flight_number']} {decoded_message['status']}",
                        "body": msg,
                    }

                    sms_notification = requests.post(
                        "http://127.0.0.1:5000/api/notifications/sms",
                        headers={"Content-Type": "application/json"},
                        data=dumps(payload),
                    )
                if passenger["notification_preferences"]["push"]:
                    payload = {
                        "user_id": passenger["_id"],
                        "body": msg,
                        "token": ""
                    }

                    push_notification = requests.post(
                        "http://127.0.0.1:5050/api/notifications/push",
                        headers={"Content-Type": "application/json"},
                        data=dumps(payload, default=str),
                    )

                # print(decoded_message)

        except JSONDecodeError as e:
            print(f"JSONDecodeError: {e} for message: {message.value}")
