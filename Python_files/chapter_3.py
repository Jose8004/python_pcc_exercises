"""Jose: 2, Fida: 1, Both: 3
Practice Question 2: Manipulate Guest List
Task:
Write a function manage_guests that simulates inviting, removing, 
and re-inviting guests. It should take a list of guests, remove 
one specified guest, add a new guest, and return the modified list.

Unit Test for Manipulate Guest List:

import unittest
from manage_guests import manage_guests
 
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
"""

def manage_guests(guests, remove, replace):
    if remove in guests:
        index = guests.index(remove)
        guests.remove(remove)
        guests.insert(index, replace)
    else:
        guests.append(replace)
    return guests

"""
Practice Question 3: Sorting and Reversing a List
Task:
Implement a function sort_and_reverse that takes a list of integers
and returns a tuple of two lists: 

the first list should be the input
list sorted in ascending order,

and the second list should be the
input list sorted in descending order.

Unit Test for Sorting and Reversing:
import unittest
from sort_and_reverse import sort_and_reverse
 
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
"""

def sort_and_reverse(list):
    sorted_asc = sorted(list)
    sorted_desc = sorted(list, reverse=True)
    print(sorted_desc)
    if not list:
        sorted_desc = []   
    return sorted_asc, sorted_desc