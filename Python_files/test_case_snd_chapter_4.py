import unittest
from snd_chapter_4 import replace_elements
 
class TestReplaceElements(unittest.TestCase):
    def test_replace_elements(self):
        self.assertEqual(replace_elements([1, 2, 3, 2, 4], 2, 99), [1, 99, 3, 99, 4])
 
    def test_no_replacements(self):
        self.assertEqual(replace_elements([1, 2, 3, 4, 5], 6, 99), [1, 2, 3, 4, 5])
 
    def test_empty_list(self):
        self.assertEqual(replace_elements([], 2, 99), [])
 
if __name__ == '__main__':
    unittest.main()