import unittest
from snd_chapter_4 import replace_elements, merge_sorted_lists
 
class TestReplaceElements(unittest.TestCase):
    def test_replace_elements(self):
        self.assertEqual(replace_elements([1, 2, 3, 2, 4], 2, 99), [1, 99, 3, 99, 4])
 
    def test_no_replacements(self):
        self.assertEqual(replace_elements([1, 2, 3, 4, 5], 6, 99), [1, 2, 3, 4, 5])
 
    def test_empty_list(self):
        self.assertEqual(replace_elements([], 2, 99), [])
 
if __name__ == '__main__':
    unittest.main()


class TestMergeSortedLists(unittest.TestCase):
    def test_merge_sorted_lists(self):
        list1 = [1, 3, 5]
        list2 = [2, 4, 6]
        self.assertEqual(merge_sorted_lists(list1, list2), [1, 2, 3, 4, 5, 6])
 
    def test_empty_lists(self):
        self.assertEqual(merge_sorted_lists([], []), [])
 
    def test_one_empty_list(self):
        self.assertEqual(merge_sorted_lists([1, 2, 3], []), [1, 2, 3])
 
if __name__ == '__main__':
    unittest.main()