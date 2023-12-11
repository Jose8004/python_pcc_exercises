import unittest
from snd_chapter_3 import merge_and_sort_lists, swap_key_value_in_dicts
 
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

class TestSwapKeyValueInDicts(unittest.TestCase):
    def test_swap_key_value(self):
        original = [{"a": 1, "b": 2}, {"x": 10, "y": 20}]
        swapped = swap_key_value_in_dicts(original)
        expected = [{1: "a", 2: "b"}, {10: "x", 20: "y"}]
        self.assertEqual(swapped, expected)
 
    def test_empty_dict_in_list(self):
        self.assertEqual(swap_key_value_in_dicts([{}, {"a": 1}]), [{}, {1: "a"}])
 
if __name__ == '__main__':
    unittest.main()