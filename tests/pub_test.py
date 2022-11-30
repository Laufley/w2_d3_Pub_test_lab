import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Last Drop", 500)
        
    def test_pub_has_name(self):
        self.assertEqual("The Last Drop", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(500, self.pub.till)

    def test_add_drink_to_list_of_drinks(self):
        drink1 = Drink("wine", 6, 13)
        self.pub.add_drink(drink1)
        self.assertEqual(1, self.pub.number_of_drinks())

    def test_increase_money_till(self):
        self.pub.increase_money_in_till(5)
        self.assertAlmostEqual(505, self.pub.till)

    def test_can_remove_drink_from_drink_list(self):
        drink1 = Drink("wine", 6, 13)
        drink2 = Drink("beer", 5, 4)
        self.pub.add_drink(drink1)
        self.pub.add_drink(drink2)
        self.pub.remove_drink_from_drink_list(drink1)
        self.assertEqual(1, self.pub.number_of_drinks())

    def test_check_customer_age(self):
        customer1 = Customer("Uncle Roger", 31,  50, 0)
        self.assertEqual(True, self.pub.check_customer_age(customer1))

    def test_check_customer_age(self):
        customer2 = Customer("Nephew", 16,  50, 0)
        self.assertEqual(False, self.pub.check_customer_age(customer2))

    def test_check_drunkness_of_customer(self):
        customer1 = Customer("Uncle Roger", 31,  50, 0)
        self.assertEqual(True, self.pub.check_drunkness_of_customer(customer1))

    def test_check_drunkness_of_customer(self):
        customer1 = Customer("Uncle Roger", 31,  50, 14)
        self.assertEqual(False, self.pub.check_drunkness_of_customer(customer1))

    def test_can_sell_drink_to_customer(self):
        drink1 = Drink("wine", 6, 13)
        drink2 = Drink("beer", 5, 4)
        customer1 = Customer("Uncle Roger", 31,  50, 0)
        self.pub.add_drink(drink1)
        self.pub.add_drink(drink2)
        self.pub.sell_drink_to_customer(drink1, customer1)
        self.assertEqual(506, self.pub.till)
        self.assertEqual(1, self.pub.number_of_drinks())
        self.assertEqual(44, customer1.wallet)

    def test_refuse_sale_to_customer_underaged(self):
        drink1 = Drink("wine", 6, 13)
        drink2 = Drink("beer", 5, 4)
        customer2 = Customer("Nephew", 16,  50, 0)
        self.pub.add_drink(drink1)
        self.pub.add_drink(drink2)
        self.pub.sell_drink_to_customer(drink1, customer2)
        self.assertEqual(500, self.pub.till)
        self.assertEqual(2, self.pub.number_of_drinks())
        self.assertEqual(50, customer2.wallet)

    def test_refuse_sale_to_customer_drunk(self):
        drink1 = Drink("wine", 6, 13)
        drink2 = Drink("beer", 5, 4)
        customer1 = Customer("Uncle Roger", 31,  50, 14)
        self.pub.add_drink(drink1)
        self.pub.add_drink(drink2)
        self.pub.sell_drink_to_customer(drink1, customer1)
        self.assertEqual(500, self.pub.till)
        self.assertEqual(2, self.pub.number_of_drinks())
        self.assertEqual(50, customer1.wallet)
