from Bridge_coding_excercise import *
from unittest import TestCase, main

class BridgeTestSuite(TestCase):

    def test_triangle_rendered_as_vector(self):
        renderer = VectorRenderer()
        triangle = Triangle(renderer=renderer)

        self.assertEqual(str(triangle), "Drawing Triangle as lines")

    def test_square_rendered_as_raster(self):
        renderer = RasterRenderer()
        square = Square(renderer=renderer)

        self.assertEqual(str(square), "Drawing Square as pixels")

if __name__ == "__main__":
    main()