import unittest

from projects.calculator_core.src.calculator import Calculator

class CalculatorTestsAddMultiply(unittest.TestCase):
    def test_add(self):
        calculator = Calculator()
        result = calculator.add(2, 3)
        self.assertEqual(result, 5)

    def test_multiply(self):
        calculator = Calculator()
        result = calculator.multiply(2, 3)
        self.assertEqual(result, 6)

