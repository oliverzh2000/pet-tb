from enum import Enum

class State(Enum):
    RESTING = 0
    SLEEPING = 1
    EATING = 2
    WALKING = 3


class Cat:
    def __init__(self, ):
        self.state = State.RESTING
        self.hunger = 10
        self.health = 10
        self.location = 0


