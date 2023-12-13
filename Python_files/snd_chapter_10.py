from pathlib import Path

"""
Practice Question 4: File Stats Analyzer
Task:
Create a function file_stats that takes a 
filename as its argument. This function 
should read the file and return a dictionary 
with the following keys: line_count (total 
number of lines), word_count (total number 
of words), and char_count (total number of 
characters).
"""

def file_stats(file_name):

    lines = Path(file_name).read_text().splitlines()
    line_count = 0
    char_count = 0
    word_count = 0

    for line in lines:
        line_count += 1
        word_count += len(line.split())
        char_count += len(line)

    dict_for_filename = {}
    dict_for_filename['line_count'] = line_count
    dict_for_filename['word_count'] = word_count
    dict_for_filename['char_count'] = char_count

    return dict_for_filename

"""
Practice Question 5: Config File Validator
Task:
Write a function validate_config that takes 
a filename of a configuration file as an 
argument.

The function should read the file 
and check for the presence of certain mandatory 
keys in each line (e.g., ‘id’, ‘name’, ‘value’). 
The function returns True if all mandatory keys 
are present in each line, otherwise False.
"""

def validate_config(file_name):
    lines = Path(file_name).read_text()
    words = lines.split()
    key_checker = 0
    for key in words:
        if key == 'id:':
            key_checker += 1
        elif key == 'name:':
            key_checker += 1
        elif key == 'value:':
            key_checker += 1

    if key_checker >= 3:
        return True
    else:
        return False
        
        