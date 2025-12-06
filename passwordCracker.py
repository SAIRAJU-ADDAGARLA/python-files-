from random import *
import os
u_pwd = input("enter a password")
pwd=['1','2','3','4','5','6','7','8','9','0']
pw=""
while(pw!=u_pwd):
    pw=""
    for letter in range(len(u_pwd)):
        guess_pwd = pwd[randint(0,9)]
        pw=str(guess_pwd)+str(pw)
        print(pw)
        print(" cracking password....please wait")
        os.system("cls")
print("your password is  :",pw)
