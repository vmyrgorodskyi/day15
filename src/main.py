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
    "water": 1000,
    "milk": 200,
    "coffee": 100,
}

#quarters = 0.25
#dimes = 0.1
#nickels = 0.05
#pennies = 0.01



# def calc_money():
#     print("Please insert coins: ")
#     quarters = input("how many quarters?: ")
#     dimes = input("how many dimes?: ")
#     nickels = input("how many nickels?: ")
#     pennies = input("how many pennies?: ")
#     float_money = (float(quarters) * 0.25) + (float(dimes) * 0.1) + (float(nickels) * 0.05) + (float(pennies) * 0.01)
#     return float_money

money = 0
received_money = 0
float_money = float(money)
change = 0

continue_operate = True
#print(MENU["espresso"]["ingredients"])
while continue_operate:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    # TODO 1. Print the report of all the resources
    if user_choice == "report":
        #print(resources, resources["water"])
        #for ingredient, amount in resources.items():
            #print(f"{ingredient.capitalize()}:  {amount}")
        print("Water: " + str(resources["water"]) + "ml")
        print("Milk: " + str(resources["milk"]) + "ml")
        print("Coffee: " + str(resources["coffee"]) + "g")
        print(f"Money: ${round(float_money, 2)}")
    elif user_choice == "off":
        print("Bye")
        break
    elif user_choice == "espresso":
        if resources["water"] < MENU["espresso"]["ingredients"]["water"]:
            print("Sorry there is not enough water")
        elif resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee")
        else:
            # calc_money()
            print("Please insert coins")
            quarters = input("how many quarters?: ")
            dimes = input("how many dimes?: ")
            nickels = input("how many nickels?: ")
            pennies = input("how many pennies?: ")
            received_money = (float(quarters) * 0.25) + (float(dimes) * 0.1) + (float(nickels) * 0.05) + (float(pennies) * 0.01)
            if received_money >= MENU["espresso"]["cost"]:
                change = received_money - MENU["espresso"]["cost"]
                float_money = float_money + float(MENU["espresso"]["cost"])
                print(f"Here is your {round(change, 2)} change")
                print("Here is your espresso. Enjoy!")
            else:
                print("Sorry, that is not enough money. Money refunded")
    elif user_choice == "latte":
        if resources["water"] < MENU["latte"]["ingredients"]["water"]:
            print("Sorry there is not enough water")
        elif resources["milk"] < MENU["latte"]["ingredients"]["milk"]:
            print("Sorry there is not enough milk")
        elif resources["coffee"] < MENU["latte"]["ingredients"]["coffee"]:
            print("Sorry there is not enough milk")
        else:
            print("Please insert coins")
            quarters = input("how many quarters?: ")
            dimes = input("how many dimes?: ")
            nickels = input("how many nickels?: ")
            pennies = input("how many pennies?: ")
            received_money = (float(quarters) * 0.25) + (float(dimes) * 0.1) + (float(nickels) * 0.05) + (float(pennies) * 0.01)
            if received_money >= MENU["latte"]["cost"]:
                change = received_money - MENU["latte"]["cost"]
                float_money = float_money + float(MENU["latte"]["cost"])
                print(f"Here is your {round(change, 2)} change")
                print("Here is your latte. Enjoy!")
            else:
                print("Sorry, that is not enough money. Money refunded")
    elif user_choice == "cappuccino":
        if resources["water"] < MENU["cappuccino"]["ingredients"]["water"]:
            print("Sorry there is not enough water")
        elif resources["milk"] < MENU["cappuccino"]["ingredients"]["milk"]:
            print("Sorry there is not enough milk")
        elif resources["coffee"] < MENU["cappuccino"]["ingredients"]["coffee"]:
            print("Sorry there is not enough milk")
        else:
            print("Please insert coins")
            quarters = input("how many quarters?: ")
            dimes = input("how many dimes?: ")
            nickels = input("how many nickels?: ")
            pennies = input("how many pennies?: ")
            received_money = (float(quarters) * 0.25) + (float(dimes) * 0.1) + (float(nickels) * 0.05) + (float(pennies) * 0.01)
            if received_money >= MENU["cappuccino"]["cost"]:
                change = received_money - MENU["cappuccino"]["cost"]
                float_money = float_money + float(MENU["cappuccino"]["cost"])
                print(f"Here is your {round(change, 2)} change")
                print("Here is your cappuccino. Enjoy!")
            else:
                print("Sorry, that is not enough money. Money refunded")









# TODO 2. Check resource sufficient to make drink order
