import unittest


class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add_two_numbers(self):
        self.assertEqual(self.calculator.add(10, 5), 15)

    def test_subtract_two_numbers(self):
        self.assertEqual(self.calculator.subtract(10, 5), 5)

    def test_multiply_two_numbers(self):
        self.assertEqual(self.calculator.multiply(10, 5), 50)

    def test_divide_two_numbers(self):
        self.assertEqual(self.calculator.divide(10, 5), 2)

    def test_divide_by_zero_raises_error(self):
        with self.assertRaises(ValueError):
            self.calculator.divide(10, 0)

    def test_calculator_supports_float_values(self):
        self.assertEqual(self.calculator.add(2.5, 3.5), 6.0)
        self.assertEqual(self.calculator.multiply(1.5, 4), 6.0)


if __name__ == "__main__":
    unittest.main()
