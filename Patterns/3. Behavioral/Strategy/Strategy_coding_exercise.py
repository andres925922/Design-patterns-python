"""
Strategy Coding Exercise
Consider the quadratic equation and its canonical solution:

a*x2+b*x+c = 0
x = -b +/- (b2 - 4*a*c)2 / 2*a


The part b^2-4*a*c is called the discriminant. Suppose we want to provide an API with two different strategies for calculating the discriminant:

In OrdinaryDiscriminantStrategy , If the discriminant is negative, we return it as-is. This is OK, since our main API returns Complex  numbers anyway.

In RealDiscriminantStrategy , if the discriminant is negative, the return value is NaN (not a number). NaN propagates throughout the calculation, so the equation solver gives two NaN values. In Python, you make such a number with float('nan').

Please implement both of these strategies as well as the equation solver itself. With regards to plus-minus in the formula, please return the + result as the first element and - as the second. Note that the solve() method is expected to return complex values.
"""

from abc import ABC, abstractmethod
from math import exp2, sqrt, isnan
import cmath

from unittest import TestCase, main


class DiscriminantStrategy(ABC):
    @abstractmethod
    def calculate_discriminant(self, a, b, c):
        pass


class OrdinaryDiscriminantStrategy(DiscriminantStrategy):
    """
    In OrdinaryDiscriminantStrategy , If the discriminant is negative, we return it as-is. This is OK, since our main API returns Complex  numbers anyway.
    """
    def calculate_discriminant(self, 
                               a: float | int, 
                               b: float | int, 
                               c: float | int) -> float | int:
        
        return float(exp2(b) - 4*a*c)


class RealDiscriminantStrategy(DiscriminantStrategy):
    """
    In RealDiscriminantStrategy , if the discriminant is negative, the return value is NaN (not a number). NaN propagates throughout the calculation, so the equation solver gives two NaN values. In Python, you make such a number with float('nan').
    """
    def calculate_discriminant(self, 
                               a: float | int, 
                               b: float | int, 
                               c: float | int):
        calc = exp2(b) - 4*a*c
        return float('nan') if calc < 0 else calc
        # if calc < 0:
        #     return float('nan')
        
        # return calc


class QuadraticEquationSolver:
    def __init__(self, strategy: DiscriminantStrategy):
        self.strategy = strategy

    def solve(self, a, b, c):
        """ Returns a pair of complex (!) values """
        # todo
        discriminant = complex(self.strategy.calculate_discriminant(a,b,c), 0)
        return (
            (-b + sqrt(discriminant)) / (2 * a), (-b - sqrt(discriminant)) / (2 * a)
        )
    
class Evaluate(TestCase):
    def test_positive_ordinary(self):
        strategy = OrdinaryDiscriminantStrategy()
        solver = QuadraticEquationSolver(strategy)
        results = solver.solve(1, 10, 16)
        self.assertEqual(complex(-2, 0), results[0])
        self.assertEqual(complex(-8, 0), results[1])

    def test_positive_real(self):
        strategy = RealDiscriminantStrategy()
        solver = QuadraticEquationSolver(strategy)
        results = solver.solve(1, 10, 16)
        self.assertEqual(complex(-2, 0), results[0])
        self.assertEqual(complex(-8, 0), results[1])

    def test_negative_ordinary(self):
        strategy = OrdinaryDiscriminantStrategy()
        solver = QuadraticEquationSolver(strategy)
        results = solver.solve(1, 4, 5)
        self.assertEqual(complex(-2, 1), results[0])
        self.assertEqual(complex(-2, -1), results[1])

    def test_negative_real(self):
        strategy = RealDiscriminantStrategy()
        solver = QuadraticEquationSolver(strategy)
        results = solver.solve(1, 4, 5)
        self.assertTrue(isnan(results[0].real))
        self.assertTrue(isnan(results[1].real))
        self.assertTrue(isnan(results[0].imag))
        self.assertTrue(isnan(results[1].imag))

if __name__ == '__main__':
    main()