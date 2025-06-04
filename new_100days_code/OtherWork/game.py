
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choice=int(input("Choose 0 for rock ,1 for paper and 2 for scissor:"))
x=[rock,paper,scissors]
import random
compare=random.choice(x)
if choice==0:
    print(rock)
    if compare == x[0]:
        print(rock)
        print("Draw")
    elif compare == x[1]:
        print(paper)
        print("Loose")
    else:
        print(scissors)
        print("Win")
elif choice==1:
    print(paper)
    if compare == x[0]:
        print(rock)
        print("Win")
    elif compare == x[1]:
        print(paper)
        print("Draw")
    else:
        print(scissors)
        print("Loose")
else:
    print(scissors)
    if compare == x[0]:
        print(rock)
        print("Loose")
    elif compare == x[1]:
        print(paper)
        print("Win")
    else:
        print(scissors)
        print("Draw")
print("*******************GAME OVER********************")