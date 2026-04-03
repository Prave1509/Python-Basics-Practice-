question = (("1.Expansion for SBI"),
            ("2.Who is the Owner for Clude"),
            ("3.AWS is which ones"))

option = (("A.State Bank of India","B.State Bulk India","C.State Boost India"),
          ("A.Google","B.Microsoft","C.Antropic"),
          ("A.Microsoft","B.Amazon","C.Flipkart"))

question_num = 0

answers = ["A","C","B"]

guesses = []

score = 0
for x in question:
    print("---------------------------------")
    print(x)
    for y in option[question_num]:
        print(y)
    

    guess = input("Enter (A,B,C):").upper()
    
    guesses.append(guess)
    
    if guess == answers[question_num]:
        
        score += 1
        print ("Correct Answer..!")

    else:
         print ("InCorrect")
         print(f"The Correct Answer is {answers[question_num]}")
    question_num += 1

print("The Answers are :",answers)

print("You entered :",guesses)

final_score = int(score/ len(question) * 100)
print("Your Final Score is ",final_score)