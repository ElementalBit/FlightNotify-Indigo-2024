from flask import Flask, request
from flask_cors import CORS
from db_connect import get_database
from json import dumps, loads
from bson import ObjectId
from pywebpush import webpush, WebPushException
from flask import current_app
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)


@app.route("/api/user/login", methods=["POST"])
def getUser():
    data = request.get_json()
    db = get_database()

    user = db.users.find_one({"email": data["email"]})

    return dumps({"user_id": user["_id"]}, default=str)


@app.route("/api/get/notifications/all", methods=["POST"])
def emailUpdate():
    data = request.get_json()
    db = get_database()

    user = db.users.find_one({"_id": ObjectId(data["user_id"])})

    return dumps(user, default=str)


@app.route("/api/get/trips/all", methods=["POST"])
def smsUpdate():
    data = request.get_json()
    db = get_database()

    tickets = db.tickets.aggregate(
        [
            {"$match": {"user_id": ObjectId(data["user_id"])}},
            {
                "$lookup": {
                    "from": "flights",
                    "localField": "flight_id",
                    "foreignField": "_id",
                    "as": "flight_details",
                }
            },
            {
                "$project": {
                    "PNR": 1,
                    "status": 1,
                    "flight_details": {
                        "flight_number": 1,
                        "departure_airport": 1,
                        "arrival_airport": 1,
                    },
                }
            },
        ]
    )

    return dumps(list(tickets), default=str)


@app.route("/api/notifications/push", methods=["POST"])
def pushNotificationUpdate():
    data = request.get_json()
    db = get_database()

    user = db.users.update_one(
        {"_id": ObjectId(data["user_id"])}, {"$push": {"notifications": data["body"]}}
    )
    print("Inside /api/notifications/push", data)
    if data.get("subscription", None):
        trigger_push_notifications(data["subscription"], data)

    return dumps(user, default=str)


@app.route("/api/push-subscriptions", methods=["POST"])
def create_push_subscription():
    data = request.get_json()
    db = get_database()
    print("Inside /api/push-subscriptions", data)
    user = db.users.find_one({"_id": ObjectId(data["user_id"])})
    print("Inside /api/push-subscriptions user", user)

    if user.get("push_subscription", None) is None:
        result = db.users.update_one(
            {"_id": ObjectId(data["user_id"])},
            {"$set": {"push_subscription": loads(data["subscription_json"])}},
        )
        print("Update push_subscriptions result", result)

    return dumps({"status": "success"})


def trigger_push_notifications(subscription, data):
    msg = {"title": data.get("title", ""), "body": data["body"]}
    try:
        print("Sending Push Notification", subscription)
        response = webpush(
            subscription_info=subscription,
            data=dumps(msg),
            vapid_private_key=os.getenv("VAPID_PRIVATE_KEY"),
            vapid_claims={
                "sub": "mailto:{}".format(
                    os.getenv("VAPID_CLAIM_EMAIL"))
            }
        )
        print("Successfully sent notification", response)
        return response.ok
    except WebPushException as ex:
        if ex.response and ex.response.json():
            extra = ex.response.json()
            print("Remote service replied with a {}:{}, {}",
                  extra.code,
                  extra.errno,
                  extra.message
                  )
        return False


if __name__ == "__main__":
    app.run(port=5050, debug=True)
