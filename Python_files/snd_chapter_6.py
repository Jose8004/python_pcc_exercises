"""
Practice Question 3: Nested Dictionary Access
Task:
Implement a function get_nested_value that takes
a nested dictionary and a list of keys. The function 
should return the value located by following the 
sequence of keys in the nested dictionary. If any 
key is not found at any level, return None.
"""

def check_all_keys(nested_dict, key_list):
    for key in key_list:
        if key not in nested_dict:
            return False
        if isinstance(nested_dict[key], dict):
            if not check_all_keys(nested_dict[key], key_list[1:]):
                return False
    return True
    
def get_nested_value(nested_dict, key_list):
    for key1, value1 in nested_dict.items():
        if check_all_keys(nested_dict, key_list) == False:
            return None
        elif isinstance(value1, dict):
                for value2 in value1.values():
                    if isinstance(value2, dict):
                        for value3 in value2.values():
                            return value3
                    else:
                        return value2
        elif key1 in nested_dict:
                for i in range(len(key_list)):
                    return nested_dict[key_list[i]]

"""def get_nested_value(nested_dict, key_list):
    if len(key_list) == 1:
        return nested_dict.get(key_list[0])
    else:
        return get_nested_value(nested_dict.get(key_list[0], {}), key_list[1:])"""


"""
Practice Question 2: Dictionary of Lists Append
Task:
Write a function append_to_dict_list that takes 
a dictionary (where each key is associated with a 
list), a key, and a value. The function should 
append the value to the list corresponding to the 
key. If the key does not exist in the dictionary, 
add a new key with the value in a list.
"""

def append_to_dict_list(dict1, key1, val1):
    if key1 in dict1.keys():
        dict1[key1].append(val1)
    else:
        dict1[key1] = [val1]
    return dict1 

"""
Practice Question 1: Dictionary Key Reversal
Task:
Create a function reverse_dictionary that takes 
a dictionary and returns a new dictionary where 
the keys and values are swapped. 
If the original 
dictionary has duplicate values, only one of the 
corresponding keys should be preserved in the 
new dictionary.
"""

def reverse_dictionary(dict_x):
    new_dict = {}
    for key, value in dict_x.items():
        if isinstance(value, dict):
            new_dict[key] = reverse_dictionary(value)
        else:
            new_dict[value] = key
    
    return new_dict
