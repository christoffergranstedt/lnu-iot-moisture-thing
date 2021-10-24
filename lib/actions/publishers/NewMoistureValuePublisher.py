from lib.Publisher import Publisher
from lib.PublisherTopic import NEW_MOISTURE_VALUE_TOPIC

class NewMoistureValuePublisher(Publisher):
    def __init__(self, client, thing_controller):
        topic = NEW_MOISTURE_VALUE_TOPIC
        Publisher.__init__(self, client, thing_controller, topic)
