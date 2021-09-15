import menu
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
kayna = True
money_machine = MoneyMachine()
menu = Menu()
coffee_maker = CoffeeMaker()
while   kayna:
    options = menu.get_items()
    choise = input(f"3tini ach baghi tchrb {options} : ")
    if choise == "off":
        kayna=False
    elif choise=="report":
        coffee_maker.report()
        money_machine.report()
    else:
         machroub =  menu.find_drink(choise)
         if coffee_maker.is_resource_sufficient(machroub):
             if money_machine.make_payment(machroub.cost) and money_machine.make_payment(machroub.cost):
                 coffee_maker.make_coffee((machroub))
                 kayna=False
