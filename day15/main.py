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

pedido = input("​What would you like? (espresso/latte/cappuccino):​")

if pedido == "report":
    for key, value in resources.items():
        print(key, value)

# TODO: 2. Given an input, Check resources

gastoDeRecurso = resources.copy()

for resource in ["water", "milk", "coffee"]:
    gastoDeRecurso[resource] = resources[resource] - MENU[pedido]["ingredients"][resource]

    if gastoDeRecurso[resource] < 0:
        print(f"Sorry, but there is not enough {resource}")

# If there is enough resources, process with the payment