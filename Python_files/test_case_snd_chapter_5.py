import unittest
from snd_chapter_5 import calculate_shipping_cost
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