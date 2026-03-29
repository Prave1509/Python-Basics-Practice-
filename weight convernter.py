#weight convernter

op=input("Enter which operator to do..\n 1.Kilo to Pounds \n 2.Pounds to Kilo \n Enter 1 or 2 to perform ..")

if op == '1':
    kilo=float(input("Enter value for Kilo :"))
    result=kilo*2.20462
    print(f"For {kilo} the Pound value is {result} ")
elif op == '2':
    pound = float (input("Enter value for Pound :"))
    result = pound*0.45359
    print(f"For {pound} the Kilo value is {result} ")
else :
    print(f"{op} is not defined..")