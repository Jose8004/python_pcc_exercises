from pathlib import Path

"""
Practice Question 1: File Content Reverser
Task:
Create a function reverse_file_content that 
takes a filename as its argument.

This function should read the file, reverse 
the order of the lines, and write them back 
to the same file.
"""

def reverse_file_content (file_name):
    path = Path(file_name)
    contents = path.read_text()
    lines = contents.splitlines()
    reversed_lines = reversed(lines)
    reversed_contents = '\n'.join(reversed_lines)
    path.write_text(reversed_contents)

"""
Practice Question 2: Exception Handling in Number Parsing
Task:
Write a function parse_numbers that takes a list of strings 
and returns a list of numbers. 
The function should convert each string to an integer, 
handling any ValueError exceptions for strings that cannot 
be converted.
"""

def parse_numbers (list_of_strings):
    
    list_of_ints = []

    for string in list_of_strings:
        try:
            list_of_ints.append(int(string))
        except ValueError:
            continue

    return list_of_ints


"""
Practice Question 3: File Existence Checker
Task:
Create a function check_file_existence that 
takes a filename and returns True if the file 
exists, or False if it does not. Use exception 
handling to catch the FileNotFoundError.
"""

def check_file_existence(filename):
    path = Path(filename)
    try:
        path.read_text()
        return True
    except FileNotFoundError:
        return False
        
