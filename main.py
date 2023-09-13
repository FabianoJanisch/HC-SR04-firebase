import time
from datetime import datetime, timedelta

import firebase_admin
from firebase_admin import credentials, firestore
from pymata4 import pymata4

start_time = datetime.now()
user = 'FabianoExecFINAL'
cont = 0

#Auth Firebase
cred = credentials.Certificate("firebase-adminsdk-example.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

def send_data_firebase(name, timenow):
    # Create a new document in Firebase with name and age
    doc_ref = db.collection("people").document()
    doc_ref.set({
        "user": name,
        "time": timenow,
    })

#Inicialize HC-SR04 with trigger_pin and echo_pin
board = pymata4.Pymata4()
trigger_pin = 13
echo_pin = 12


#Send to Firebase the current time and user
def send_data():
        now = datetime.now()
        time_now = now.strftime("%H:%M")
        send_data_firebase(user, time_now)

def the_callback(data):
    global start_time, cont
    print (data[2])
    if data[2] > 60:
            time_now_2 = datetime.now()
            later_10 = (time_now_2 - start_time) >= timedelta(minutes=1)
            if later_10 or cont == 0:
                 send_data()
                 start_time = datetime.now()
                 cont += 1
                 #Data is sent and the start time is reset
                 print ('Dados enviados')

#Sensor in while
board.set_pin_mode_sonar(trigger_pin, echo_pin, the_callback)
while True:
    try:
        time.sleep(1)
        board.sonar_read(trigger_pin)
    except Exception:
        board.shutdown

