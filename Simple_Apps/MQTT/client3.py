# This module subscribes to the Averages topic
# and Prints the 1 minute, 5 minute, and thirty minute average in table form
# it is dependent upon the paho mqtt library, time library, tables function
# in order to use the tables function must use pretty-tables from
# https://pypi.org/project/pretty-tables/

import paho.mqtt.client as mqtt
import time
import tables


def on_message(client, userdata, msg):
    message = msg.payload.decode()
    incoming_message.append(message)
    # print(f"Received {message} from {msg.topic} topic")


mqttBroker = "localhost"
client = mqtt.Client("Client3")
incoming_message = []
client.connect(mqttBroker)

pre_str_to_list = ''
while True:

    # client start loop and subscribe to topic "Average_Time"
    client.loop_start()
    client.subscribe("Average_Time")
    client.on_message = on_message

    # prints new table of averages only if they have changed
    new_vale = 0
    if len(incoming_message) != 0:
        new_vale = incoming_message.pop(0)
        str_to_list = new_vale.strip('][').split(', ')
        if str_to_list != pre_str_to_list:
            pre_str_to_list = str_to_list
            new_table = tables.add_to_table(str_to_list)
            print(new_table)

    time.sleep(1)
