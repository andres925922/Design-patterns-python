
from enum import Enum

class Gender(Enum):
    FEMALE = 0
    MALE = 1
    NO_BINARY = 2

class Person:

    def __init__(self) -> None:
        # Adress Information
        self.street = None
        self.post_code = None
        self.city = None

        # Personal information
        self.name = None
        self.last_name = None
        self.gender = None

        # Employment information
        self.company_name = None
        self.position = None
        self.anual_income = None

    def __str__(self) -> str:
        return f"{self.name} {self.last_name} lives in {self.street} and works as {self.position} in {self.company_name} with an annual income of {self.anual_income} "


# Person builder definition
class PersonBuilder:

    def __init__(self,
                 person: Person = None) -> None:
        if person is None: self.person = Person() # If no Person instance is provided, the builder initialize a brand new one
        else: self.person = person

    def build(self):
        return self.person # Person Object return 
    
    # Builder methods
    @property
    def address(self):
        return PersonAddressBuilder(self.person)
    
    @property
    def job(self):
        return PersonJobBuilder(self.person)
    
    @property
    def personal_information(self):
        return PersonPersonalInformationBuilder(self.person)
    

# Bellow the builders definition for each particular group of caracteristics.
class PersonAddressBuilder(PersonBuilder):

    def __init__(self, person: Person) -> None:
        # In this case we must provide an instance of the person.
        super().__init__(person)

    # Setter definition
    def lives_at(self, street: str):
        self.person.street = street
        return self # We return the self object so we can chain behaviours 
    
    def with_postal_code(self, postal_code : int):
        self.person.post_code = postal_code
        return self 
        
    def in_city(self, city: str):
        self.person.city = city
        return self

class PersonJobBuilder(PersonBuilder):

    def __init__(self, person: Person) -> None:
        super().__init__(person)

    def in_comapny(self, comapny: str):
        self.person.company_name = comapny
        return self
    
    def in_position(self, position: str):
        self.person.position = position
        return self
    
    def with_annual_income(self, income: float):
        self.person.anual_income = income
        return self
    
class PersonPersonalInformationBuilder(PersonBuilder):
    def __init__(self, person: Person) -> None:
        super().__init__(person) 

    def with_name(self, name: str):
        self.person.name = name 
        return self
    
    def with_last_name(self, last_name: str):
        self.person.last_name = last_name
        return self
    
    def with_gender(self, gender: Gender):
        self.person.gender = gender
        return self

if __name__ == "__main__":
    # First we create a new builder which will create a new Person Instance if no instance provided
    # If you have a live instance and you need to update the values you will have to pass it to the builder constructor

    person_builder = PersonBuilder() # No instance provided so the builder will create it for us.

    # Dont forget to create the build methods in the builder so you can call the object functions
    # See methods under decorator @property

    # now we start to build the object

    andres_convertini = person_builder \
                            .personal_information \
                                .with_name("Andres") \
                                .with_last_name("Convertini") \
                                .with_gender(Gender.MALE) \
                            .job \
                                .in_comapny("My Own Company") \
                                .in_position("Engineer") \
                                .with_annual_income(35000) \
                            .address \
                                .in_city("Somwhere in the world") \
                                .with_postal_code(550000) \
                                .lives_at("Somewhere in the city") \
                            .build() # Dont forget to build so you get the object person.

    print(andres_convertini)

