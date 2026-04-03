def balance(bank_balance):
    print(f"Your Bank Balance is ₹{bank_balance:.2f}")

def deposit():
    depo_amount = float(input("Enter the Deposit Amount :"))
    if depo_amount < 0 :
        print("The Deposit Amount is less than zero ! Please Check")
        return 0
    else :
        return depo_amount
        


def withdraw(bank_balance):
    amount = float(input("Enter the Withdraw Amount :"))
     
    if amount > bank_balance:
        print("The Withdraw amount is more than your Balance")
        print(f"The Bank Balance is {bank_balance}")
        return 0

    elif amount <= 0:
        print("Invalid withdraw amount")
        return 0
        
    else:
        return amount


def main():
    bank_balance = 0
    is_banking = True

    while is_banking:
        print("Welcome to the State Bank :")
        print("1.Balance Checking")
        print("2.Deposit money")
        print("3.Withdraw money")
        print("4.Exit Service")

        user_choice = input("Enter your Choice (1-4 only) :")

        if user_choice == '1':
            balance(bank_balance)
        elif user_choice == '2':
            a = deposit()
            bank_balance += a
        elif user_choice == '3':
            w = withdraw(bank_balance)
            bank_balance -= w
            print(f"The Withdraw amount is {w}")
            print(f"The Avalible balance is {bank_balance} ")
        elif user_choice == '4':
            is_banking = False
        else:
            print("Invalid input operation")

    print("Thanks for Banking with us..!")

if __name__ == '__main__':
    main()