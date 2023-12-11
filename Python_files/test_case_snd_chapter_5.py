import unittest
from snd_chapter_5 import calculate_shipping_cost, validate_password_strength
class TestCalculateShippingCost(unittest.TestCase):
    def test_small_package(self):
        self.assertEqual(calculate_shipping_cost(1), 5)
 
    def test_medium_package(self):
        self.assertEqual(calculate_shipping_cost(5), 11) # 5 + 2*3
 
    def test_large_package(self):
        self.assertEqual(calculate_shipping_cost(10), 21) # 5 + 2*8
 
    def test_zero_weight(self):
        self.assertEqual(calculate_shipping_cost(0), 5)
 
if __name__ == '__main__':
    unittest.main()

class TestValidatePasswordStrength(unittest.TestCase):
    def test_strong_password(self):
        self.assertEqual(validate_password_strength('StrongPass1'), 'Strong')
 
    def test_weak_password_short(self):
        self.assertEqual(validate_password_strength('Short1'), 'Weak')
 
    def test_weak_password_no_number(self):
        self.assertEqual(validate_password_strength('Password'), 'Weak')
 
    def test_weak_password_no_uppercase(self):
        self.assertEqual(validate_password_strength('weakpass1'), 'Weak')
 
    def test_empty_password(self):
        self.assertEqual(validate_password_strength(''), 'Weak')
 
if __name__ == '__main__':
    unittest.main()