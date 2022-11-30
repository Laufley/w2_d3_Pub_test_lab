import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Last Drop", 500)
        self.drink = Drink("rum and ginger", 7)
        

    def test_pub_has_name(self):
        self.assertEqual("The Last Drop", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(500, self.pub.till)

    def test_add_drink_to_list_of_drinks(self):
        self.pub.add_drink(self.drink)
        self.assertEqual(1, self.pub.number_of_drinks())

    def test_increase_money_till(self):
        self.pub.increase_money_in_till(5)
        self.assertAlmostEqual(505, self.pub.till)

    def test_can_remove_drink_from_drink_list(self):
        drink1 = Drink("wine", 6)
        drink2 = Drink("beer", 5)
        self.pub.add_drink(drink1)
        self.pub.add_drink(drink2)
        self.pub.remove_drink_from_drink_list(drink1)
        self.assertEqual(1, self.pub.number_of_drinks())

    def test_can_sell_drink_to_customer(self):
        customer = Customer("Uncle Roger", 50)
        drink1 = Drink("wine", 6)
        drink2 = Drink("beer", 5)
        self.pub.add_drink(drink1)
        self.pub.add_drink(drink2)
        self.pub.sell_drink_to_customer(drink1, customer)
        self.assertEqual(506, self.pub.till)
        self.assertEqual(1, self.pub.number_of_drinks())
        self.assertEqual(44, customer.wallet)