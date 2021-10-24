class Publisher:
    """A base class publisher that other class can inherit from"""

    def __init__(self, client, thing_controller, topic):
        """Constructor"""
        self.client = client
        self.thing_controller = thing_controller
        self.topic = topic

    def publish(self, data):
        """Publish to the topic for the publisher"""
        self.client.publish(topic=self.topic, msg=data)
