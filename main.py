from http.client import MOVED_PERMANENTLY
import re


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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

resources = {"water": 300, "milk": 200, "coffee": 100, "Money": 0}
resourceUnits = {"water": "ml", "milk": "ml", "coffee": "g", "Money": "$"}
coinValues = {"quarters": 0.25, "dimes": 0.10, "nickles": 0.05, "pennies": 0.01}

machineStatus = "on"

def turnOff():
    print("Goodbye")
    return "off"


def printResourcesWithUnits():
    for item in resources:
        stringFormat = "{0}: {1}{2:.2f}" if item == "Money" else "{0}: {2}{1}"
        print(stringFormat.format(item, resourceUnits[item], resources[item]))


def enoughResources(drink):
    """returns True if enough resources to make drink passed in"""
    output = True
    for ingredient in MENU[drink]["ingredients"]:
        if resources[ingredient] < MENU[drink]["ingredients"][ingredient]:
            output = False
            print (f"Sorry there is not enough {ingredient}.")
    return output

def processCoins():
    """returns the total $ calculated from inserted coins"""
    print("Please insert coins.")
    moneyGiven = 0
    for coin in coinValues:
        givenCoin = input("How many {}?: ".format(coin))
        if not givenCoin:
            givenCoin = 0
        else:
            try:
                givenCoin = int(givenCoin)
            except:
                print("invalid input: not a number")
                givenCoin = 0
        moneyGiven += round(givenCoin * coinValues[coin],2)
        print("    Total so far: ${:.2f}".format(moneyGiven))
    return moneyGiven

def processTransaction(drink):
    """checks if enough money was inputted, prints feedback, processes transaction"""
    price = MENU[drink]["cost"]
    moneyInput = processCoins()
    if moneyInput <= price:
        print("Sorry that's not enough money. Money refunded.")
        return "unsuccessful"
    change = moneyInput - price
    resources["Money"] += price
    print("Here is ${:.2f} in change.".format(change))
    return "success"

def makeCoffee(drink):
    """Deduct the ingredients from the resources"""
    for ingredient in MENU[drink]["ingredients"]:
        resources[ingredient] -= MENU[drink]["ingredients"][ingredient]
    print("Here is your {}. Enjoy! ☕".format(drink))


while machineStatus == "on":
    print("---- MENU:|espresso|latte|cappuccino|  MACHINE OPTIONS:|report|off| ----")
    userAction = input("What would you like? (espresso/latte/cappuccino): ")

    if userAction == "off":
        machineStatus = turnOff()
    elif userAction == "report":
        printResourcesWithUnits()
    elif userAction in MENU.keys() :
        if enoughResources(userAction):
            if processTransaction(userAction) == "success":
                makeCoffee(userAction)



        
