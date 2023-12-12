import random

"""
Practice Question 2: Password Change Request
Task:
Create a function password_change_request that 
prompts the user to enter a new password and then 
enter it again to confirm. The loop continues 
until both passwords match.
"""

def password_change_request():
    flag = True
    while flag:
        new_password = input("Enter new password: ")
        confirm = input("Confirm your new password: ")
        if new_password == confirm:
            print('Password successfully changed!')
            flag = False
        else:
            print('Passwords do not match. Try again.')

"""
Practice Question 1: Age Verifier
Task:
Write a function age_verifier that 
continuously asks the user for their 
age until they provide a valid age 
(a number from 1 to 120). Once a valid 
age is provided, the function should 
print a message confirming the age.
"""

def age_verifier():

    while True:
        age = input("Enter your age: ")
        for i in age:
            try:
                age[i] = int(age[i])
                break
            except ValueError:
                print("Invalid age. Please try again.")

    flag = True
    while flag or flag < len(age):
        for i in len(age):
            if 1 < int(age[i]) < 120:
                print('Your age is 25')
                flag = False
            else:
                print('Invalid age. Please try again.')
                flag += 1
                continue

"""
Practice Question 3: Interactive Number Guesser
Task:
Implement a function number_guesser that generates 
a random number between 1 and 10 and asks the user 
to guess the number. The user keeps guessing until 
they guess the correct number.
"""

def number_guesser():
    rand_num = random.randint(1, 10)
    flag = True
    while flag:
        user_num = input("Guess the number: ")
        if int(user_num) == rand_num:
            flag = False
            print(f'Correct! The number was {user_num}')
        else:
            print('Try again.')
            continue