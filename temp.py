op = int(input("Temperature Conventer\nEnter 1 for Celsius to Fahrenheit Conventer\nEnter 2 for Fahrenheit to Celsius  "))

if op == 1:
    cel = float(input("Enter the Celsius Value :"))
    result = (cel * 9/5)+32
    print(f"The Fahrenheit is {result}F for {cel} C  ")

elif op == 2:
    frn = float(input("Enter the Fahrenheit Value :"))
    result = (frn - 33)*5/9
    print(f"The Celsius is {result}C for {frn} F  ")

else :
    print("Enter Valid Input")
