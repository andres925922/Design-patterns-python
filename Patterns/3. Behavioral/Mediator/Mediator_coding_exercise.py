"""
Mediator Coding Exercise
Our system has any number of instances of Participant  classes. Each Participant has a value integer attribute, initially zero.

A participant can say()  a particular value, which is broadcast to all other participants. At this point in time, every other participant is obliged to increase their value  by the value being broadcast.

Example:

Two participants start with values 0 and 0 respectively

Participant 1 broadcasts the value 3. We now have Participant 1 value = 0, Participant 2 value = 3

Participant 2 broadcasts the value 2. We now have Participant 1 value = 2, Participant 2 value = 3
"""

class Participant:
    def __init__(self, mediator):
        self.value = 0
        self.mediator = mediator
        self.mediator.participants.append(self)

    def say(self, value):
        # todo
        self.mediator.broadcast(self, value)

class Mediator:
    def __init__(self):
        self.participants: list[Participant] = []

    def broadcast(self, sender: Participant, value):
        for participant in self.participants:
            if participant != sender:
                participant.value += value



                

