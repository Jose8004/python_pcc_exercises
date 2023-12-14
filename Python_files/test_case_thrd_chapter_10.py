import unittest
from unittest.mock import patch
import random

from thrd_chapter_10 import robust_file_reader, safe_number_converter, database_connection_simulator

 
class TestRobustFileReader(unittest.TestCase):
    def test_read_existing_file(self):
        # Create a test file
        with open('test_file.txt', 'w') as f:
            f.write('Hello World')
        result = robust_file_reader('test_file.txt')
        self.assertEqual(result, 'Hello World')
 
    def test_file_not_found(self):
        result = robust_file_reader('nonexistent_file.txt')
        self.assertEqual(result, 'File not found error')
 
"""    def test_io_error(self):
        # Mock an IOError scenario
        with unittest.mock.patch('builtins.open', side_effect=IOError):
            result = robust_file_reader('test_file.txt')
            self.assertEqual(result, 'IO error occurred')"""
 
if __name__ == '__main__':
    unittest.main()

class TestSafeNumberConverter(unittest.TestCase):
    def test_successful_conversion(self):
        self.assertEqual(safe_number_converter(['1.5', '2.3', '3']), [1.5, 2.3, 3.0])
 
    def test_partial_failure(self):
        self.assertEqual(safe_number_converter(['4.5', 'invalid', '6']), [4.5, None, 6.0])
 
    def test_complete_failure(self):
        self.assertEqual(safe_number_converter(['not_a_number', 'nope']), [None, None])
 
if __name__ == '__main__':
    unittest.main()

class TestDatabaseConnectionSimulator(unittest.TestCase):
    def test_successful_connection(self):
        with patch('random.choice', return_value=None):
            self.assertEqual(database_connection_simulator(), 'Connected successfully')
 
    def test_connection_error(self):
        with patch('random.choice', side_effect=[ConnectionError, ConnectionError, ConnectionError]):
            self.assertEqual(database_connection_simulator(), 'Failed to connect: ConnectionError')
 
    def test_timeout_error(self):
        with patch('random.choice', side_effect=[TimeoutError, TimeoutError, TimeoutError]):
            self.assertEqual(database_connection_simulator(), 'Failed to connect: TimeoutError')
 
if __name__ == '__main__':
    unittest.main()