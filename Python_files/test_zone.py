def math_quiz():
    num_1 = input("Enter num1: ")
    num_2 = input("Enter num2: ")
    flag = True
    while flag:
        answer = input(f'What is {num_1} + {num_2}?: ')
        if answer != num_1 + num_2:
            print('Wrong answer, try again!')
        else:
            flag = False
            print('Correct!')
        return

math_quiz()