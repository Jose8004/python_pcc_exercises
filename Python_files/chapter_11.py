"""
Practice Question 1: Temperature Converter
Task:
Write a function convert_to_celsius that accepts 
a temperature in Fahrenheit and converts it to 
Celsius. The function should return the temperature 
in Celsius rounded to 2 decimal places. Store the 
function in a module called temperature_conversion.py.
"""

def convert_to_celsius(farhenheit):
    celsius = (farhenheit - 32) * (5 / 9)
    return celsius

"""
Practice Question 2: String Reverser
Task:
Create a function reverse_string that 
takes a string and returns its reverse. 
The function should handle both single 
words and phrases.
Store this function in a module called 
string_operations.py.
"""

def reverse_string(string):
    try:
        reversed_str = "".join(reversed(string))
    except TypeError:
        return None
    
    return reversed_str

