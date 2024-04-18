import unittest

from projects.calculator_core.src.calculator import Calculator


class CalculatorTestsSubtractDivide(unittest.TestCase):

    def test_divide(self):
        calculator = Calculator()
        result = calculator.divide(6, 2)
        self.assertEqual(result, 3)

    def test_subtract(self):
        calculator = Calculator()
        result = calculator.subtract(5, 3)
        self.assertEqual(result, 2)

