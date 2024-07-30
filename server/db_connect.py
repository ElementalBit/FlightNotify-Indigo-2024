from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

def get_database():

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = os.getenv('MOONGODB_CONNECTION_STRING')

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client["indigoDB"]


def create_collections(db):
    user_validation = {
        "$jsonSchema": {
            "bsonType": "object",
            "required": [
                "name",
                "email",
                "phone_number",
                "notification_preferences",
            ],
            "properties": {
                "name": {
                    "bsonType": "string",
                    "description": "must be a string and is required",
                },
                "email": {
                    "bsonType": "string",
                    "description": "must be a string and is required",
                },
                "phone_number": {
                    "bsonType": "string",
                    "description": "must be a string and is required",
                },
                "notification_preferences": {
                    "bsonType": "object",
                    "required": ["sms", "email", "push"],
                    "properties": {
                        "sms": {
                            "bsonType": "bool",
                            "description": "must be a boolean and is required",
                        },
                        "email": {
                            "bsonType": "bool",
                            "description": "must be a boolean and is required",
                        },
                        "push": {
                            "bsonType": "bool",
                            "description": "must be a boolean and is required",
                        },
                    },
                },
                "tickets": {
                    "bsonType": "array",
                    "description": "must be a string if the field exists",
                    "items": {"bsonType": "objectId"},
                },
            },
        }
    }

    ticket_validation = {
        "$jsonSchema": {
            "bsonType": "object",
            "required": [
                "PNR",
                "user_id",
                "flight_id",
                "status",
            ],
            "properties": {
                "PNR": {
                    "bsonType": "string",
                    "description": "must be a string and is required",
                },
                "user_id": {
                    "bsonType": "objectId",
                    "description": "must be an ObjectId and is required",
                },
                "flight_id": {
                    "bsonType": "objectId",
                    "description": "must be an ObjectId and is required",
                },
                "status": {
                    "bsonType": "string",
                    "description": "must be a string and is required",
                },
            },
        }
    }

    flight_validation = {
        "$jsonSchema": {
            "bsonType": "object",
            "required": [
                "flight_number",
                "departure_time",
                "arrival_time",
                "departure_airport",
                "arrival_airport",
                "status",
            ],
            "properties": {
                "flight_number": {
                    "bsonType": "string",
                    "description": "must be a string and is required",
                },
                "departure_time": {
                    "bsonType": "date",
                    "description": "must be a date and is required",
                },
                "arrival_time": {
                    "bsonType": "date",
                    "description": "must be a date and is required",
                },
                "departure_airport": {
                    "bsonType": "string",
                    "description": "must be a string and is required",
                },
                "arrival_airport": {
                    "bsonType": "string",
                    "description": "must be a string and is required",
                },
                "passengers": {"bsonType": "array", "items": {"bsonType": "objectId"}},
                "gates": {
                    "bsonType": "string",
                },
                "status": {
                    "bsonType": "string",
                    "description": "must be a string and is required",
                },
            },
        }
    }

    # Create collections with validation
    db.create_collection("users", validator=user_validation)
    db.create_collection("tickets", validator=ticket_validation)
    db.create_collection("flights", validator=flight_validation)


# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":

    # Get the database
    db = get_database()
    create_collections(db)
