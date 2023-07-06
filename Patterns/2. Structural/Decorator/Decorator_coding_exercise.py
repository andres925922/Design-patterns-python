"""

Decorator Coding Exercise
You are given two types, Circle and Square, and a decorator called ColoredShape.

The decorator adds the color to the string output for a given shape, just as we did in the lecture.

There's a trick though: the decorator now has a resize() method that should resize the underlying shape. However, only the Circle has a resize() method; the Square does not — do not add it!

You are asked to complete the implementation of Circle, Square and ColoredShape.

"""

class Circle:
  def __init__(self, radius):
    self.radius = radius

  def resize(self, factor):
    self.radius *= factor

  def __str__(self):
    return "A circle of radius %s" % self.radius

class Square:
  def __init__(self, side):
    self.side = side

  def __str__(self):
    return 'A square with side %s' % self.side


class ColoredShape:
  def __init__(self, shape, color):
    self.color = color
    self.shape = shape

  def resize(self, factor):
    # todo
    # note that a Square doesn't have resize()
    if isinstance(self.shape, Circle):
        self.shape.resize(factor)
    return

  def __str__(self):
    return "%s has the color %s" % (self.shape, self.color)