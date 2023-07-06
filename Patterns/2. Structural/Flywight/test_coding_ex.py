import unittest

from Flyweight_coding_exercise import *

class TestFlyweightClass(unittest.TestCase):

    def test_first_test(self):
        frase = Sentence("Hola amigo")
        frase[1].capitalized = True
        print(frase)
        self.assertEqual(str(frase), "Hola AMIGO")

    def test_second_test(self):
        frase = Sentence("La vaca lola es mi mejor amiga")
        frase[2].capitalized = True
        frase[5].capitalized = True
        frase[6].capitalized = True
        print(frase)
        self.assertEqual(str(frase), "La vaca LOLA es mi MEJOR AMIGA")

if __name__ == '__main__':
    unittest.main()