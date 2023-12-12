import unittest
import os
from chapter_10 import reverse_file_content, parse_numbers, check_file_existence
 
class TestReverseFileContent(unittest.TestCase):
    def setUp(self):
        self.filename = "test_file.txt"
        with open(self.filename, 'w') as f:
            f.write("Line 1\nLine 2\nLine 3")
 
    def test_reverse_file_content(self):
        reverse_file_content(self.filename)
        with open(self.filename, 'r') as f:
            content = f.read()
        self.assertEqual(content, "Line 3\nLine 2\nLine 1")
 
    def test_empty_file(self):
        with open(self.filename, 'w') as f:
            pass
        reverse_file_content(self.filename)
        with open(self.filename, 'r') as f:
            content = f.read()
        self.assertEqual(content, "")
 
if __name__ == '__main__':
    unittest.main()

class TestParseNumbers(unittest.TestCase):
    def test_parse_numbers(self):
        self.assertEqual(parse_numbers(["1", "2", "3"]), [1, 2, 3])
 
    def test_parse_with_non_numbers(self):
        self.assertEqual(parse_numbers(["4", "five", "6"]), [4, 6])
 
    def test_parse_empty_list(self):
        self.assertEqual(parse_numbers([]), [])
 
if __name__ == '__main__':
    unittest.main()

class TestCheckFileExistence(unittest.TestCase):
    def setUp(self):
        self.existing_file = "existing_file.txt"
        with open(self.existing_file, 'w') as f:
            f.write("This is a test file.")
 
    def test_existing_file(self):
        self.assertTrue(check_file_existence(self.existing_file))
 
    def test_non_existing_file(self):
        self.assertFalse(check_file_existence("non_existing_file.txt"))
 
    def tearDown(self):
        os.remove(self.existing_file)
 
if __name__ == '__main__':
    unittest.main()