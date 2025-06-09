from art import logo
print(logo)


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
profit=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def report():
    """Print the available resources and machine profit."""
    print(f"water :{resources["water"]}")
    print(f"coffee :{resources["coffee"]}")
    print(f"milk :{resources["milk"]}")
    print(f"amount :{round(profit,2)}")
def is_resource(order_ingredients):
    """Check resources are sufficient or not to make the drink."""
    for item in order_ingredients:
        if order_ingredients[item]>resources[item]:
            print("Not enough ingredients available")
            return False
        else:
            return True
def coin():
    """Ask the user to enter the coin ."""
    total=float(input("Enter the  number of quarter: "))*0.25
    total +=float(input("Enter the number of quarter:  "))*0.10
    total +=float(input("Enter the number of nickels:  "))*0.05
    total +=float(input("Enter the number of penny:  "))*0.01
    return total
def transaction(money_received,drink_cost):
    """Check the entered amount is sufficient to make the drink"""
    if money_received>drink_cost:
        change=round(money_received-drink_cost,2)
        print(f"here is your {change} change")
        global profit
        profit+=drink_cost
        return True
    else:
        print("Not enough amount paid")
        return False
def making(choice):
    """Return the message coffee making and deplete the resources used."""
    ingredients=["milk","coffee","water"]
    for item in ingredients:
        if item in choice["ingredients"]:
            resources[item]-=choice["ingredients"][item]
    print(f"Here is your {user} ☕️. Enjoy!")





is_on=True
while is_on:
    user=input("what would you like(cappuccino,espresso,latte): ").lower()
    if user=="off":
        is_on=False
    elif user=="report":
        report()
    elif user in MENU:
        chosen=MENU[user]
        if is_resource(chosen["ingredients"]):
            amount=coin()
            if transaction(amount,chosen['cost']):

                making(chosen)