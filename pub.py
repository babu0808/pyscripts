# # pub.py
# import paho.mqtt.client as mqtt

# # MQTT Broker details
# broker = "localhost"  # Local Mosquitto broker
# port = 1883
# topic = "meter/data"  # MQTT topic to publish DLMS data

# # Callback for when the client publishes data
# def on_publish(client, userdata, mid):
#     print(f"Data published to topic: {topic}")

# # Create MQTT client instance
# client = mqtt.Client()

# # Assign the on_publish callback function
# client.on_publish = on_publish

# # Connect to the broker
# client.connect(broker, port)

# # Publish a message (this could be replaced by actual meter data in the future)
# message = "Reading meter data from Gurux DLMS stack"
# result = client.publish(topic, message)

# # Wait to make sure the message is delivered
# client.loop_start()
# client.loop_stop()

# print(f"Message sent: {message}")




import paho.mqtt.client as mqtt
import time

# MQTT Broker details
broker = "localhost"
port = 1883
topic = "meter/data"  # MQTT topic to publish DLMS data

# Callback for when the client publishes data
def on_publish(client, userdata, mid):
    print(f"Data published to topic: {topic}")

# Create MQTT client instance
client = mqtt.Client()

# Assign the on_publish callback function
client.on_publish = on_publish

# Connect to the broker
client.connect(broker, port)

# Publish a message with the retain flag
message = "sending from pub"
result = client.publish(topic, message, retain=True)  # Retain flag set to True

# Start the loop to allow message delivery
client.loop_start()

# Wait for a few seconds to ensure message is processed
time.sleep(2)

client.loop_stop()

print(f"Message sent: {message}")
