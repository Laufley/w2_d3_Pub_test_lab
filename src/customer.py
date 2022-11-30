class Customer:
    def __init__(self, name, age, wallet, drunkness):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkness = drunkness

    def reduce_money_in_wallet(self, amount):
        self.wallet -= amount

    def drunk_level(self, drink):
        self.drunkness += drink.alcohol_level
