import random
def spin_row():
    symbols = ['❤️','⭐','😎','🌳','👍']
    
    return [random.choice(symbols) for x in range(3)]

def print_row(row):
    print(" | ".join(row))

def get_payout(row,bet):
    if row[0] == row[1] == row[2] :
        if row[0] == "🌳":
            return bet * 5
        elif row[0] == "😎":
            return bet * 8
        elif row[0] == "👍":
            return bet * 10
        elif row[0] == "⭐":
            return bet * 20
        elif row[0] == "❤️":
            return bet * 50
    return 0
    

def main():
    balance = 100

    print("-------------------------")
    print("WELCOME TO SLOT MACHINE")
    print("The Symbols :❤️ ⭐ 😎 🌳 👍")
    print("-------------------------")

    while balance > 0:
        print(f"Your Current Balance is {balance}")
        bet = input("Enter your Bet Amount :")

        if bet.isdigit() == False:
            print("Enter Valid Input..!")
            continue

        bet = int(bet)
        if bet > balance :
            print("Your Bet amount is greater than your Balance")
            continue
        if bet <=0 :
            print("The Bet amount is Invalid..!")

        elif isinstance(bet,(int,float)) == True:
            balance -= bet
            print(f"The Bet Amount is {bet} ")
            print(f"The Avalible Balance is {balance}")
            ans = input("Are you want to spin now  💫 enter(y/n) :").lower()
            if ans != 'y':
                print("Quit")
                break
            row = spin_row()
            print("Spinning...\n")
            print_row(row)
            
            payout = get_payout(row,bet)
            if payout > 0:
                print(f"You Won {payout}")
            else:
                print("Sorry you lose")

            again = input("\n Do you want to play again? (y/n)").lower()

            if again != 'y':
                print("Thanks for Playing.")
                break
    if balance <= 0:
        print("\n You ran out of Balance Game over..!")
    else:
        print("Total :",payout)     

            


        


if __name__ == '__main__':
    main()