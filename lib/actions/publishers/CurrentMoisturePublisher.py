from lib.Publisher import Publisher
from lib.PublisherTopic import CURRENT_MOISTURE_VALUE_TOPIC

class CurrentMoisturePublisher(Publisher):
    def __init__(self, client, thing_controller):
        topic = CURRENT_MOISTURE_VALUE_TOPIC
        Publisher.__init__(self, client, thing_controller, topic)
