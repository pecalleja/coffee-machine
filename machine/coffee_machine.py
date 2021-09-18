from dataclasses import dataclass


@dataclass
class CoffeeMachine:
    water: int
    milk: int
    coffee_beams: int
    disposable_cups: int
    cash: int
    recipes = {
        "1": {
            "name": "espresso",
            "water": 250,
            "milk": 0,
            "coffee": 16,
            "cost": 4
        },
        "2": {
            "name": "latte",
            "water": 350,
            "milk": 75,
            "coffee": 20,
            "cost": 7
        },
        "3": {
            "name": "cappuccino",
            "water": 200,
            "milk": 100,
            "coffee": 12,
            "cost": 6
        }
    }

    def get_status(self):
        print("The coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.coffee_beams} of coffee beans")
        print(f"{self.disposable_cups} of disposable cups")
        print(f"{self.cash} of money")


coffee_machine = CoffeeMachine(
    cash=550,
    water=400,
    milk=540,
    coffee_beams=120,
    disposable_cups=9
)

print("Write action (buy, fill, take, remaining, exit):")
action = input()
while action != "exit":
    if action == "fill":
        print("Write how many ml of water you want to add:")
        coffee_machine.water += int(input())
        print("Write how many ml of milk you want to add:")
        coffee_machine.milk += int(input())
        print("Write how many grams of coffee beans you want to add:")
        coffee_machine.coffee_beams += int(input())
        print("Write how many disposable coffee cups you want to add:")
        coffee_machine.disposable_cups += int(input())
    elif action == "take":
        print(f"I gave you {coffee_machine.cash}")
        coffee_machine.cash = 0
    elif action == "buy":
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
        coffee_option = input()
        if coffee_option != "back":
            recipe = coffee_machine.recipes[coffee_option]
            if coffee_machine.milk < recipe["milk"]:
                print("Sorry, not enough milk!")
            elif coffee_machine.water < recipe["water"]:
                print("Sorry, not enough water!")
            elif coffee_machine.coffee_beams < recipe["coffee"]:
                print("Sorry, not enough coffee!")
            else:
                print("I have enough resources, making you a coffee!")
                coffee_machine.cash += recipe["cost"]
                coffee_machine.milk -= recipe["milk"]
                coffee_machine.water -= recipe["water"]
                coffee_machine.coffee_beams -= recipe["coffee"]
                coffee_machine.disposable_cups -= 1
    elif action == "remaining":
        coffee_machine.get_status()

    print("Write action (buy, fill, take, remaining, exit):")
    action = input()
