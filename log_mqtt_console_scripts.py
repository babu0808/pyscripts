# Note : just a sample, not tested and cannot use as it is
# Developer : Babu Malagaveli

import paho.mqtt.client as mqtt
from datetime import datetime
import ssl

# Configuration
BROKER_ADDRESS = "nms.bcits.in"
BROKER_PORT = 9002
MQTT_USERNAME = "mqttmasteruser"
MQTT_PASSWORD = "TaX7sz6Ql3ZdyqkWzu7FQkSiBTU"  # 🔒 Replace with actual password
TOPIC = "#"  # Subscribe to all topics
LOG_FILE = "wirepas_mqtt_secure_logs.txt"

# Callback when the client connects
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Connected to broker.")
        client.subscribe(TOPIC)
    else:
        print(f"❌ Failed to connect, return code {rc}")

# Callback when a message is received
def on_message(client, userdata, msg):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    payload_hex = msg.payload.hex(' ')
    log_entry = f"[{timestamp}] Topic: {msg.topic}\nPayload: {payload_hex}\n\n"
    print(log_entry.strip())

    with open(LOG_FILE, "a") as file:
        file.write(log_entry)

# Setup client
client = mqtt.Client()
client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
client.tls_set(cert_reqs=ssl.CERT_NONE)
client.tls_insecure_set(True)  # Accept self-signed or insecure certs

client.on_connect = on_connect
client.on_message = on_message

# Connect and start loop
try:
    print("🔄 Connecting to MQTT broker...")
    client.connect(BROKER_ADDRESS, BROKER_PORT, keepalive=60)
    client.loop_forever()
except Exception as e:
    print(f"💥 Error: {e}")
