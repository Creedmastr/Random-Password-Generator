from asyncore import write
from cgitb import text
import random
import time


lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = "@_%*$"

string = lower + upper + numbers
lenght = int(input("Lenght of the password : "))
if lenght < 3:
    print("Please enter a lenght of 3 or plus")
    time.sleep(10)
    exit("Please enter a lenght of 3 or plus")
elif lenght > 999:
    print("Please enter a lenght of 999 or under 999")
    time.sleep(10)
    exit()
else: 
    pass

symbols_wanted = input("Do you want symbols in your password ? (y/n)")
if symbols_wanted == "y":
    string = lower + upper + numbers + symbols
elif symbols_wanted == "n":
    string = string
    pass
else:
    print("Please enter a valid value")
    exit()

password = ''.join(random.choice(string) for _ in range(lenght))

if lower and upper and numbers in password: 
    pass
else:
    password = ''.join(random.choice(string) for _ in range(lenght))

textfile = input("Want you to write it in a text file ? (y/n) ")

if textfile == "y":
    file = open("password.txt", "w+")
    file.write(password)
    file.write(password)
elif textfile == 'n':
    print("Your new password is : " + password)
    time.sleep(1000)