from asyncore import write
import random
import time


lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'

string = lower + upper + numbers
lenght = int(input("Lenght of the password : "))
password = ''.join(random.choice(string) for _ in range(lenght))

writetext = input("Want you to write it in a text file ? (y/n) ")
file = open("password.txt", "w+")

if writetext == "y" or "yes" or "Y" or "YES":
    file.write(password)
    file.write(password)
    pass
else:
    print("Your new password is : " + password)
    time.sleep(1000)

