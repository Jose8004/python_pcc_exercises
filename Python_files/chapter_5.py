"""both do nº3, nº1 Jose, nº2 Fida
Jose: 1, 3, Fida: 2, 3
Practice Question 1: Classroom Grading System
Task:
Write a function classify_grades that takes a list of student grades (as integers)
 and classifies each grade. The function should return a list of strings with 
 classifications: 
 ‘Fail’ (less than 60), 
 ‘Pass’ (60-69), 
 ‘Good’ (70-89),
  ‘Excellent’ (90-100).

Unit Test for Classroom Grading System:

import unittest
from classify_grades import classify_grades
 
class TestClassifyGrades(unittest.TestCase):
    def test_classify_grades(self):
        grades = [55, 65, 75, 95]
        expected = ['Fail', 'Pass', 'Good', 'Excellent']
        self.assertEqual(classify_grades(grades), expected)
 
    def test_empty_list(self):
        self.assertEqual(classify_grades([]), [])
 
    def test_boundary_values(self):
        grades = [59, 60, 69, 70, 89, 90, 100]
        expected = ['Fail', 'Pass', 'Pass', 'Good', 'Good', 'Excellent', 'Excellent']
        self.assertEqual(classify_grades(grades), expected)
 
if __name__ == '__main__':
    unittest.main()          
"""

def classify_grades(grades):
    if grades:
        for i in range(len(grades)):
            if isinstance(grades[i], str):
                grade = 0
            else:
                grade = grades[i]
            if grade < 60:
                grades[i] = "Fail"
            elif 60 <= grade <= 69:
                grades[i] = "Pass"
            elif 70 <= grade <= 89:
                grades[i] = "Good"
            elif 90 <= grade <= 100:
                grades[i] = "Excellent"
    return grades

"""
Practice Question 3: Check Username Availability
Task:
Write a function is_username_available that takes two lists:
current_users and new_users. The function should return a 
list of booleans indicating if each new user’s username is
available (not in current_users). The comparison should be
case insensitive.

Unit Test for Check Username Availability:

import unittest
from is_username_available import is_username_available
 
class TestIsUsernameAvailable(unittest.TestCase):
    def test_username_availability(self):
        current_users = ['admin', 'user1', 'testuser']
        new_users = ['User1', 'guest', 'Admin']
        expected = [False, True, False]  # 'User1' and 'Admin' are taken
        self.assertEqual(is_username_available(current_users, new_users), expected)
 
    def test_all_available(self):
        current_users = ['user1', 'user2']
        new_users = ['user3', 'user4']
        self.assertEqual(is_username_available(current_users, new_users), [True, True])
 
    def test_empty_new_users(self):
        self.assertEqual(is_username_available(['admin', 'user1'], []), [])
 
if __name__ == '__main__':
    unittest.main()
"""

def is_username_available(current_users, new_users):
    bools_list = ["True" if user.lower() not in current_users.lower() else "False" for user.lower() in new_users.lower()]
    
    """
    This is the expanded version
    bools_list = []
    for user in new_users:
        if user not in current_users:
            bools_list.append("True")
        else:
            bools_list.append("False")
    """

