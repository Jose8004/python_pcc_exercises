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