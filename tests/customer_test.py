import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    
    def setUp(self):
        self.customer = Customer("Uncle Roger", 50)
    
    def test_customer_has_name(self):
        self.assertEqual("Uncle Roger", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(50, self.customer.wallet)

    def test_reduce_money_wallet(self):
        self.customer.reduce_money_in_wallet(5)
        self.assertAlmostEqual(45, self.customer.wallet)
