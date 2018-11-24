# Program to connect to ActiveMQ broker and read messages from the FuSE.ModelOutput topic and then publish messages
# to MCITOPIC to be consumed by the phone.

import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import json
import time

broker = "localhost"  # The mqtt broker location (can be changed to an IP address if so desired
port = 1883  # The mqtt broker port

WORKLOAD: int = 0


def on_message_workload(client, userdata, msg):
    global WORKLOAD
    payload = dict(json.loads(msg.payload))
    WORKLOAD = int(payload['outputValues'][0]['value'])
    print(WORKLOAD)


def on_message_skills(client, userdata, msg):
    global WORKLOAD
    print(WORKLOAD)
    print(type(WORKLOAD))
    skill_dict = json.loads(msg.payload)
    print(type(skill_dict))
    num_skills = len(skill_dict['ExpectedNextState'])
    print(num_skills)
    print(type(skill_dict['ExpectedNextState']))
    i = 0
    skills: dict = {}
    while i < num_skills:
        skills[skill_dict['ExpectedNextState'][i]['ID']] = float(skill_dict['ExpectedNextState'][i]['Value'])
        print(skills)
        i += 1
    listofkeys = list(skills.keys())
    print(listofkeys)
    msg_list = []
    i = 0
    for _ in listofkeys:
        if WORKLOAD <= 33:
            if listofkeys[i] == '2':
                print("Made it this far!!")
                if 0 <= skills[listofkeys[i]] < 2:
                    msg_list.append('(H) COP Picture')
                    print("High priority alert for skill: ", listofkeys[i])
                    i += 1
                elif 2 <= skills[listofkeys[i]] < 3.5:
                    msg_list.append('(M) COP Picture')
                    print("Med. priority alert for skill: ", listofkeys[i])
                    i += 1
                elif 3.5 <= skills[listofkeys[i]]:
                    print("Low priority alert for skill: ", listofkeys[i])
                    msg_list.append('(L) COP Picture')
                    i += 1
            elif listofkeys[i] == '3':
                if 0 <= skills[listofkeys[i]] < 2:
                    msg_list.append('(H) mIRC Chat')
                    print("High priority alert for skill: ", listofkeys[i])
                    i += 1
                elif 2 <= skills[listofkeys[i]] < 3.5:
                    msg_list.append('(M) mIRC Chat')
                    print("Med. priority alert for skill: ", listofkeys[i])
                    i += 1
                elif 3.5 <= skills[listofkeys[i]]:
                    msg_list.append('(L) mIRC Chat')
                    print("Low priority alert for skill: ", listofkeys[i])
                    i += 1
            elif listofkeys[i] == '4':
                if 0 <= skills[listofkeys[i]] < 2:
                    msg_list.append('(H) Comm. Plan')
                    print("High priority alert for skill: ", listofkeys[i])
                    i += 1
                elif 2 <= skills[listofkeys[i]] < 3.5:
                    msg_list.append('(M) Comm. Plan')
                    print("Med. priority alert for skill: ", listofkeys[i])
                    i += 1
                elif 3.5 <= skills[listofkeys[i]]:
                    msg_list.append('(L) Comm. Plan')
                    print("Low priority alert for skill: ", listofkeys[i])
                    i += 1
            elif listofkeys[i] == '5':
                if 0 <= skills[listofkeys[i]] < 2:
                    msg_list.append('(H) Comm. Standards')
                    print("High priority alert for skill: ", listofkeys[i])
                    i += 1
                elif 2 <= skills[listofkeys[i]] < 3.5:
                    msg_list.append('(M) Comm. Standards')
                    print("Med. priority alert for skill: ", listofkeys[i])
                    i += 1
                elif 3.5 <= skills[listofkeys[i]]:
                    msg_list.append('(L) Comm. Standards')
                    print("Low priority alert for skill: ", listofkeys[i])
                    i += 1
            elif listofkeys[i] == '6':
                if 0 <= skills[listofkeys[i]] < 2:
                    msg_list.append('(H) Problem Solving')
                    print("High priority alert for skill: ", listofkeys[i])
                    i += 1
                elif 2 <= skills[listofkeys[i]] < 3.5:
                    msg_list.append('(M) Problem Solving')
                    print("Med. priority alert for skill: ", listofkeys[i])
                    i += 1
                elif 3.5 <= skills[listofkeys[i]]:
                    msg_list.append('(L) Problem Solving')
                    print("Low priority alert for skill: ", listofkeys[i])
                    i += 1
            elif listofkeys[i] == '7':
                if 0 <= skills[listofkeys[i]] < 2:
                    msg_list.append('(H) Aircraft Monitoring')
                    print("High priority alert for skill: ", listofkeys[i])
                    i += 1
                elif 2 <= skills[listofkeys[i]] < 3.5:
                    msg_list.append('(M) Aircraft Monitoring')
                    print("Med. priority alert for skill: ", listofkeys[i])
                    i += 1
                elif 3.5 <= skills[listofkeys[i]]:
                    msg_list.append('(L) Aircraft Monitoring')
                    print("Low priority alert for skill: ", listofkeys[i])
                    i += 1
            elif listofkeys[i] == '8':
                if 0 <= skills[listofkeys[i]] < 2:
                    msg_list.append('(H) Mission Timeline')
                    print("High priority alert for skill: ", listofkeys[i])
                    i += 1
                elif 2 <= skills[listofkeys[i]] < 3.5:
                    msg_list.append('(M) Mission Timeline')
                    print("Med. priority alert for skill: ", listofkeys[i])
                    i += 1
                elif 3.5 <= skills[listofkeys[i]]:
                    msg_list.append('(L) Mission Timeline')
                    print("Low priority alert for skill: ", listofkeys[i])
                    i += 1
            elif listofkeys[i] == '9':
                if 0 <= skills[listofkeys[i]] < 2:
                    msg_list.append('(H) Flight Plan Routes')
                    print("High priority alert for skill: ", listofkeys[i])
                    i += 1
                elif 2 <= skills[listofkeys[i]] < 3.5:
                    msg_list.append('(M) Flight Plan Routes')
                    print("Med. priority alert for skill: ", listofkeys[i])
                    i += 1
                elif 3.5 <= skills[listofkeys[i]]:
                    msg_list.append('(L) Flight Plan Routes')
                    print("Low priority alert for skill: ", listofkeys[i])
                    i += 1
            elif listofkeys[i] == '10':
                if 0 <= skills[listofkeys[i]] < 2:
                    msg_list.append('(H) Airspace')
                    print("High priority alert for skill: ", listofkeys[i])
                    i += 1
                elif 2 <= skills[listofkeys[i]] < 3.5:
                    msg_list.append('(M) Airspace')
                    print("Med. priority alert for skill: ", listofkeys[i])
                    i += 1
                elif 3.5 <= skills[listofkeys[i]]:
                    msg_list.append('(L) Airspace')
                    print("Low priority alert for skill: ", listofkeys[i])
                    i += 1
            elif listofkeys[i] == '11':
                if 0 <= skills[listofkeys[i]] < 2:
                    msg_list.append('(H) Target Features')
                    print("High priority alert for skill: ", listofkeys[i])
                    i += 1
                elif 2 <= skills[listofkeys[i]] < 3.5:
                    msg_list.append('(M) Target Features')
                    print("Med. priority alert for skill: ", listofkeys[i])
                    i += 1
                elif 3.5 <= skills[listofkeys[i]]:
                    msg_list.append('(L) Target Features')
                    print("Low priority alert for skill: ", listofkeys[i])
                    i += 1
            elif listofkeys[i] == '12':
                if 0 <= skills[listofkeys[i]] < 2:
                    msg_list.append('(H) Theater Environment')
                    print("High priority alert for skill: ", listofkeys[i])
                    i += 1
                elif 2 <= skills[listofkeys[i]] < 3.5:
                    msg_list.append('(M) Theater Environment')
                    print("Med. priority alert for skill: ", listofkeys[i])
                    i += 1
                elif 3.5 <= skills[listofkeys[i]]:
                    msg_list.append('(L) Theater Environment')
                    print("Low priority alert for skill: ", listofkeys[i])
                    i += 1
            elif listofkeys[i] == '13':
                if 0 <= skills[listofkeys[i]] < 2:
                    msg_list.append('(H) Basic Piloting Skills')
                    print("High priority alert for skill: ", listofkeys[i])
                    i += 1
                elif 2 <= skills[listofkeys[i]] < 3.5:
                    msg_list.append('(M) Basic Piloting Skills')
                    print("Med. priority alert for skill: ", listofkeys[i])
                    i += 1
                elif 3.5 <= skills[listofkeys[i]]:
                    msg_list.append('(L) Basic Piloting Skills')
                    print("Low priority alert for skill: ", listofkeys[i])
                    i += 1
        elif 33 < WORKLOAD <= 67:
            if listofkeys[i] == '2':
                if 0 <= skills[listofkeys[i]] < 2:
                    msg_list.append('(H) COP Picture')
                    print("High priority alert for skill: ", listofkeys[i])
                    i += 1
                elif 2 <= skills[listofkeys[i]] < 3.5:
                    msg_list.append('(M) COP Picture')
                    print("Med. priority alert for skill: ", listofkeys[i])
                    i += 1
            elif listofkeys[i] == '3':
                if 0 <= skills[listofkeys[i]] < 2:
                    msg_list.append('(H) mIRC Chat')
                    print("High priority alert for skill: ", listofkeys[i])
                    i += 1
                elif 2 <= skills[listofkeys[i]] < 3.5:
                    msg_list.append('(M) mIRC Chat')
                    print("Med. priority alert for skill: ", listofkeys[i])
                    i += 1
            elif listofkeys[i] == '4':
                if 0 <= skills[listofkeys[i]] < 2:
                    msg_list.append('(H) Comm. Plan')
                    print("High priority alert for skill: ", listofkeys[i])
                    i += 1
                elif 2 <= skills[listofkeys[i]] < 3.5:
                    msg_list.append('(M) Comm. Plan')
                    print("Med. priority alert for skill: ", listofkeys[i])
                    i += 1
            elif listofkeys[i] == '5':
                if 0 <= skills[listofkeys[i]] < 2:
                    msg_list.append('(H) Comm. Standards')
                    print("High priority alert for skill: ", listofkeys[i])
                    i += 1
                elif 2 <= skills[listofkeys[i]] < 3.5:
                    msg_list.append('(M) Comm. Standards')
                    print("Med. priority alert for skill: ", listofkeys[i])
                    i += 1
            elif listofkeys[i] == '6':
                if 0 <= skills[listofkeys[i]] < 2:
                    msg_list('(H) Problem Solving')
                    print("High priority alert for skill: ", listofkeys[i])
                    i += 1
                elif 2 <= skills[listofkeys[i]] < 3.5:
                    publish.single('MCITOPIC', '(M) Problem Solving', 0)
                    msg_list('(M) Problem Solving')
                    print("Med. priority alert for skill: ", listofkeys[i])
                    i += 1
            elif listofkeys[i] == '7':
                if 0 <= skills[listofkeys[i]] < 2:
                    publish.single('MCITOPIC', '(H) Aircraft Monitoring', 0)
                    print("High priority alert for skill: ", listofkeys[i])
                    i += 1
                elif 2 <= skills[listofkeys[i]] < 3.5:
                    publish.single('MCITOPIC', '(M) Aircraft Monitoring', 0)
                    print("Med. priority alert for skill: ", listofkeys[i])
                    i += 1
            elif listofkeys[i] == '8':
                if 0 <= skills[listofkeys[i]] < 2:
                    publish.single('MCITOPIC', '(H) Mission Timeline', 0)
                    print("High priority alert for skill: ", listofkeys[i])
                    i += 1
                elif 2 <= skills[listofkeys[i]] < 3.5:
                    publish.single('MCITOPIC', '(M) Mission Timeline', 0)
                    print("Med. priority alert for skill: ", listofkeys[i])
                    i += 1
            elif listofkeys[i] == '9':
                if 0 <= skills[listofkeys[i]] < 2:
                    publish.single('MCITOPIC', '(H) Flight Plan Routes', 0)
                    print("High priority alert for skill: ", listofkeys[i])
                    i += 1
                elif 2 <= skills[listofkeys[i]] < 3.5:
                    publish.single('MCITOPIC', '(M) Flight Plan Routes', 0)
                    print("Med. priority alert for skill: ", listofkeys[i])
                    i += 1
            elif listofkeys[i] == '10':
                if 0 <= skills[listofkeys[i]] < 2:
                    publish.single('MCITOPIC', '(H) Airspace', 0)
                    print("High priority alert for skill: ", listofkeys[i])
                    i += 1
                elif 2 <= skills[listofkeys[i]] < 3.5:
                    publish.single('MCITOPIC', '(M) Airspace', 0)
                    print("Med. priority alert for skill: ", listofkeys[i])
                    i += 1
            elif listofkeys[i] == '11':
                if 0 <= skills[listofkeys[i]] < 2:
                    publish.single('MCITOPIC', '(H) Target Features', 0)
                    print("High priority alert for skill: ", listofkeys[i])
                    i += 1
                elif 2 <= skills[listofkeys[i]] < 3.5:
                    publish.single('MCITOPIC', '(M) Target Features', 0)
                    print("Med. priority alert for skill: ", listofkeys[i])
                    i += 1
            elif listofkeys[i] == '12':
                if 0 <= skills[listofkeys[i]] < 2:
                    publish.single('MCITOPIC', '(H) Theater Environment', 0)
                    print("High priority alert for skill: ", listofkeys[i])
                    i += 1
                elif 2 <= skills[listofkeys[i]] < 3.5:
                    publish.single('MCITOPIC', '(M) Theater Environment', 0)
                    print("Med. priority alert for skill: ", listofkeys[i])
                    i += 1
            elif listofkeys[i] == '13':
                if 0 <= skills[listofkeys[i]] < 2:
                    publish.single('MCITOPIC', '(H) Basic Piloting Skills', 0)
                    print("High priority alert for skill: ", listofkeys[i])
                    i += 1
                elif 2 <= skills[listofkeys[i]] < 3.5:
                    publish.single('MCITOPIC', '(M) Basic Piloting Skills', 0)
                    print("Med. priority alert for skill: ", listofkeys[i])
                    i += 1
        elif 67 < WORKLOAD:
            if listofkeys[i] == '2':
                if 0 <= skills[listofkeys[i]] < 2:
                    publish.single('MCITOPIC', '(H) COP Picture', 0)
                    print("High priority alert for skill: ", listofkeys[i])
                    i += 1
            elif listofkeys[i] == '3':
                if 0 <= skills[listofkeys[i]] < 2:
                    publish.single('MCITOPIC', '(H) mIRC Chat', 0)
                    print("High priority alert for skill: ", listofkeys[i])
                    i += 1
            elif listofkeys[i] == '4':
                if 0 <= skills[listofkeys[i]] < 2:
                    publish.single('MCITOPIC', '(H) Communication Plan', 0)
                    print("High priority alert for skill: ", listofkeys[i])
                    i += 1
            elif listofkeys[i] == '5':
                if 0 <= skills[listofkeys[i]] < 2:
                    publish.single('MCITOPIC', '(H) Communication Standards', 0)
                    print("High priority alert for skill: ", listofkeys[i])
                    i += 1
            elif listofkeys[i] == '6':
                if 0 <= skills[listofkeys[i]] < 2:
                    publish.single('MCITOPIC', '(H) Problem Solving', 0)
                    print("High priority alert for skill: ", listofkeys[i])
                    i += 1
            elif listofkeys[i] == '7':
                if 0 <= skills[listofkeys[i]] < 2:
                    publish.single('MCITOPIC', '(H) Aircraft Monitoring', 0)
                    print("High priority alert for skill: ", listofkeys[i])
                    i += 1
            elif listofkeys[i] == '8':
                if 0 <= skills[listofkeys[i]] < 2:
                    publish.single('MCITOPIC', '(H) Mission Timeline', 0)
                    print("High priority alert for skill: ", listofkeys[i])
                    i += 1
            elif listofkeys[i] == '9':
                if 0 <= skills[listofkeys[i]] < 2:
                    publish.single('MCITOPIC', '(H) Flight Plan Routes', 0)
                    print("High priority alert for skill: ", listofkeys[i])
                    i += 1
            elif listofkeys[i] == '10':
                if 0 <= skills[listofkeys[i]] < 2:
                    publish.single('MCITOPIC', '(H) Airspace', 0)
                    print("High priority alert for skill: ", listofkeys[i])
                    i += 1
            elif listofkeys[i] == '11':
                if 0 <= skills[listofkeys[i]] < 2:
                    publish.single('MCITOPIC', '(H) Target Features', 0)
                    print("High priority alert for skill: ", listofkeys[i])
                    i += 1
            elif listofkeys[i] == '12':
                if 0 <= skills[listofkeys[i]] < 2:
                    publish.single('MCITOPIC', '(H) Theater Environment', 0)
                    print("High priority alert for skill: ", listofkeys[i])
                    i += 1
            elif listofkeys[i] == '13':
                if 0 <= skills[listofkeys[i]] < 2:
                    publish.single('MCITOPIC', '(H) Basic Piloting Skills', 0)
                    print("High priority alert for skill: ", listofkeys[i])
                    i += 1

    x = 0
    k = 0
    while x < len(msg_list):
        publish.single('MCITOPIC', msg_list[k], 0)
        time.sleep(1)
        k += 1
        x += 1


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("Toolkit/DataMessage/JSON")
    client.subscribe("measure")
    publish.single("MCITOPIC", "(S)", 0)  # this will be used to sync the WAD timer with the connection of this program


client = mqtt.Client()
client.connect(broker, port)

client.on_connect = on_connect
client.message_callback_add("Toolkit/DataMessage/JSON", on_message_workload)
client.message_callback_add("measure", on_message_skills)

client.loop_forever()
