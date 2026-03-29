import time

time_var = int(input("Enter the time in seconds :"))
for x in range(time_var, 0, -1):
    seconds = x % 60 #get the remaining seconds
    minutes = int(x/60) % 60 
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("The Time is UP..!")

#for example 
#input is 3665 almost one hour
#for seconds 3665 / 60 = 61 , remainder is 5
#for minutes 3665 / 60 = 61.08 nearly 61 , 61 % 60 = 1 , 1 min
#for hours 3665 / 3600 = 1.01 nearly 1 , 1 hour
#it conclude 01:01:05