# <img src="https://purepng.com/public/uploads/large/purepng.com-blue-paper-planepaper-planeaeroplanepaper-gliderpaper-dartaircraftfolded-paperpaperboardclipartblue-1421526589469sqfgi.png" alt="logo" width="80"/>FlightNotify
Welcome to FlightNotify, a real-time flight status update service. FlightNotify provides users with timely notifications about their flights through email, SMS, and push notifications.
## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Block Diagram](#block-diagram)
- [System Workflow](#system-workflow)
- [Screenshots](#screenshots)

## Introduction

FlightNotify is designed to keep travelers informed about their flight status in real-time. Whether you're at the airport or on the go, you can receive updates on delays, gate changes, cancellations, and more through your preferred communication channel.

## Features

- **Real-Time Updates:** Get instant alerts about flight status changes.
- **Multiple Notification Channels:** Choose to receive updates via email, SMS, or push notifications.
- **Customizable Alerts:** Filter notifications to include only the information you need.
- **User-Friendly Interface:** Easy to navigate and manage your flight alerts.

## Technologies Used

FlightNotify is built using a combination of modern technologies to ensure reliability, scalability, maintainability and ease of use.

- **Backend:**
  - **Python:** Core programming language for the backend.
  - **Flask:** Micro web framework for building the API. Port=5000 and 5050
  - **Kafka:** Distributed event streaming platform for real-time data processing. Port=9092

- **Frontend:**
  - **React:** JavaScript library for building user interfaces. Port5173
  - **HTML:** Standard markup language used for creating and structuring content on the web.
  - **Tailwind CSS:** CSS framework for responsive design.

- **Notifications:**
  - **Twilio:** API service for sending SMS notifications.
  - **SMTPlib:** Library for sending email notifications.

- **Database:**
  - **MongoDB:** NoSQL Database to store user, ticket and flight related data.

### Packages with versions
#### Python
```python
Package            Version
------------------ --------
Flask              3.0.3
Flask-Cors         4.0.1
kafka-python       2.0.2
pip                24.1.2
PyJWT              2.8.0
pymongo            4.8.0
requests           2.32.3
twilio             9.2.3
```

## Block Diagram
![alt text](documents/diagram.png)

## System Workflow
- **Simulating Flight Updates:**
    - The airport announces a flight update by sending a request to the producer server.
    - The producer server publishes the flight update to the flight-update topic in Kafka.

- **Consuming Flight Updates:**
    - A consumer reads the update from the flight-update topic.
    - The consumer queries the concerned passengers for the current update.
    - The consumer bundles the recipient data with the flight update message.
    - The consumer sends this bundled information to the producer server.
    
- **Publishing to Corresponding Topics:**
    - The producer publishes the bundled requests to the corresponding topics in Kafka (e.g., email requests to the email topic).

- **Delivering Updates:**
    - The respective servers (email-server, sms-server, push-notification-server) consume these messages.
    - Each server delivers the update via its respective medium.

## Screenshots
![alt text](documents/postman_request_flight-status.jpg)
![alt text](documents/zookeper+kafka.jpg)
![alt text](documents/db_users_collection.jpg)
![alt text](documents/db_tickets_collections.jpg)
![alt text](documents/db_flights_collections.jpg)
![alt text](documents/email_notification_anant.jpg)
![alt text](documents/sms_notification_radhika.jpg)
![alt text](documents/frontend_home.jpg)
![alt text](documents/frontend_my-trips.jpg)
![alt text](documents/frontend_notifications.jpg)
![alt text](documents/frontend_notifications_radhika.jpg)
![alt text](documents/frontend_login.jpg)