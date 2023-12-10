import unittest
from snd_chapter_6 import get_nested_value, append_to_dict_list
 
class TestGetNestedValue(unittest.TestCase):
    def test_get_nested_value(self):
        nested_dict = {'a': {'b': {'c': 1}}}
        keys = ['a', 'b', 'c']
        self.assertEqual(get_nested_value(nested_dict, keys), 1)
 
    def test_key_not_found(self):
        nested_dict = {'a': {'b': 2}}
        keys = ['a', 'c']
        self.assertIsNone(get_nested_value(nested_dict, keys))
 
    def test_empty_keys(self):
        nested_dict = {'a': 1}
        self.assertIsNone(get_nested_value(nested_dict, []))
 
    def test_empty_dict(self):
        self.assertIsNone(get_nested_value({}, ['a']))
 
if __name__ == '__main__':
    unittest.main()

class TestAppendToDictList(unittest.TestCase):
    def test_append_to_existing_key(self):
        dict_list = {'a': [1, 2], 'b': [3]}
        append_to_dict_list(dict_list, 'a', 4)
        self.assertEqual(dict_list, {'a': [1, 2, 4], 'b': [3]})
 
    def test_append_to_new_key(self):
        dict_list = {'a': [1, 2]}
        append_to_dict_list(dict_list, 'b', 3)
        self.assertEqual(dict_list, {'a': [1, 2], 'b': [3]})
 
    def test_empty_dict(self):
        dict_list = {}
        append_to_dict_list(dict_list, 'a', 1)
        self.assertEqual(dict_list, {'a': [1]})
 
if __name__ == '__main__':
    unittest.main()