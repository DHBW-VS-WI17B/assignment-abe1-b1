from dataclasses import dataclass


@dataclass
class ActorMessage:
    def __init__(self, action, payload=None, customer_id=None, response_to=None):
        self.action = action
        self.payload = payload
        self.customer_id = customer_id
        self.response_to = response_to
