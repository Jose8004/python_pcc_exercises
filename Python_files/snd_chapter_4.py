"""
Practice Question 3: List Element Replacement
Task:
Write a function replace_elements that takes a
list and two values: target and replacement. Replace
all occurrences of target in the list with replacement.

without list comprehension:
    for i in range(len(list)):
        if list[i] == target:
            list[i] = replacement
    return list

list comprehension that didn't worked:
return [list[i] = replacement for i in range(len(list)) if list[i] == target]
"""

def replace_elements(list, target, replacement):
    for i in range(len(list)):
        if list[i] == target:
            list[i] = replacement
    return list

"""
Practice Question 1: Merging Sorted Lists
Task:
Write a function merge_sorted_lists that takes 
two lists of integers, both sorted in ascending 
order. Merge these two lists into a single list, 
which should also be sorted in ascending order. 
Return the merged list.
"""

def merge_sorted_lists(list_1, list_2):
    list_1 = sorted(list_1)
    list_2 = sorted(list_2)
    single_list = list_1 + list_2
    return sorted(single_list)