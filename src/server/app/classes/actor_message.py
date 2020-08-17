"""ActorMessage
"""
class ActorMessage:
    """Messageobject to communicate between client and server
    """
    def __init__(self, action, payload):
        self.action = action
        self.payload = payload
