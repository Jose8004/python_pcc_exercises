import random

def generate_expressions(num):
    expressions = []
    rand_int = random.randint(1, 10)
    operators = ["+", "-", "*", "/"]
    while True:
        for op in operators:
            expressions.append(f"{num} {op} {rand_int}")
        if op == "/":
            break
    print(expressions)
    return expressions

generate_expressions(9)