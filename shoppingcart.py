foods = []
price = []
total = 0

while True:
    food = input("Enter the food item (q for quit):")
    if food == "q":
        break
    foods.append(food)
    p = float(input("Enter the price of the food item:"))
    price.append(p)

for i in range(len(foods)):
    total += price[i]

print(f"Total: {total:.2f}Rs")