"""
Practice Question 1: Merge and Sort Lists
Task:
Create a function merge_and_sort_lists
that takes two lists of integers. Merge
these lists and then sort the merged list
in ascending order. Return the sorted merged list."""

def merge_and_sort_lists(list1, list2):
    return sorted(list1 + list2)

"""
Practice Question 3: List of Dictionaries – Key Value Swap
Task:
Create a function swap_key_value_in_dicts that takes a list 
of dictionaries. The function should swap keys and values in 
each dictionary and return a new list of dictionaries with 
the swapped key-value pairs.
"""

def swap_key_value_in_dicts(list_of_dicts):
    swapped_dicts = []
    for one_dict in list_of_dicts:
        new_dict = {}
        for key, value in one_dict.items():
            new_dict[value] = key
        swapped_dicts.append(new_dict)
    return swapped_dicts
        