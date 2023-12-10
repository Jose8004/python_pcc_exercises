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

def append_to_dict_list
