from idlelib.configdialog import changes

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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
water = 300
milk = 200
coffee = 100
Money = 0
nick = True
while nick:
    ask = (input("What would you like? (espresso/latte/cappuccino):")).lower()
    if ask == "off":
        nick = False
        break
    if ask == "report":
        print("Water:",water,"ml","\nMilk:",milk,"ml","\nCoffee:",coffee,"ml","\nMoney: $",Money)
    if water == 0 or coffee == 0:
        print("Insufficient resources")
        continue
    if ask == "espresso" and (water < 50 or coffee < 18):
        print("Insufficient resources")
        continue
    if ask == "latte" and (water < 200 or milk < 150 or coffee < 24):
        print("Insufficient resources")
        continue
    if ask == "cappuccino" and (water < 250 or milk < 100 or coffee < 24):
        print("Insufficient resources")
        continue
    else:
        if ask == "espresso":
            Money += 1.5
        if ask == "latte":
            Money += 2.5
        if ask == "cappuccino":
            Money += 3.0
        print("Please insert coins.")
        def coffee_machine(quarter, dimes, nickles, pennies , cost,water_reduce,coffee_reduce,milk_reduce,coffee_name):
            quarter *= 0.25
            dimes *= 0.10
            nickles *= 0.05
            pennies *= 0.01
            total = quarter + dimes + nickles + pennies
            if total > cost:
                global water, milk, coffee
                change = round((total - cost),2)

                print(f"Here is ${change} in change\nHere is your {coffee_name} ☕️. Enjoy!")
                water -= water_reduce
                coffee -= coffee_reduce
                milk -= milk_reduce
                if water < 0:
                    water = 0
                if coffee < 0:
                    coffee = 0
                if milk < 0:
                    milk = 0
            else:
                print("Sorry that's not enough money. Money refunded.")
        if ask == "espresso":
            coffee_machine(quarter=(int(input("how many quarters?:"))), dimes=(int(input("how many dimes?:"))),
                     nickles=(int(input("how many nickles?:"))), pennies=(int(input("how many pennies?:"))),
                   cost = 1.5,water_reduce=50,coffee_reduce=18,milk_reduce=0,coffee_name="espresso")
        if ask == "latte":
            coffee_machine(quarter=(int(input("how many quarters?:"))), dimes=(int(input("how many dimes?:"))),
                   nickles=(int(input("how many nickles?:"))), pennies=(int(input("how many pennies?:"))), cost=1.5,
                   water_reduce=200, coffee_reduce=24 ,milk_reduce=150,coffee_name="latte")
        if ask == "cappuccino":
            coffee_machine(quarter=(int(input("how many quarters?:"))), dimes=(int(input("how many dimes?:"))),
                           nickles=(int(input("how many nickles?:"))), pennies=(int(input("how many pennies?:"))),
                           cost=3.0,water_reduce=250, coffee_reduce=24, milk_reduce=100, coffee_name="cappuccino")


