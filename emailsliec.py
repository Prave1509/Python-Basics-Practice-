email = input ("Enter Your Mail ID :")

index = email.index('@')
#praveen123@gmail.com 
#the index is 10 for @ 
#the 0 to 10-1 (0 to position of(@)-1)will the user name others were @gmail.com

username = email[:index]
other = email[index:]

print(f"The User name is {username}\n other :{other} ")