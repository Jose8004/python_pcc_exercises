"""
Practice Question 1: Dictionary of Squares
Task:
Write a function generate_squares that takes
 an integer n and returns a dictionary where
   the keys are numbers from 1 to n and the 
   values are their squares.

Unit Test for Dictionary of Squares:
import unittest
from generate_squares import generate_squares
 
class TestGenerateSquares(unittest.TestCase):
    def test_generate_squares(self):
        self.assertEqual(generate_squares(5), {1: 1, 2: 4, 3: 9, 4: 16, 5: 25})
 
    def test_generate_squares_empty(self):
        self.assertEqual(generate_squares(0), {})
 
    def test_generate_squares_negative(self):
        self.assertEqual(generate_squares(-3), {})
 
if __name__ == '__main__':
    unittest.main()
"""

def generate_squares(num):
    squares_dict = {}
    for number in range(1, num+1):
        squares_dict[number] = number ** 2
    return squares_dict

"""
Practice Question 3: Dictionary Value Counter
Task:
Write a function count_values that takes a dictionary
and returns a new dictionary where each key is a value
from the input dictionary 

and the corresponding value
is the number of times that key value appeared in the
original dictionary.

Unit Test for Dictionary Value Counter:
import unittest
from count_values import count_values
 
class TestCountValues(unittest.TestCase):
    def test_count_values(self):
        input_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
        expected = {1: 2, 2: 1, 3: 1}
        self.assertEqual(count_values(input_dict), expected)
 
    def test_count_values_empty(self):
        self.assertEqual(count_values({}), {})
 
    def test_count_values_same_values(self):
        input_dict = {'a': 1, 'b': 1, 'c': 1}
        expected = {1: 3}
        self.assertEqual(count_values(input_dict), expected)
 
if __name__ == '__main__':
    unittest.main()
"""

def count_values(dict):
    count_dict = {}
    for i in dict.values():
        if i in count_dict.keys():
            count_dict[i] = count_dict[i] + 1
        else:
            count_dict[i] = 1
    return count_dict