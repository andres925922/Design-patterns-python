from random import randint

from typing import Any


class SingletonMeta(type):
     """Well, type has also a completely different ability: it can create classes on the fly. type can take the description of a class as parameters, and return a class.
     
     type works this way:

        type(name, bases, attrs)
        Where:

        name: name of the class
        bases: tuple of the parent class (for inheritance, can be empty)
        attrs: dictionary containing attributes names and values
        e.g.:

        >>> class MyShinyClass(object):
        ...       pass
        can be created manually this way:

        >>> MyShinyClass = type('MyShinyClass', (), {}) # returns a class object
        >>> print(MyShinyClass)

        What are metaclasses
        Metaclasses are the 'stuff' that creates classes.

        You define classes in order to create objects, right?

        But in Python classes are objects.

        Well, metaclasses are what create these objects. They are the classes' classes, you can picture them this way:

        MyClass = MetaClass()
        my_object = MyClass()

        You've seen that type lets you do something like this:

        MyClass = type('MyClass', (), {})

        It's because the function type is in fact a metaclass. type is the metaclass Python uses to create all classes behind the scenes.

"""
     _instances = {}

     def __call__(cls, *args: Any, **kwds: Any) -> Any:
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls) \
                                        .__call__(*args, **kwds)
        return cls._instances[cls]
        
        #   return super().__call__(*args, **kwds)


class Random_Number:

    def __init__(self) -> None:
        self.number = randint(1, 300)

    def __str__(self) -> str:
        return str(self.number)

print("No singleton class")
n1 = Random_Number()
n2 = Random_Number()

print(n1, n2, sep="\n")

class RandomNumberSingletonDecorated(metaclass = SingletonMeta):
    def __init__(self) -> None:
        self.number = randint(1, 300)

    def __str__(self) -> str:
        return str(self.number)
    
print("No singleton class")
sn1 = RandomNumberSingletonDecorated()
sn2 = RandomNumberSingletonDecorated()

print(sn1, sn2, sep="\n")