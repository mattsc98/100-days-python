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
    "money": 0
}

def display_resources():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")

def check_resources(drink):
    ingredients = drink['ingredients']
    
    water   = ingredients.get('water')
    coffee  = ingredients.get('coffee')
    milk    = ingredients.get('milk')
    
    if milk is None:
        milk = 0
        
    check_water     = resources['water'] - water
    check_milk      = resources['milk'] - milk
    check_coffee    = resources['coffee'] - coffee
    
    if(check_water < 0):
        print("Sorry there is not enough water")
        exit()
    if(check_milk < 0):
        print("Sorry there is not enough milk")
        exit()
    if(check_coffee < 0):
        print("Sorry there is not enough coffee")    
        exit()  
          

def process_coins():
    
    quarters_amount = int(input("How many quarters? "))
    dimes_amount    = int(input("How many dimes? "))
    nickles_amount  = int(input("How many nickles? "))
    pennies_amount  = int(input("How many pennies? "))
    
    quarters    = 0.25 * quarters_amount
    dimes       = 0.10 * dimes_amount
    nickles     = 0.05 * nickles_amount
    pennies     = 0.01 * pennies_amount
    
    total_coins = quarters + dimes + nickles + pennies
    return total_coins

def check_transaction_successful(drink_cost, coins_given, drink_name):
    change = 0.00

    if(drink_cost > coins_given):
        print("Sorry that's not enough money. Money refunded.")
        return False
    
    else:
        resources["money"] += drink_cost
        
        if(drink_cost != coins_given):
            change = coins_given - drink_cost
            change = round(change, 2)

        print(f"Enjoy your {drink_name}! Here is ${change} in change")
        return True

def deduct_resources(drink):
    ingredients = drink['ingredients']
    
    water   = ingredients.get('water')
    coffee  = ingredients.get('coffee')
    milk    = ingredients.get('milk')
    
    if milk is None:
        milk = 0
        
    resources['water']     = resources['water'] - water
    resources['milk']      = resources['milk'] - milk
    resources['coffee']    = resources['coffee'] - coffee

def coffee_machine():
    
    while(True):
        drink = {}
        
        user_input = input("What would you like? (espresso/latte/cappuccino): ")
        
        if(user_input == "off"):
            exit()
            
        elif(user_input == "report"):
            display_resources()
            continue
            
        elif(user_input == "espresso"):
            drink = MENU["espresso"]
            
        elif(user_input == "latte"):
            drink = MENU["latte"]        

        elif(user_input == "cappuccino"):
            drink = MENU["cappuccino"]   
            
        else:
            print("Invalid response")
            
        check_resources(drink)

        print(f"\nPrice is {drink['cost']}.")
        
        coins_given = process_coins()
        
        check_transaction = check_transaction_successful(drink['cost'], coins_given, user_input)
        if check_transaction is False:
            continue

        

            
coffee_machine()