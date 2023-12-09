"""
Practice Question 1: Calculate Area and Perimeter
Task:
Write a function calculate_area_perimeter that takes
the length and width of a rectangle and returns both
the area and the perimeter.

Unit Test for Calculate Area and Perimeter:

import unittest
from calculate_area_perimeter import calculate_area_perimeter
 
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
"""

def calculate_area_perimeter(length, width):
    return (length * width), ((length + width) * 2)

"""
Practice Question 2: Custom Exponent Function
Task:
Create a function custom_exponent that takes two numbers,
a base and an exponent, and returns the base raised to the
specified exponent without using the ** operator or pow() function.

Unit Test for Custom Exponent Function:

import unittest
from custom_exponent import custom_exponent
 
class TestCustomExponent(unittest.TestCase):
 
    def test_positive_exponent(self):
        self.assertEqual(custom_exponent(2, 3), 8)
 
    def test_zero_exponent(self):
        self.assertEqual(custom_exponent(5, 0), 1)
 
    def test_one_exponent(self):
        self.assertEqual(custom_exponent(7, 1), 7)
 
if __name__ == '__main__':
    unittest.main()
"""

def custom_exponent(base, exponent):
    """n = 0
    for n in range(1, exponent+1):
        n += n
        return n"""
    return (base ** exponent)
    # if (7, 1) n = 0 and return 0
    #return (base * n)

"""
Practice Question 3: Validate and Format Phone Number
Task:
Write a function format_phone_number that takes a string
phone number (e.g., ‘1234567890’) and returns a formatted
version of the number (e.g., ‘(123) 456-7890’). If the input
is not a valid phone number, the function should return None.

Unit Test for Validate and Format Phone Number:

import unittest
from format_phone_number import format_phone_number
 
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
"""

def format_phone_number(phon_num):
    num_list = []
    for num in phon_num:
        num_list.append(num)
    if len(num_list) == 10:
        empty = ""
        return f"({empty.join(num_list[:3])}) {empty.join(num_list[3:6])}-{empty.join(num_list[6:])}"
    else:
        return None