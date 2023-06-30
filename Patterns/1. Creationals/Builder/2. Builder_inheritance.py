class Person:

    def __init__(self) -> None:
        self.name = None
        self.last_name = None
        self.date_of_birth = None

    def __str__(self) -> str:
        return f"My name is {self.name} {self.last_name} and I was born in {self.date_of_birth}"

    
class PersonBuilder:

    def __init__(self) -> None:
        self.person = Person()

    def build(self):
        return self.person

class PersonNameBuilder(PersonBuilder):
    
    def called(self, name, last_name):
        self.person.name = name
        self.person.last_name = last_name
        return self
    
class PersonDateOfBirthBuilder(PersonNameBuilder):

    def set_date_of_birth(self, date):
        self.person.date_of_birth = date
        return self
    

builder = PersonDateOfBirthBuilder()
me = builder.set_date_of_birth('05-08-1991') \
            .called("Andres", "Convertini") \
            .build()

print(me)
