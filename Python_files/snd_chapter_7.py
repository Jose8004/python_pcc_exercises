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
    