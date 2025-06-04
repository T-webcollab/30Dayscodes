import random
from GUESS_LOGO import logo
print (logo)
num=random.randint(1,100)
print("WELCOME TO NUMBER GUESSING GAME")
def difficulty():
    choose=input("Enter difficulty level: HARD OR EASY: ").lower()
    if choose =="easy":
        return 10
    elif choose=="hard":
        return 5
    else:
        print("Wrong input")
        return 0
def check(chance):
    option=0
    while option<chance:
        guess=int(input("Make a guess: "))
        if guess==num:
            print("YOUR GUESS IS CORRECT\n******YOU WIN*******")
            return
        elif guess > num:
            print ("TOO HIGH")
        elif guess < num:
            print("TOO LOW")
        else :
            print("____YOU LOSE____")
        option+=1
        if option==chance and guess!=num:
            print("____YOU LOSE____")
            return
        print(f"YOU HAVE {chance-option} CHANCE REMAINING. ")

check(difficulty())