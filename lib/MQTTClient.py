import machine
import config
import _thread
import time
import importedLibraries.mqtt
from lib.actions.subscribers.GetCurrentMoistureSubscriber import GetCurrentMoistureSubscriber
from lib.SubscriberTopic import CURRENT_MOISTURE_VALUE_TOPIC

class MQTTClient:
    def __init__(self, thing_controller):
        self.thing_controller = thing_controller

    def connect(self):
        self.mqtt_client = importedLibraries.mqtt.MQTTClient(config.DEVICE_ID, config.MQTT_HOST,user=config.MQTT_USER, password=config.MQTT_PASSWORD, port=config.MQTT_PORT)
        self.mqtt_client.set_callback(self.thing_controller.on_message)
        self.mqtt_client.connect()

    def get_client(self):
        return self.mqtt_client

    def wait_msg(self):
        while True:
            self.mqtt_client.wait_msg()
            time.sleep(1)
