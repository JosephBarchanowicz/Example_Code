# This module subscribes to the Random Number topic
# and publishes the 1 minute, 5 minute, and thirty minute average
# it is dependent upon the paho mqtt library, time library, datetime library
# and average classes

import paho.mqtt.client as mqtt
from averages import OneMinute, FiveMinute, ThirtyMinute
from datetime import datetime
import time
incoming_message = []


def on_message(client, userdata, msg):
    message = msg.payload.decode()
    incoming_message.append(message)
    print(f"Received {message} from {msg.topic} topic")


mqttBroker = "localhost"
client = mqtt.Client("Client2")
client.connect(mqttBroker)

# making average minute objects
one_min = OneMinute()
five_min = FiveMinute()
thirty_min = ThirtyMinute()

# initially set all values minute values to 0 and previous average to null
ave_vales = [0, 0, 0]
pre_average = ""

while True:

    # client start loop and subscribe to topic "Random_Value"
    client.loop_start()
    client.subscribe("Random_Value")
    client.on_message = on_message

    # if new incoming message, type cast to int in variable new_val
    new_val = 0
    if len(incoming_message) != 0:
        new_val = int(incoming_message.pop(0))

        # one minute averages calculation
        one_min.add_value(new_val)
        if one_min.check_time() <= datetime.now():
            ave_vales[0] = one_min.get_average()
            one_min.reset()

        # five minute averages calculation
        five_min.add_value(new_val)
        if five_min.check_time() <= datetime.now():
            ave_vales[1] = five_min.get_average()
            five_min.reset()

        # thirty minute averages calculation
        thirty_min.add_value(new_val)
        if thirty_min.check_time() <= datetime.now():
            ave_vales[2] = thirty_min.get_average()
            thirty_min.reset()

        averages = str([ave_vales[0], ave_vales[1], ave_vales[2]])

        # Publish averages to topic "Average_Time" only if they have changed
        if averages != pre_average:
            pre_average = averages
            client.publish("Average_Time", averages)
            print(f"Just published {averages} to Topic temp2")
    time.sleep(1)
