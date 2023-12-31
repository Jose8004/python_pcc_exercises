import unittest
from io import StringIO
from unittest.mock import patch
from snd_chapter_7 import password_change_request, age_verifier, number_guesser
 
class TestPasswordChangeRequest(unittest.TestCase):
 
    @patch('builtins.input', side_effect=['password123', 'pass123', 'password123', 'password123'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_password_confirmation(self, stdout_mock, input_mock):
        password_change_request()
        output = stdout_mock.getvalue()
        self.assertIn('Passwords do not match. Try again.', output)
        self.assertIn('Password successfully changed!', output)
 
if __name__ == '__main__':
    unittest.main()

class TestAgeVerifier(unittest.TestCase):
 
    @patch('builtins.input', side_effect=['abc', '-1', '130', '25'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_valid_age(self, stdout_mock, input_mock):
        age_verifier()
        output = stdout_mock.getvalue()
        self.assertIn('Invalid age. Please try again.', output)
        self.assertIn('Your age is 25', output)
 
if __name__ == '__main__':
    unittest.main()

class TestNumberGuesser(unittest.TestCase):
 
    @patch('random.randint', return_value=5)
    @patch('builtins.input', side_effect=['3', '7', '5'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_number_guessing(self, stdout_mock, input_mock, randint_mock):
        number_guesser()
        output = stdout_mock.getvalue()
        self.assertIn('Try again.', output)
        self.assertIn('Correct! The number was 5', output)
 
if __name__ == '__main__':
    unittest.main()