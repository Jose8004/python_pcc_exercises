import unittest
from chapter_9 import VehicleRegistry, EventManager, StoreInventory
 
class TestVehicleRegistry(unittest.TestCase):
    def setUp(self):
        self.registry = VehicleRegistry("City Registry")
 
    def test_register_vehicle(self):
        self.registry.register_vehicle("ABC123", "John Doe", "Car")
        self.assertIn("ABC123", self.registry.registered_vehicles)
        self.assertEqual(self.registry.registered_vehicles["ABC123"], ("John Doe", "Car"))
 
    def test_deregister_vehicle(self):
        self.registry.register_vehicle("XYZ789", "Jane Smith", "Truck")
        self.registry.deregister_vehicle("XYZ789")
        self.assertNotIn("XYZ789", self.registry.registered_vehicles)
 
    def test_list_vehicles(self):
        self.registry.register_vehicle("ABC123", "John Doe", "Car")
        expected_list = ["ABC123: John Doe - Car"]
        self.assertEqual(self.registry.list_vehicles(), expected_list)
 
if __name__ == '__main__':
    unittest.main()


class TestEventManager(unittest.TestCase):
    def setUp(self):
        self.event = EventManager("Tech Conference")
 
    def test_add_participant(self):
        self.event.add_participant("Alice")
        self.assertIn("Alice", self.event.participants)
 
    def test_remove_participant(self):
        self.event.add_participant("Bob")
        self.event.remove_participant("Bob")
        self.assertNotIn("Bob", self.event.participants)
 
    def test_get_participant_list(self):
        self.event.add_participant("Alice")
        self.event.add_participant("Bob")
        expected_list = ["Alice", "Bob"]
        self.assertEqual(self.event.get_participant_list(), expected_list)
 
if __name__ == '__main__':
    unittest.main()

class TestStoreInventory(unittest.TestCase):
    def setUp(self):
        self.store = StoreInventory("BestStore")
 
    def test_add_product(self):
        self.store.add_product("Laptop", 10)
        self.assertIn("Laptop", self.store.inventory)
        self.assertEqual(self.store.inventory["Laptop"], 10)
 
    def test_remove_product(self):
        self.store.add_product("Mouse", 15)
        self.store.remove_product("Mouse")
        self.assertNotIn("Mouse", self.store.inventory)
 
    def test_check_stock(self):
        self.store.add_product("Keyboard", 20)
        self.assertEqual(self.store.check_stock("Keyboard"), 20)
 
if __name__ == '__main__':
    unittest.main()