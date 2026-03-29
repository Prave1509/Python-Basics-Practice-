foods = []
prices = []
total = 0
while True:
    food = input("Enter food to buy or Enter q or Quit :")
    if food.lower() == 'q':
        print("Quiting..")
        break
    else:
        price = float(input(f"Enter the Price of the {food} "))
        foods.append(food)
        prices.append(price)

print("==== YOUR FOOD CART ====")
for x in range(len(foods)):
    print(f"{foods[x]} - ₹{prices[x]}")
    

for x in prices:
    total += x

print(f"The Total Bill is ₹{total}")