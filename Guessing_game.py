#!/usr/bin/python3.6
import random

num=0
num1=0
uns="None"
print("we starting number guesing game")

def checknum(num,num1):
    if num >100 or num < 0:
        print("wrong number range please try agane")
        reqnum(num,num1)
    elif num1 != 0:
        game(num,num1)
    else:
        gennum(num,num1)
        return 

def checkuns(uns):
    if uns == "Yes" or uns == "YES" or uns == "yes" or uns == "y" or uns == "Y":
       num1=0
       reqnum(num,num1)
    else:
       return

def reqnum(num,num1):
    num=int(input("please enter number between 0 and 100 : "))
    checknum(num,num1)
    return

def gennum(num,num1):
    num1=random.randint(0,100)
    game(num,num1)
    return

def game(num,num1):
    if num > num1:
        print("gues lower")
        reqnum(num,num1)
    elif num < num1:
        print("gues higher")
        reqnum(num,num1)
    else:
        print("good gues")
        uns=input("do you want play agane ?  ")
        checkuns(uns)
    return
reqnum(num,num1)