from dataclasses import dataclass


@dataclass
class ActorMessage:
    def __init__(self, action, payload):
        self.action = action
        self.payload = payload
