class Person:

    def __init__(self, name):
        self.name = name
        self.chat_log = []
        self.room: ChatRoom = None

    def receive(self, source, msg):
        s = f'{source}: {msg}'
        print(f'[{self.name}\'s chat session] {s}')

    def private_message(self, who, message):
        self.room.message(self.name, who, message)

    def say(self, message):
        self.room.broadcast(self.name, message=message)

class ChatRoom:

    def __init__(self):
        self.people: list[Person] = []

    def join(self, person: Person):
        join_msg = f' {person.name} has joined the room'
        self.broadcast('room', join_msg)
        person.room = self
        self.people.append(person)

    def broadcast(self, source, message):
        for p in self.people:
            if p != source:
                p.receive(source, message)

    def message(self, source, destination, message):
        for p in self.people:
            if p.name == destination:
                p.receive(source, message)

if __name__ == '__main__':
    room = ChatRoom()
    john = Person('John')
    jane = Person('Jane')

    room.join(jane)
    room.join(john)

    john.say('Hi room')
    jane.say('Hi John')

    simon = Person('Simon')
    room.join(simon)
    simon.say('Hello room')
    jane.private_message(simon, 'Hi simon.')