import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Test cases for SimpleCalculator class"""

    def setUp(self):
        """Set up a calculator instance before each test"""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test addition operation with various cases"""
        # Test positive numbers
        self.assertEqual(self.calc.add(2, 3), 5)
        # Test negative numbers
        self.assertEqual(self.calc.add(-1, -1), -2)
        # Test mixed positive/negative
        self.assertEqual(self.calc.add(-5, 5), 0)
        # Test with zero
        self.assertEqual(self.calc.add(0, 7), 7)
        # Test floating point numbers
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3, places=7)

    def test_subtraction(self):
        """Test subtraction operation with various cases"""
        # Test positive numbers
        self.assertEqual(self.calc.subtract(5, 3), 2)
        # Test negative numbers
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        # Test mixed positive/negative
        self.assertEqual(self.calc.subtract(5, -3), 8)
        # Test with zero
        self.assertEqual(self.calc.subtract(0, 7), -7)
        # Test floating point numbers
        self.assertAlmostEqual(self.calc.subtract(0.3, 0.1), 0.2, places=7)

    def test_multiplication(self):
        """Test multiplication operation with various cases"""
        # Test positive numbers
        self.assertEqual(self.calc.multiply(2, 3), 6)
        # Test negative numbers
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        # Test mixed positive/negative
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        # Test with zero
        self.assertEqual(self.calc.multiply(0, 7), 0)
        # Test floating point numbers
        self.assertAlmostEqual(self.calc.multiply(0.1, 0.2), 0.02, places=7)

    def test_division(self):
        """Test division operation with various cases"""
        # Test normal division
        self.assertEqual(self.calc.divide(6, 3), 2)
        # Test floating point result
        self.assertAlmostEqual(self.calc.divide(1, 2), 0.5, places=7)
        # Test division by zero
        self.assertIsNone(self.calc.divide(5, 0))
        # Test negative numbers
        self.assertEqual(self.calc.divide(-6, 3), -2)
        # Test zero divided by number
        self.assertEqual(self.calc.divide(0, 5), 0)

if __name__ == '__main__':
    unittest.main()