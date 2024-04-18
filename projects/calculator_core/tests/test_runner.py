# test_runner.py
import unittest

# Import your test cases
from projects.calculator_core.tests.test_add_multiply import CalculatorTestsAddMultiply
from projects.calculator_core.tests.test_subtract_divide import CalculatorTestsSubtractDivide

if __name__ == "__main__":
    unittest.main()
