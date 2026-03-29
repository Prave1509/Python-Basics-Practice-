operator=input("Enter an Operator (+ - * /) :")
num1 = float(input("Enter an 1st Number :"))
num2 = float(input("Enter an 2nd Number :"))

if operator == '+':
    p=num1+num2
    print(round(p,2))

elif operator == '-':
    p=num1-num2
    print(round(p,2))

elif operator == '*':
    p=num1*num2
    print(round(p,2))

elif operator == '/':
    p=num1/num2
    print(round(p,2))

else :
    print(f"{operator} is not an valid operator to perform calculation..")

