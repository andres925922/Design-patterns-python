from random import randint

# singleton decorator definition. This takes a class as an argument
def singleton(class_: object):

    _instances = {} # Here we are going to store all instances to prevent if a new one is attempted to be created

    def get_instances(*args, **kwargs):
        """ This function checks if the class is an instance and if it is stored in the _intances dict
        
        If so, we return the instance, if not we create one, store it and return it 
        """
        if class_ not in _instances:
            _instances[class_] = class_(*args, **kwargs)
        
        return _instances[class_] # We return the  instance in the dictionaty
    
    # Then we return the method
    return get_instances


class Random_Number:

    def __init__(self) -> None:
        self.number = randint(1, 300)

    def __str__(self) -> str:
        return str(self.number)

print("No singleton class")
n1 = Random_Number()
n2 = Random_Number()

print(n1, n2, sep="\n")

@singleton
class RandomNumberSingletonDecorated:
    def __init__(self) -> None:
        self.number = randint(1, 300)

    def __str__(self) -> str:
        return str(self.number)
    
print("No singleton class")
sn1 = RandomNumberSingletonDecorated()
sn2 = RandomNumberSingletonDecorated()

print(sn1, sn2, sep="\n")