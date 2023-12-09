"""
Practice Question 1: Merge and Sort Lists
Task:
Create a function merge_and_sort_lists
that takes two lists of integers. Merge
these lists and then sort the merged list
in ascending order. Return the sorted merged list."""

def merge_and_sort_lists(list1, list2):
    return sorted(list1 + list2)
