from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

state="on"
while(state!="off"):
    selected = input("What would you like? (espresso/latte/cappuccino):")
    myMenu=Menu()
    myCoffeeMaker=CoffeeMaker()
    myMoneyMechine=MoneyMachine()
    if myMenu.find_drink(selected) is not None:
        myMenuItem=myMenu.find_drink(selected)
        s=input("report? ")
        if s=="report":
            myCoffeeMaker.report()
        if myCoffeeMaker.is_resource_sufficient(myMenuItem):
            myMoneyMechine.make_payment(myMenuItem.cost)