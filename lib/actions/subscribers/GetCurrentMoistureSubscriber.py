from lib.Subscriber import Subscriber
from lib.SubscriberTopic import CURRENT_MOISTURE_VALUE_TOPIC

class GetCurrentMoistureSubscriber(Subscriber):
    def __init__(self, client, thing_controller):
        topic = CURRENT_MOISTURE_VALUE_TOPIC
        Subscriber.__init__(self, client, thing_controller, topic)

    def on_message(self, topic, msg):
        self.thing_controller.publish_current_moisture_value()
