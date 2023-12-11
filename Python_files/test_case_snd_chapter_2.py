import unittest
from snd_chapter_2 import whitespace_analyzer, transform_quote, dynamic_greeting
# Implement the whitespace_analyzer function here
 
class TestWhitespaceAnalyzer(unittest.TestCase):
    def test_whitespace_analysis(self):
        input_string = "\t  Hello World \n"
        leading, trailing, modified = whitespace_analyzer(input_string)
        self.assertEqual(leading, {' ': 2, '\t': 1})
        self.assertEqual(trailing, {' ': 1, '\n': 1})
        self.assertEqual(modified, "Hello World")
 
# Additional tests could include strings with no whitespace, only leading or trailing whitespace, etc.
 
if __name__ == '__main__':
    unittest.main()

 
class TestTransformativeQuote(unittest.TestCase):
    def test_quote_transformation(self):
        quote = "To be or not to be"
        expected = "TO_BE_OR_NOT_TO_BE21"
        self.assertEqual(transform_quote(quote), expected)
 
# Additional tests might include quotes with punctuation, very long quotes, or quotes with no spaces.
 
if __name__ == '__main__':
    unittest.main()

class TestDynamicGreeting(unittest.TestCase):
    def test_greeting(self):
        self.assertEqual(dynamic_greeting("Alice"), "Hello Alice, welcome to Python!")
        self.assertEqual(dynamic_greeting("Bob"), "Hello Bob, welcome to Python!")
 
# Additional tests can include edge cases like empty strings or non-string inputs.
 
if __name__ == '__main__':
    unittest.main()