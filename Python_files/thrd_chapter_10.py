from pathlib import Path
import random
import time

"""
Practice Question 1: Robust File Reader
Task:
Create a function robust_file_reader that 
takes a filename as its argument. This 
function should attempt to read and return 
the contents of the file. If the file does 
not exist, it should handle the FileNotFoundError 
and return an appropriate error message. 
Additionally, if an IOError occurs, it should be 
handled separately with a different error message.
"""

def robust_file_reader(file_name):
    path = Path(file_name)
    try:
        contents = path.read_text()
    except FileNotFoundError:
        return 'File not found error'
    except IOError:
        return 'IO error occurred'
    
    return contents

"""
Practice Question 2: Safe Number Converter
Task:
Write a function safe_number_converter that 
takes a list of strings and attempts to convert 
each to a floating-point number. If a conversion 
fails due to a ValueError, it should store None 
for that item. Return the list of converted values.
"""
    
def safe_number_converter(list_of_strings):
    list_of_floats = []
    for string in list_of_strings:
        try:
            list_of_floats.append(float(string))
        except ValueError:
            list_of_floats.append(None)
    return list_of_floats

"""
Practice Question 3: Database Connection Simulator
Task:
Create a function database_connection_simulator that 
simulates a database connection. The function should 
randomly raise either a ConnectionError or a TimeoutError. 
Implement a retry mechanism that retries the connection 
up to three times before giving up and returning an 
appropriate message for the type of exception raised.
"""

def database_connection_simulator():
    rand_num = random.randint(1, 2)
    max_retries = 3
    connect_error = 1
    time_error = 2

    for i in range(max_retries):
        if rand_num == 1:
                raise ConnectionError
        if rand_num == 2:
                raise TimeoutError
        time.sleep(1)
    if rand_num
    raise Exception()
