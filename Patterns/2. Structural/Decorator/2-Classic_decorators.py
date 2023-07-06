# Copyright (c) 2023 Andres Convertini
#
# -*- coding:utf-8 -*-
# @Script: 2-Classic_decorators.py
# @Author: Andres Convertini
# @Email: andres.convertini91@gmail.com
# @Create At: 2023-07-06 06:37:44
# @Last Modified By: Andres Convertini
# @Last Modified At: 2023-07-06 06:38:18
# @Description: This is description.

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
    

class ColoredShape(Shape):
    def __init__(self, shape, color) -> None:

        # Dupplication error in case we are using the same decorator twice
        if isinstance(shape, ColoredShape):
            raise Exception("This object has been decorated already by this decorator.")

        self._shape = shape
        self._color = color

    @property
    def shape(self):
        return self._shape

    def __str__(self) -> str:
        return f'{self._shape} and has the color {self._color}'
    
if __name__ == '__main__':

    circle = Circle(2)
    red_circle = ColoredShape(circle, "red")
    print(red_circle, circle, sep='\n')
    red_circle_radius = red_circle.shape.radius
    print(red_circle_radius)

    # Try to resize the circle
    red_circle_radius = red_circle.shape.resize(2).radius
    print(red_circle_radius)