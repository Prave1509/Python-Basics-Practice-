import random
lower = 1
higher = 100
is_running = True
no_of_guess = 0

actual_value = random.randint(lower,higher)

print("=========Number Guessing Game==========")
print(f"Enter Number Between {lower} and {higher} ")

while is_running:

    guess = input ("Enter your Guess :")
    if guess.isdigit():
        guess = int(guess)
        no_of_guess += 1

        if guess < lower or guess > higher :
            print("Your Guess is out of Range..!")
            print(f" Please Enter Number Between {lower} and {higher} ")
        elif guess < actual_value :
            print("The Answer is Greater than your guess ")
            print("Your Guess is very low..! Try Again Buddy")
        elif guess > actual_value :
            print("The answer is Lower than your guess ")
            print("Your Guess is very high..! Try Again you can do it ..!")
        else :
            print(f"You Got it ...The answer is {actual_value}")
            print(f"The No of Guesses {no_of_guess}")    
            is_running = False
    else:
        print("Invalid Input..!")
        print(f" Please Enter Number Between {lower} and {higher} ")

