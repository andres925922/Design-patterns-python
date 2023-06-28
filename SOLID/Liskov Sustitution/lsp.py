"""
Sumary

If you have some interface that takes some sort of base class, you should be able to stick a derived class in there and everything should work as expected.

"""

class Rectangle:
    def __init__(self, height, width) -> None:
        self._height = height
        self._width = width

    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        self._height = value

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        self._width = value

    @property
    def area(self):
        return self._width * self._height
    
    def __str__(self) -> str:
        return f'Width: {self.width}, Height: {self.height}'
    

# Lets create a class Square that inherits from Rectangle and breaks the LSP

class Square(Rectangle):
    def __init__(self, size) -> None:
        """ Both sides are equal """
        Rectangle.__init__(self, size, size)

    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectangle.width.setter
    def height(self, value):
        self._width = self._height = value


def use_it(rc):
    w = rc.width
    rc.height = 10  # unpleasant side effect
    expected = int(w * 10)
    print(f'Expected an area of {expected}, got {rc.area}')


rc = Rectangle(2, 3)
use_it(rc)

sq = Square(5)
use_it(sq)

# Better implementation

# class Rectangle_1:
#     def __init__(self, 
#                  height, 
#                  width, 
#                  is_square = False) -> None:
#         self._is_square = is_square
#         if(is_square and height == width):
#             self._height = self._width = height
#         else:
#             self._height = height
#             self._width = width

#     @property
#     def height(self):
#         return self._height
    
#     @height.setter
#     def height(self, value):
#         if(self._is_square): self._height = self._width = value
#         else: self._height = value

#     @property
#     def width(self):
#         return self._width
    
#     @width.setter
#     def width(self, value):
#         if(self._is_square): self._height = self._width = value
#         else: self._width = value

#     @property
#     def area(self):
#         return self._width * self._height
    
#     def __str__(self) -> str:
#         return f'Width: {self.width}, Height: {self.height}'
    
# class Square_1(Rectangle_1):

#     def __init__(self, size) -> None:
#         super().__init__(size, size, True)
