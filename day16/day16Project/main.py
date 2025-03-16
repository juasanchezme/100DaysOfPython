from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()

machineON  = True
while machineON:
    drinkOrder = input(f"what beverage would you like {menu.get_items()}? ")

    # printing a report 
    if drinkOrder == "report":
        coffeeMaker.report()
        moneyMachine.report()
    elif drinkOrder == "off":
        machineON = False

    else:
        
        if menu.find_drink(drinkOrder):
            selectedDrinkObj = menu.find_drink(drinkOrder)

            if coffeeMaker.is_resource_sufficient(selectedDrinkObj):
                cost = selectedDrinkObj.cost
                #print(cost)
                
                if moneyMachine.make_payment(cost):
                    coffeeMaker.make_coffee(selectedDrinkObj)
