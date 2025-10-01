# This module publishes a random number between 1 and 100
# at a random time interval between 1 and 30
# it is dependent upon the paho mqtt library, time library,
# and random_numbers functions
# must use paho-mqtt from https://pypi.org/project/paho-mqtt/

import paho.mqtt.client as mqtt
import random_numbers
import time

mqttBroker = "localhost"
client = mqtt.Client("Client1")
client.connect(mqttBroker)


while True:
    random_val = random_numbers.random_input()
    random_timer = random_numbers.random_timer()

    # publish random value to topic "Random_Value"
    client.publish("Random_Value", random_val)
    print(f"Just published {random_val} to topic Random_Value")
    time.sleep(random_timer)
