import unittest
from chapter_2 import dynamic_greeting, generate_expressions
 
# Implement the dynamic_greeting function here
 
class TestDynamicGreeting(unittest.TestCase):
    def test_greeting(self):
        self.assertEqual(dynamic_greeting("Alice"), "Hello Alice, welcome to Python!")
        self.assertEqual(dynamic_greeting("Bob"), "Hello Bob, welcome to Python!")
 
# Additional tests can include edge cases like empty strings or non-string inputs.
 
if __name__ == '__main__':
    unittest.main()
 
class TestExpressionsGenerator(unittest.TestCase):
    def test_expression_generation(self):
        target = 8
        expressions = generate_expressions(target)
        for expr in expressions:
            self.assertEqual(eval(expr), target)
 
# Additional tests might include checking for the uniqueness of expressions, handling of zero and negative numbers, etc.
 
if __name__ == '__main__':
    unittest.main()
