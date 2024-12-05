# HC-SR04 Firebase Integration

A real-time monitoring system that uses the **HC-SR04 ultrasonic sensor** and **Firebase Firestore** to collect and log proximity data automatically.

---

## Features

- **Seamless Firebase Integration**  
  Automatically logs proximity events and timestamps to Firebase Firestore in real-time.  

- **HC-SR04 Sensor Support**  
  Monitors distance using the ultrasonic sensor and triggers actions based on defined conditions.  

- **Customizable Trigger Logic**  
  The system is designed to send data only when the distance exceeds a set threshold and after specific time intervals.  

- **User-Friendly Setup**  
  Easy configuration of Firebase credentials and sensor pins for quick deployment.  

- **Modular and Scalable**  
  Built with Python, allowing seamless expansion for other sensors or additional features.  

---

## How It Works

1. **Real-Time Distance Measurement**  
   The HC-SR04 sensor continuously measures distances.  

2. **Automatic Data Logging**  
   If certain criteria are met (e.g., distance exceeds a threshold), the system logs user and timestamp data to Firebase Firestore.  

3. **Data-Driven Insights**  
   The logged data can be accessed and analyzed later for actionable insights.

---

## Quick Start Guide

### Prerequisites
- Python 3.8 or higher installed.
- Firebase project set up with Firestore enabled.
- Arduino Uno (or similar) with the HC-SR04 ultrasonic sensor.

## Steps to Run
Clone this repository:

```bash
git clone https://github.com/FabianoJanisch/HC-SR04-firebase.git
```
### Place your Firebase credentials file:
Place your 'firebase-adminsdk-example.json' in the project folder.

### Connect the HC-SR04 sensor to your Arduino:

- Trigger Pin: GPIO 13
- Echo Pin: GPIO 12
  
### Run the main Python script:
```bash
python main.py
```
## Code Overview
### Firebase Authentication
Initializes Firebase using the Admin SDK with a JSON credentials file.

### Ultrasonic Sensor Configuration
Configures the HC-SR04 sensor for real-time distance measurements using the PyMata4 library.

### Proximity Event Logging
Sends user and timestamp data to Firebase when the specified conditions are met.

## Relation to Another Project
This project is part of a larger solution, which includes a Flutter application for real-time visualization of the data collected by the system. The Flutter app communicates with Firebase to display HC-SR04 sensor readings directly on your mobile device.

You can check out the Flutter app's code in the following GitHub repository:

[Arduino Brush App (Flutter)](https://github.com/FabianoJanisch/aplicativo-arduino-brush)

## Awards 
This project was awarded 1st place in the **"PIBITI"** category at the **X Seminário de Iniciação Científica (SEMIC)**, held at Faculdade São Leopoldo Mandic in Campinas, São Paulo on October 4, 2023.





