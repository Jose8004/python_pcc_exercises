import unittest
from chapter_5 import classify_grades, is_username_available
 
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