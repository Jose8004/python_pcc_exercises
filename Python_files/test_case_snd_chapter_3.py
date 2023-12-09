import unittest
from snd_chapter_3 import merge_and_sort_lists
 
class TestMergeAndSortLists(unittest.TestCase):
    def test_merge_and_sort(self):
        list1 = [3, 6, 1]
        list2 = [8, 5, 2]
        result = merge_and_sort_lists(list1, list2)
        self.assertEqual(result, [1, 2, 3, 5, 6, 8])
 
    def test_with_empty_lists(self):
        self.assertEqual(merge_and_sort_lists([], []), [])
        self.assertEqual(merge_and_sort_lists([1, 2], []), [1, 2])
        self.assertEqual(merge_and_sort_lists([], [1, 2]), [1, 2])
 
if __name__ == '__main__':
    unittest.main()