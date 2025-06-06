
import random
from data import data
import art
print(art.logo)
def select():
    """Select random data from list data and return it."""
    my_dict=random.choice(data)
    return my_dict
A=select()
B=select()
if A==B:
    B=select()
def compare():
    """COMPARE THE FOLLOWERS OF THE PERSONALITIES AND GIVE  SCORE"""
    score=0
    end=False
    while not end:
        global A
        global B
        print("*****WELCOME TO HIGHER LOWER GAME*******")
        key_to_find=["name","description","country"]
        a_data=[A[k] for k in key_to_find if k in A]

        b_data=[B[k] for k in key_to_find if k in B]
        print(f"A : {a_data}")
        print(art.vs)
        print(f"B : {b_data}")

        user=input("Enter who is more famous A or B :").upper()
        if user=="A" and A["follower_count"]>B["follower_count"]:
            print("YOU WON")
            score+=1
            print(f"Your score is{score} ")
            A=A
            B=select()
        elif user=="B" and A["follower_count"]<B["follower_count"]:
            print("YOU WON")
            score += 1
            print(f"Your score is{score} ")
            A = B
            B = select()
        else:
            print("You lose")
            end=True
    print(f"Your current score is {score}")
compare()







