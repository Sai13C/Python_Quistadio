# Shopping List Dictionary

shopping = {}

for i in range(3):
    item = input("Enter an item: ")
    price = input("Enter the price: ")

    shopping[item] = price

print("\n--- Your Shopping List ---")

for item, price in shopping.items():
    print(item, "=", price)
