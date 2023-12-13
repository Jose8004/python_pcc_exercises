import unittest
from snd_chapter_10 import file_stats, validate_config
 
class TestFileStats(unittest.TestCase):
    def setUp(self):
        self.filename = "sample_file.txt"
        with open(self.filename, 'w') as f:
            f.write("Hello world!\nPython is great.\n")
 
    def test_file_stats(self):
        stats = file_stats(self.filename)
        self.assertEqual(stats, {'line_count': 2, 'word_count': 5, 'char_count': 28})
 
    def test_empty_file(self):
        with open(self.filename, 'w') as f:
            pass
        stats = file_stats(self.filename)
        self.assertEqual(stats, {'line_count': 0, 'word_count': 0, 'char_count': 0})
 
    def tearDown(self):
        import os
        os.remove(self.filename)
 
if __name__ == '__main__':
    unittest.main()

class TestValidateConfig(unittest.TestCase):
    def setUp(self):
        self.valid_config = "valid_config.txt"
        self.invalid_config = "invalid_config.txt"
        with open(self.valid_config, 'w') as f:
            f.write("id: 1\nname: Test\nvalue: 123\n")
        with open(self.invalid_config, 'w') as f:
            f.write("id: 2\nname: Sample\n")
 
    def test_valid_config(self):
        self.assertTrue(validate_config(self.valid_config))
 
    def test_invalid_config(self):
        self.assertFalse(validate_config(self.invalid_config))
 
    def tearDown(self):
        import os
        os.remove(self.valid_config)
        os.remove(self.invalid_config)
 
if __name__ == '__main__':
    unittest.main()