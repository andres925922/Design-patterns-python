"""
Factory Coding Exercise

You are given a class called Person . The person has two attributes: id , and name .

Please implement a  PersonFactory that has a non-static  create_person()  method that takes a person's name and return a person initialized with this name and an id.

The id of the person should be set as a 0-based index of the object created. So, the first person the factory makes should have Id=0, second Id=1 and so on.
"""

class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self) -> str:
        return f"{self.name}"

class PersonFactory:

    person_instances = []

    def create_person(self, name):
        # todo
        index = self.person_instances.__len__()
        person = Person(index, name)
        self.person_instances.append(person)
        return person

person_factory = PersonFactory()
person = person_factory.create_person("pela")

person2 = person_factory.create_person("lucha")

print(person, person2, person_factory.person_instances)