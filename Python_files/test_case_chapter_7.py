import unittest
from io import StringIO
from unittest.mock import patch
from chapter_7 import math_quiz
 
class TestMathQuiz(unittest.TestCase):
 
    @patch('builtins.input', side_effect=['9', '7'])  # First wrong, then correct
    def test_correct_answer(self, input_mock):
        with patch('sys.stdout', new_callable=StringIO) as stdout_mock:
            math_quiz()
            output = stdout_mock.getvalue()
            self.assertIn('Wrong answer, try again!', output)
            self.assertIn('Correct!', output)
 
if __name__ == '__main__':
    unittest.main()