"""
Practice Question 2: Determine Shipping Cost
Task:
Create a function calculate_shipping_cost
that takes the weight of a package (in kilograms)
and calculates the shipping cost.
If the weight is
up to 2 kg, the cost is $5. For each additional kg,
the cost increases by $2.
"""

def calculate_shipping_cost(weight):
    if weight <= 2:
        return 5
    else:
        return 5 + (2 * (weight - 2))