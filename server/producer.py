from flask import Flask, request
from flask_cors import CORS

from time import sleep
from json import dumps

from kafka import KafkaProducer

app = Flask(__name__)
CORS(app)

# Producer which publishes the flight status
@app.route('/api/flight-update', methods=['POST'])
def flightUpdate():
    # flight data to be published
    data = request.get_json()

    producer = KafkaProducer(
        bootstrap_servers=["localhost:9092"],
        value_serializer=lambda x: dumps(x).encode("utf-8"),
    )

    producer.send('flight-update', value=data)
    producer.flush()
    return data

# Producer which publishes the email request
# Kafka Topic email
@app.route('/api/notifications/email', methods=['POST'])
def emailUpdate():
    # email data to be sent
    data = request.get_json()

    producer = KafkaProducer(
        bootstrap_servers=["localhost:9092"],
        value_serializer=lambda x: dumps(x).encode("utf-8"),
    )

    producer.send('email', value=data)
    print("Published email")
    producer.flush()
    return data

# Producer which publishes the sms request
# Kafka Topic sms
@app.route('/api/notifications/sms', methods=['POST'])
def smsUpdate():
    # sms data to be sent
    data = request.get_json()

    producer = KafkaProducer(
        bootstrap_servers=["localhost:9092"],
        value_serializer=lambda x: dumps(x).encode("utf-8"),
    )

    producer.send('sms', value=data)
    print("Published sms")
    producer.flush()
    return data

if __name__ == "__main__":
    app.run(debug=True)