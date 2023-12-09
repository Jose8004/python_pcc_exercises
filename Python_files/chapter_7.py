"""
Practice Question 2: Interactive Math Quiz
Task:
Create a function math_quiz that generates a
simple arithmetic question (e.g., ‘What is 3 + 4?’).
It should ask the user for an answer and keep prompting
until the correct answer is given.

Unit Test for Interactive Math Quiz:

import unittest
from io import StringIO
from unittest.mock import patch
from math_quiz import math_quiz
 
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
"""

def math_quiz():
    flag = True
    while flag:
        answer = input('What is 5 + 2?: ')
        if int(answer) != 7:
            print('Wrong answer, try again!')
        else:
            flag = False
            print('Correct!')
            