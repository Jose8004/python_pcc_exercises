import unittest
from chapter_8 import calculate_area_perimeter, custom_exponent, format_phone_number
 
class TestCalculateAreaPerimeter(unittest.TestCase):
 
    def test_area_perimeter(self):
        area, perimeter = calculate_area_perimeter(5, 3)
        self.assertEqual(area, 15)
        self.assertEqual(perimeter, 16)
 
    def test_zero_values(self):
        area, perimeter = calculate_area_perimeter(0, 5)
        self.assertEqual(area, 0)
        self.assertEqual(perimeter, 10)
 
if __name__ == '__main__':
    unittest.main()

class TestCustomExponent(unittest.TestCase):
 
    def test_positive_exponent(self):
        self.assertEqual(custom_exponent(2, 3), 8)
 
    def test_zero_exponent(self):
        self.assertEqual(custom_exponent(5, 0), 1)
 
    def test_one_exponent(self):
        self.assertEqual(custom_exponent(7, 1), 7)
 
if __name__ == '__main__':
    unittest.main()

class TestFormatPhoneNumber(unittest.TestCase):
 
    def test_valid_phone_number(self):
        formatted = format_phone_number("1234567890")
        self.assertEqual(formatted, "(123) 456-7890")
 
    def test_invalid_phone_number(self):
        self.assertIsNone(format_phone_number("12345"))
 
    def test_non_numeric_phone_number(self):
        self.assertIsNone(format_phone_number("abcd"))
 
if __name__ == '__main__':
    unittest.main()