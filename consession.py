menu = {"Biriyani":500,
        "Parrato":30,
        "Mushroom Rice":450,
        "Panner Tikka":90,
        "Dessart":180,
        "Ice Cream":45}

cart = []
total_bill = 0


print("---------MENU----------")
for key , value in menu.items():  #menu.items give the key and value here biriyani:500;
    print(f"{key:15} - ₹{value:.2f}")

print("=======================")

while True :
    food = input ("Enter Your Order or Enter Q to Quit:").lower()
    if food == "q":
        break
    found = False
    for item in menu:
        if item.lower() == food.lower():
            cart.append(item)
            found = True
            break
    if not found:
        print("Item not Found!")

print("========YOUR ORDER========")
for x in cart:
    total_bill += menu.get(x)
    print(x)
    
print(f"Total is :₹{total_bill}")