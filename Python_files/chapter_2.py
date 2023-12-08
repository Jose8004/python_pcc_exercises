import random

"""
Jose: 1, 4 Fida: 2, 3
1. Dynamic Greeting (Combines 2-1, 2-3, 2-6)
Task: Write a Python script that assigns a person’s name to a 
variable and a greeting template to another variable. The greeting
 should be a string that expects a name to be inserted (use string
   formatting or concatenation). Initially, display the greeting 
   for the first name. Then, update the name variable to a different
     name and display the greeting again with the new name.
Key Concepts: Variable assignment, string manipulation, string formatting.

class TestDynamicGreeting(unittest.TestCase):
    def test_greeting(self):
        self.assertEqual(dynamic_greeting("Alice"), "Hello Alice, welcome to Python!")
        self.assertEqual(dynamic_greeting("Bob"), "Hello Bob, welcome to Python!")
"""

def dynamic_greeting(name):
    return f"Hello {name}, welcome to Python!"

"""
4. Mathematical Expressions Generator (Builds on 2-9)
Task: Create a Python program that generates and prints
 four unique arithmetic expressions (using addition, 
 subtraction, multiplication, division) that result in 
 a user-provided number. The expressions must use at 
 least two different numbers each (other than the target
   number) and must be generated programmatically (not 
   hard-coded). Display the expressions and their results.
Key Concepts: Arithmetic operations, loops, conditional logic,
 input handling.
These questions are designed to not only test your knowledge
 of the basics but also to push your understanding of how to
   apply these concepts in more dynamic and integrated ways.



class TestExpressionsGenerator(unittest.TestCase):
    def test_expression_generation(self):
        target = 8
        expressions = generate_expressions(target)
        for expr in expressions:
            self.assertEqual(eval(expr), target)
 
# Additional tests might include checking for the uniqueness
 of expressions, handling of zero and negative numbers, etc.
 
if __name__ == '__main__':
    unittest.main()
"""

def generate_expressions(num):
    expressions = []
    rand_int = random.randint(1, 10)
    operators = ["+", "-", "*", "/"]
    while True:
        for op in operators:
            expressions.append(f"{num} {op} {rand_int}")
        if op == "/":
            break
    return expressions