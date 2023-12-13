"""
Practice Question 2: Determine Shipping Cost
Task:
Create a function calculate_shipping_cost
that takes the weight of a package (in kilograms)
and calculates the shipping cost.
If the weight is
up to 2 kg, the cost is $5. For each additional kg,
the cost increases by $2.
"""

def calculate_shipping_cost(weight):
    if weight <= 2:
        return 5
    else:
        return 5 + (2 * (weight - 2))
    
"""
Practice Question 1: Validate Password Strength
Task:
Write a function validate_password_strength that 
takes a string (password) and checks its strength. 

A password is considered ‘Strong’ if it has at 
least 8 characters, contains both uppercase and 
lowercase letters, and has at least one number. 

Otherwise, it’s ‘Weak’.
"""

def validate_password_strength(password):

    has_upper = False
    has_lower = False
    is_digit = False

    if len(password) >= 8:
        for i in range(len(password)):
            if password[i].isupper():
                has_upper = True
            if password[i].islower():
                has_lower = True
            if password[i].isdigit():
                is_digit = True
                
    if has_upper and has_lower and is_digit:
        return 'Strong'
    else:
        return 'Weak'