import paho.mqtt.client as mqtt
import json
from config import THINGSBOARD_TOKEN, THINGSBOARD_HOST

class ThingsBoardClient:
    def __init__(self):
        self.client = mqtt.Client()
        self.client.username_pw_set(THINGSBOARD_TOKEN)
        self.client.connect(THINGSBOARD_HOST, 1883, 60)

    def publish(self, temp, hum):
        payload = json.dumps({
            "temperature": temp,
            "humidity": hum
        })
        self.client.publish('v1/devices/me/telemetry', payload)
