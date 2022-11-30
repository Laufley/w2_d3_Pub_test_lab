import unittest
from src.customer import Customer 
from src.drink import Drink

class TestCustomer(unittest.TestCase):
    
    def setUp(self):
        self.customer = Customer("Uncle Roger", 31, 50, 0)
    
    def test_customer_has_name(self):
        self.assertEqual("Uncle Roger", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(50, self.customer.wallet)

    def test_reduce_money_wallet(self):
        self.customer.reduce_money_in_wallet(5)
        self.assertAlmostEqual(45, self.customer.wallet)

    def test_drunk_level(self):
        drink2 = Drink("beer", 5, 4)
        self.customer.drunk_level(drink2)
        self.assertEqual(4, self.customer.drunkness)
