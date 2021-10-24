class Subscriber:
    """A base class for subscribers that other classes can inherit from"""

    def __init__(self, client, thing_controller, topic):
        """Constructor, taking in a mqtt client and the thing controller and a topic"""
        self.client = client
        self.thing_controller = thing_controller
        self.topic = topic

    def listen(self):
        """Call this method to subscribe to the topic"""
        print('Subscribed to topic ' + self.topic)
        self.client.subscribe(topic=self.topic)

    def on_message(self, topic, msg):
        """Perform this action when a message has been received in the topic"""
        print(topic)
        print(msg)
