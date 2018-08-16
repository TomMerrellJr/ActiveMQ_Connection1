# Program to connect to ActiveMQ broker and read messages from the FuSE.ModelOutput topic and then publish messages
# to MCITOPIC to be consumed by the phone.

import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish


import json
import time

broker = "localhost"
port = 1883

MSGDICT = {}
workload = 0


# Define the Callback
def on_message(client, userdata, msg):
    global MSGDICT
    global workload
    MSGDICT = dict(json.loads(msg.payload))
    workload = MSGDICT['outputValues']['value']
    if workload <= 33:
        publish.single("MCITOPIC", "(H) This is a sample high priority alert", 0)
        time.sleep(5)
        publish.single("MCITOPIC", "(M) This is a sample moderate priority alert", 0)
        time.sleep(5)
        publish.single("MCITOPIC", "(L) This is a sample low priority alert", 0)
    elif 33 < workload <= 67:
        publish.single("MCITOPIC", "(H) this is a sample high priority alert", 0)
        time.sleep(5)
        publish.single("MCITOPIC", "(M) This is a sample moderate priority alert", 0)
    elif workload > 67:
        publish.single("MCITOPIC", "(H) This is a sample high priority alert", 0)


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("FuSE/ModelOutput")


client = mqtt.Client()
client.connect(broker, port)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()