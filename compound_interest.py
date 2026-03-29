principle_amount = float(input("Enter your Principle Amount :"))
rate = float(input("Enter Rate of Interest :"))
time = int(input("Enter the time Duration :"))
n = int(input("Enter the Compounding :"))

amount = principle_amount * (1 + rate/n) ** (n * time)
interest = amount - principle_amount

print(f"Final Amount : ₹{amount}")
print(f"Compound Interest : ₹{interest}")