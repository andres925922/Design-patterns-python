# This attepmt to be a better implmentation of the point 2.

from typing import Any

def super_getattr(typ, obj, item):
    """Call this function at end of custom __getattr__ method to inherit getattr behaviour of
    parent, including expected AttributeError.  Works with new-style classes."""
    sup = super(typ, obj)
    super_get = getattr(sup, '__getattr__', sup.__getattribute__)
    return super_get(item)

class Shape:

    def __str__(self) -> str:
        return ""
    

class Circle(Shape):

    def __init__(self, rad) -> None:
        self._radius = rad

    def resize(self, factor):
        self._radius *= factor
        return self

    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, new_radius):
        self.radius = new_radius

    def __str__(self) -> str:
        return f'this is a circle of radius {self._radius}'
    
class Square(Shape):

    def __init__(self, size) -> None:
        self._size = size

    def __str__(self) -> str:
        return f'this is a square with size {self._size}'   
    

class ColoredShape:
    def __init__(self, shape, color) -> None:

        # Dupplication error in case we are using the same decorator twice
        if isinstance(shape, ColoredShape):
            raise Exception("This object has been decorated already by this decorator.")

        self._shape = shape
        self._color = color

    @property
    def shape(self):
        return self._shape

    def __iter__(self):
        return self._shape.__iter__()

    def __next__(self):
        return self._shape.__next__()
      
    def __getattr__(self, item):
        return getattr(self.__dict__['_shape'], item)

    def __str__(self) -> str:
        return f'{self._shape} and has the color {self._color}'
    
if __name__ == '__main__':

    red_circle = ColoredShape(Circle(2), 'red')
    print(red_circle.shape, red_circle.__dict__['_shape'], sep="\n")
    print(red_circle.resize(2), red_circle.radius, sep="\n")