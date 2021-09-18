print("Write how many ml of water the coffee machine has:")
water = int(input())
print("Write how many ml of milk the coffee machine has:")
milk = int(input())
print("Write how many grams of coffee beans the coffee machine has:")
coffee = int(input())
print("Write how many cups of coffee you will need:")
cups = int(input())

coffee_recipe = {
    'water': 200,
    'milk': 50,
    'coffee': 15
}

cups_count = 0

while (
    water >= coffee_recipe['water'] and
    milk >= coffee_recipe['milk'] and
    coffee >= coffee_recipe['coffee']
):
    cups_count += 1
    water -= coffee_recipe['water']
    milk -= coffee_recipe['milk']
    coffee -= coffee_recipe['coffee']

if cups > cups_count:
    print(f"No, I can make only {cups_count} cup(s) of coffee")
elif cups < cups_count:
    print(f"Yes, I can make that amount of coffee (and even {cups_count - cups} more than that)")
else:
    print("Yes, I can make that amount of coffee")
