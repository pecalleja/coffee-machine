# print("Starting to make a coffee")
# print("Grinding coffee beans")
# print("Boiling water")
# print("Mixing boiled water with crushed coffee beans")
# print("Pouring coffee into the cup")
# print("Pouring some milk into the cup")
# print("Coffee is ready!")
print("Write how many cups of coffee you will need:")
amount = int(input())  # cups
water = 200  # ml
milk = 50  # ml
coffee = 15  # g
print(f"For {amount} cups of coffee you will need:")
print(f"{water*amount} ml of water")
print(f"{milk*amount} ml of milk")
print(f"{coffee*amount} g of coffee beans")
