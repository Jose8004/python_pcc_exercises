"""
Practice Question 1: Filter and Transform List
Task:
Write a function filter_and_square that takes a list of integers.
It should filter out all odd numbers and square the remaining even numbers.
Return the transformed list.

Unit Test for Filter and Transform List:

import unittest
from filter_and_square import filter_and_square
 
class TestFilterAndSquare(unittest.TestCase):
    def test_filter_and_square(self):
        self.assertEqual(filter_and_square([1, 2, 3, 4, 5, 6]), [4, 16, 36])
 
    def test_empty_list(self):
        self.assertEqual(filter_and_square([]), [])
 
    def test_all_odd_numbers(self):
        self.assertEqual(filter_and_square([1, 3, 5, 7]), [])
 
if __name__ == '__main__':
    unittest.main()
"""

def filter_and_square(int_list):
    new_list = []
    for num in int_list:
        if num % 2 == 0:
            new_list.append(num ** 2)
    return new_list

"""
Practice Question 2: List Comprehension with Conditional
Task:
Create a function negative_to_zero that uses a list comprehension
 to convert all negative numbers in a list to 0 while keeping positive
   numbers unchanged.

Unit Test for List Comprehension with Conditional:

import unittest
from negative_to_zero import negative_to_zero
 
class TestNegativeToZero(unittest.TestCase):
    def test_negative_to_zero(self):
        self.assertEqual(negative_to_zero([1, -2, 3, -4, 5, -6]), [1, 0, 3, 0, 5, 0])
 
    def test_no_negatives(self):
        self.assertEqual(negative_to_zero([1, 2, 3, 4]), [1, 2, 3, 4])
 
    def test_all_negatives(self):
        self.assertEqual(negative_to_zero([-1, -2, -3]), [0, 0, 0])
 
if __name__ == '__main__':
    unittest.main()
"""

def negative_to_zero(list_1):
    list_1 = [num if num > 0 else 0 for num in list_1]
    return list_1
