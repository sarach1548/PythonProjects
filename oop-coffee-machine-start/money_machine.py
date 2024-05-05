class MoneyMachine:
    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit"""
        print(f"money: ${self.profit + self.money_received}")

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        q = input("quarters:")
        d = input("dimes")
        n = input("nickles")
        p = input("pennies")
        return q * 0.25 + d * 0.10 + n * 0.05 + p * 0.01

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        sum = self.process_coins()
        if sum < cost:
            print("Sorry that's not enough money. Money refunded.")
            return False
        if sum>cost:
            self.money_received=sum-cost
        self.profit=cost