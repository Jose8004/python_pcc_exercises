import unittest
from chapter_6 import generate_squares, count_values
 
class TestGenerateSquares(unittest.TestCase):
    def test_generate_squares(self):
        self.assertEqual(generate_squares(5), {1: 1, 2: 4, 3: 9, 4: 16, 5: 25})
 
    def test_generate_squares_empty(self):
        self.assertEqual(generate_squares(0), {})
 
    def test_generate_squares_negative(self):
        self.assertEqual(generate_squares(-3), {})
 
if __name__ == '__main__':
    unittest.main()

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