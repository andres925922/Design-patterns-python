from unittest import TestCase, main

from Decorator_coding_exercise import ColoredShape, Circle, Square

class Evaluate(TestCase):
    def test_circle(self):
        circle = ColoredShape(Circle(5), 'red')
        self.assertEqual(
        'A circle of radius 5 has the color red',
        str(circle)
        )
        circle.resize(2)
        self.assertEqual(
        'A circle of radius 10 has the color red',
        str(circle)
        )
    
    def test_square(self):
       square = ColoredShape(Square(3), 'blue')
       self.assertEqual(
          'A square with side 3 has the color blue',
          str(square)
       )



if __name__ == '__main__':
  main()
