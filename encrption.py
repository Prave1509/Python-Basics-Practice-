import random
import string

chars = " "+ string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)
#print(f"My Chars List :{chars}")
#print(f"My Key List   :{key}")

#encryption process
text = input("Enter Your Message to Encrypt : ")
encrypt = ""

for letter in text :
    index = chars.index(letter)
    encrypt += key[index]

print ("Your Text    :",text)
print ("Encrypt Text :",encrypt)


redo = input("Do you want to Decrypt the Text to Original Formate (Enter y or n):").lower()
if redo == 'y':

    #decryption process
    cipher = input("Enter the Encryption Text to make it Original Text : ")
    text = ""

    for letter in cipher:
        index = key.index(letter)
        text += chars[index]

    print ("The Encrypted Text :",cipher)
    print ("The Original Text  :",text)

elif redo != 'y' and redo != 'n':
    print("Invalid Input..")

else:
    print("Thank you buddy..!")
