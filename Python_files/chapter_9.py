"""
Question 1: Vehicle Registration System
Description:
Create a class called VehicleRegistry.
It should have the following attributes and methods:

Attributes: 

registry_name (string) and 

registered_vehicles (dictionary with vehicle license plate numbers as keys and 
a tuple (owner_name, vehicle_type) as values).

Methods:

register_vehicle(license_plate, owner_name, vehicle_type): 
Registers a new vehicle.

deregister_vehicle(license_plate): Removes a vehicle from the registry.

list_vehicles(): Returns a list of all registered vehicles in 
the format “License Plate: Owner – Vehicle Type”.
"""

class VehicleRegistry:

    def __init__(self, registry_name):
        self.registry_name = registry_name
        self.registered_vehicles = {}
    
    def register_vehicle(self, license_plate, owner_name, vehicle_type):
        self.registered_vehicles[license_plate] = (owner_name, vehicle_type)
    
    def deregister_vehicle(self, license_plate):
        del self.registered_vehicles[license_plate]
    
    def list_vehicles(self):
        list = []
        for key, value in self.registered_vehicles.items():
            list.append(f"{key}: {value[0]} - {value[1]}")
        return list

"""
Question 2: Event Management
Description:
Create a class called EventManager.
It should have the following attributes and methods:

Attributes: event_name (string) and participants (list of participant names).
Methods:
add_participant(name): Adds a new participant.
remove_participant(name): Removes a participant.
get_participant_list(): Returns a list of all participants.
"""

class EventManager:

    def __init__(self, event_name):
        self.event_name = event_name
        self.participants = []
    
    def add_participant(self, name):
        self.participants.append(name)
    
    def remove_participant(self, name):
        self.participants.remove(name)
    
    def get_participant_list(self):
        return self.participants
        
"""
Question 3: Online Store Inventory
Description:
Create a class called StoreInventory. It should have
the following attributes and methods:

Attributes: store_name (string) and inventory (dictionary
with product names as keys and quantities as values).
Methods:
add_product(product_name, quantity): Adds or updates 
a product in the inventory.
remove_product(product_name): Removes a product from the inventory.
check_stock(product_name): Returns the quantity of the specified product.
"""

class StoreInventory:
    def __init__(self, store_name):
        self.store_name = store_name
        self.inventory = {}
    
    def add_product(self, product_name, quantity):
        self.inventory[product_name] = quantity
    
    def remove_product(self, product_name):
        del self.inventory[product_name]
    
    def check_stock(self, product_name):
        return self.inventory[product_name]
