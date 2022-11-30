class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.list_of_drinks = []
    
    def add_drink(self, drink):
        self.list_of_drinks.append(drink)

    def number_of_drinks(self):
        return len(self.list_of_drinks)

    def increase_money_in_till(self, amount):
        self.till += amount
    
    def remove_drink_from_drink_list(self, drink):
        self.list_of_drinks.remove(drink)

    def check_customer_age(self, customer):
        if customer.age >= 18:
            return True
        else: 
            return False

    def check_drunkness_of_customer(self, customer):
        if customer.drunkness <= 11:
            return True
        else: 
            return False

    def sell_drink_to_customer(self, drink, customer):
        if self.check_customer_age(customer) == True:
            if self.check_drunkness_of_customer(customer) == True:
                customer.reduce_money_in_wallet(drink.price)
                self.increase_money_in_till(drink.price)
                self.remove_drink_from_drink_list(drink)
            else:
                return "go home, you're drunk"
        else:
            return "HAIYAA, you're underaged"

        
    
