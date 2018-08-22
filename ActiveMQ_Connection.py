# Program to connect to ActiveMQ broker and read messages from the FuSE.ModelOutput topic and then publish messages
# to MCITOPIC to be consumed by the phone.

import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish


import json
import time

broker = "localhost"  # The mqtt broker location (can be changed to an IP address if so desired
port = 1883  # The mqtt broker port

MSGDICT = {}
workload = 0


# Define the Callback
def on_message(client, userdata, msg):
    global MSGDICT
    global workload
    MSGDICT = dict(json.loads(msg.payload))  # Convert the message payload to a dictionary that can be easily used.
    workload = MSGDICT['outputValues'][0]['value']  # This is where the workload value can be found in the sample output
    # This loop here can be altered to send specific messages to the MCITOPIC for the phone to display.
    if workload <= 33:
        # Send 3 sample messages for the phone to read, each 5 seconds apart
        publish.single("MCITOPIC", "(H) This is a sample high priority alert", 0)
        time.sleep(5)
        publish.single("MCITOPIC", "(M) This is a sample moderate priority alert", 0)
        time.sleep(5)
        publish.single("MCITOPIC", "(L) This is a sample low priority alert", 0)
    elif 33 < workload <= 67:
        # Send 2 sample messages for the phone to read each 5 seconds apart
        publish.single("MCITOPIC", "(H) this is a sample high priority alert", 0)
        time.sleep(5)
        publish.single("MCITOPIC", "(M) This is a sample moderate priority alert", 0)
    elif workload > 67:
        # only send the "high" priority alert for the phone to read
        publish.single("MCITOPIC", "(H) This is a sample high priority alert", 0)
    else:
        print("Cannot find the mental workload value")


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("Toolkit.DataMessage.JSON")
    publish.single("MCITOPIC", "(S)", 0)  # this will be used to sync the WAD timer with the connection of this program


client = mqtt.Client()
client.connect(broker, port)

client.on_connect = on_connect
client.on_message = on_message

time.sleep(2)

client.loop_forever()
