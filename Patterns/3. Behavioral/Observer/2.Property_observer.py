
class Event(list):
    # List of functions that need to be invoked whenever this event actually happens
    def __call__(self, *arg, **kwargs):
        for item in self:
            item(*arg, **kwargs)

class PropertyObservable:
    def __init__(self):
        self.property_changed = Event()

class Person(PropertyObservable):

    def __init__(self, age=0):
        super().__init__()
        self._age = age

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if self._age == value:
            return
        self._age = value
        self.property_changed('age', value)

class PersonMonitor:
    def __init__(self, person: Person):
        self.person = person
        person.property_changed(
            self.person_changed
        )
    
    def person_changed(self, name, value):
        if name == 'name':
            if value < 16:
                print('SOrry you cannot drive')
            else:
                print('Okay you can drive')
                self.person.property_changed.remove(
                    self.person_changed
                )