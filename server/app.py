from flask import Flask, request
from flask_cors import CORS
from db_connect import get_database
from json import dumps
from bson import ObjectId

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
    print(data)
    user = db.users.update_one(
        {"_id": ObjectId(data["user_id"])}, 
        {"$push": {
            "notifications": data["body"]
        }}
        )
    print(user)
    return dumps(user, default=str)


if __name__ == "__main__":
    app.run(port=5050, debug=True)
