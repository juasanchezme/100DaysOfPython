print("hello")

# TODO: 1. print report of all coffe machine resources

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,

        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


# TODO: 2. Given an input, Check resources

def checkResources():
    for i in ["water", "milk", "coffee"]:
        suministro = resources[i] - MENU[pedido]["ingredients"][i]
        if suministro < 0:
            print(f"Sorry there is not enough {resources[i]}")
            return False
        return True
    

# If there is enough resources, process with the payment 

def payment():
    status = False

    print("Please insert money")
    quarters = int(input("How many quarters "))
    dimes = int(input("How many dimes "))
    nickels = int(input("How many nickels "))
    pennies = int(input("How many pennies "))

    userMoney = quarters*0.25 + 0.10*dimes + nickels*0.05 + pennies*0.02
    productPrice = MENU[pedido]["cost"]
    vuelto = userMoney - productPrice
    vuelto = round(vuelto,2)

    if userMoney >= productPrice:
        print(f"Preparing beverage {pedido}, you have {vuelto} back")
        status = True

    else:
        print(f"Sorry, not enough money, you may add {-vuelto}")

    return status

MachineON = True   
while MachineON:
    pedido = input("​What would you like? (espresso/latte/cappuccino):​")

    if pedido == "report":
        for key, value in resources.items():
            print(key, value)
    elif pedido == "off":
        MachineON = False

    else:
        if checkResources():
            if payment():
                resources["money"] += MENU[pedido]["cost"]
                resources["water"] -= MENU[pedido]["ingredients"]["water"]
                resources["milk"] -= MENU[pedido]["ingredients"]["milk"]
                resources["coffee"] -= MENU[pedido]["ingredients"]["coffee"]
