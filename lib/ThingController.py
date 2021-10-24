from lib.MQTTClient import MQTTClient
from lib.actions.publishers.NewMoistureValuePublisher import NewMoistureValuePublisher
from lib.actions.publishers.CurrentMoisturePublisher import CurrentMoisturePublisher
from lib.actions.subscribers.GetCurrentMoistureSubscriber import GetCurrentMoistureSubscriber
from lib.sensors.MoistureSensor import MoistureSensor
import time
from lib.SubscriberTopic import CURRENT_MOISTURE_VALUE_TOPIC
import _thread

class ThingController:
    """The controller that controlls the thing, main"""

    def __init__(self):
        """Constructor that initalizes some attributes"""
        self.mqtt_client = None
        self.moisture_sensor = None
        self.new_moisture_value_publisher = None
        self.current_moisture_value_publisher = None
        self.publish_frequency_hours = 6

    def run(self):
        """To run the controller call this method, sets up MQTT and its subscribers and publishers and start a new thread to publish the current moisture value"""
        self.mqtt_client = MQTTClient(self)
        self.mqtt_client.connect()
        self.moisture_sensor = MoistureSensor()
        self.initilize_listeners_and_publisher()
        _thread.start_new_thread(self.publish_moisture_value_loop, ())
        self.mqtt_client.wait_msg()

    def initilize_listeners_and_publisher(self):
        """Initalize MQTT subscribers and publishers"""
        self.new_moisture_value_publisher = NewMoistureValuePublisher(self.mqtt_client.get_client(), self)
        self.current_moisture_value_publisher = CurrentMoisturePublisher(self.mqtt_client.get_client(), self)
        self.get_current_moisture_subscriber = GetCurrentMoistureSubscriber(self.mqtt_client.get_client(), self)
        self.get_current_moisture_subscriber.listen()

    def on_message(self, bufferTopic, bufferMsg):
        """When message is received to any topic see if it matches some topic that any subscribers are listen to and delegate to that subscriber"""
        topic = bufferTopic.decode("utf-8")
        msg = bufferMsg.decode("utf-8")
        if topic == CURRENT_MOISTURE_VALUE_TOPIC: self.get_current_moisture_subscriber.on_message(topic, msg)

    def publish_current_moisture_value(self):
        """Publish the current moisture level when called"""
        value = str(self.moisture_sensor.get_value_in_procent())
        self.current_moisture_value_publisher.publish(value)

    def publish_moisture_value_loop(self):
        """Continously publish the current moisture level in an set interval"""
        while True:
            self.new_moisture_value_publisher.publish(str(self.moisture_sensor.get_value_in_procent()))
            time.sleep(self.publish_frequency_hours * 60 * 60)
