class CoffeeMaker:
    """Models the machine that makes the coffee"""

    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """Prints a report of all resources."""
        print(f"water: {self.resources["water"]}ml\nmilk: {self.resources["milk"]}ml\ncoffee: {self.resources["coffee"]}g")

    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        if self.resources["water"] - drink.ingredients["water"] < 0:
            print("Sorry there is not enough water.")
            return False
        if self.resources["milk"] - drink.ingredients["milk"] < 0:
            print("Sorry there is not enough milk.")
            return False
        if self.resources["coffee"] - drink.ingredients["coffee"] < 0:
            print("Sorry there is not enough coffee.")
            return False
        return True

    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        if self.is_resource_sufficient(order):
            self.resources["water"] -= order.ingredients["water"]
            self.resources["milk"] -= order.ingredients["milk"]
            self.resources["coffee"] -= order.ingredients["coffee"]
        # קודם תורידו את הכמויות ואח"כ תדפיסו:
        print(f"Here is your {order.name} ☕️. Enjoy!")
