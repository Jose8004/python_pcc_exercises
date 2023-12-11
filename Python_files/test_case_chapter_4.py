import unittest
from chapter_4 import filter_and_square, negative_to_zero, slice_lists
 
class TestFilterAndSquare(unittest.TestCase):
    def test_filter_and_square(self):
        self.assertEqual(filter_and_square([1, 2, 3, 4, 5, 6]), [4, 16, 36])
 
    def test_empty_list(self):
        self.assertEqual(filter_and_square([]), [])
 
    def test_all_odd_numbers(self):
        self.assertEqual(filter_and_square([1, 3, 5, 7]), [])
 
if __name__ == '__main__':
    unittest.main()

class TestNegativeToZero(unittest.TestCase):
    def test_negative_to_zero(self):
        self.assertEqual(negative_to_zero([1, -2, 3, -4, 5, -6]), [1, 0, 3, 0, 5, 0])
 
    def test_no_negatives(self):
        self.assertEqual(negative_to_zero([1, 2, 3, 4]), [1, 2, 3, 4])
 
    def test_all_negatives(self):
        self.assertEqual(negative_to_zero([-1, -2, -3]), [0, 0, 0])
 
if __name__ == '__main__':
    unittest.main()

class TestSliceLists(unittest.TestCase):
    def test_slice_lists_long_list(self):
        long_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        expected = ([1, 2, 3], [5, 6, 7], [10, 11, 12])
        self.assertEqual(slice_lists(long_list), expected)
 
    def test_short_list(self):
        short_list = [1, 2, 3, 4]
        expected = ([1, 2, 3, 4],)
        self.assertEqual(slice_lists(short_list), expected)
 
    def test_empty_list(self):
        self.assertEqual(slice_lists([]), ([],))
 
if __name__ == '__main__':
    unittest.main()