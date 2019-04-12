#!/usr/bin/python2.7
-------------------------------------------------------------------
-------------------------------------------------------------------

#random module

#to enable module
import random 
print(random.randint(0,100))  #generates random and prints numbers in given range

-------------------------------------------------------------------
-------------------------------------------------------------------

#gassing game

import random

print("we starting gassing game")
num=input("please enter number between 0 and 100 : ")
num2=random.randint(0,100)
if num1 == num2:
    print("good gues!!!")
else:
    print("bad gues! the correct numbere are : " + num2)

