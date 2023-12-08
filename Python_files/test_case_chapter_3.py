import unittest
from chapter_3 import manage_guests, sort_and_reverse
 
class TestManageGuests(unittest.TestCase):
    def test_guest_replacement(self):
        guests = ["Alice", "Bob", "Charlie"]
        self.assertEqual(
            manage_guests(guests, "Bob", "Diana"),
            ["Alice", "Diana", "Charlie"]
        )
 
    def test_guest_replacement_not_in_list(self):
        guests = ["Alice", "Charlie"]
        self.assertEqual(
            manage_guests(guests, "Bob", "Diana"),
            ["Alice", "Charlie", "Diana"]  # Assuming we add Diana even if Bob wasn't found
        )
 
if __name__ == '__main__':
    unittest.main()

class TestSortAndReverse(unittest.TestCase):
    def test_sort_and_reverse(self):
        numbers = [3, 1, 4, 1, 5, 9, 2]
        sorted_asc, sorted_desc = sort_and_reverse(numbers)
        self.assertEqual(sorted_asc, [1, 1, 2, 3, 4, 5, 9])
        self.assertEqual(sorted_desc, [9, 5, 4, 3, 2, 1, 1])
 
    def test_empty_list(self):
        self.assertEqual(sort_and_reverse([]), ([], []))
 
if __name__ == '__main__':
    unittest.main()