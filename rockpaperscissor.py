import random



running = True

while running:
    option = ("rock", "paper", "scissors")
    system = random.choice(option)
    user = None
        
    while user not in option:
        user = input("Enter Your Choice (ROCK PAPER OR SCISSORS) :").lower()

    print(f"You Select :{user}")
    print(f"The System select :{system}")

    if user == system :
        print("The Match will tie..! Try Again")
    elif user == "rock" and system == "scissors":
        print("You Win Buddy..")
    elif user == "paper" and system == "rock":
        print("You Win Buddy..")
    elif user == "scissors" and system == "paper":
        print("You Win Buddy..")
    else :
        print("Oops.. you Lose")
    
    play_again = input("Play Again? (y/n)").lower()
    if  play_again != "y":
        running = False

print("Thanks for playing..!Have a Nice day")