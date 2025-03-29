#hangman game 

import hangarts
stages=hangarts.stages
logo=hangarts.logo
print(logo)
# choosing a random word:
import hangwords
word=hangwords.word_list
import random
choosen_word=random.choice(word)
#Creating a placeholder with same number of _ as the the letter in chosenword:
placeholder=''
for i in range(len(choosen_word)):
    placeholder+="_"
print(placeholder)

#creating the number of lives remained to user:
lives=6


#Asking user to guess a letter from choosen_word:
end=False
correct=[]
while end!=True:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess=(input("Guess the letter: ")).lower()
    display=''

#creating a variable display with guess letter at the write place and "_" at the remaining place
    if guess in correct:
        print(f"You already guessed the letter: {guess}")
    for letter in choosen_word:
        if letter == guess:
            display += guess
            correct.append(guess)
        elif letter in correct:
            display += letter
        else:
            display += "_"
        
            
    print(display)
#Tracking the lives:
    if guess not in choosen_word:
        lives-=1
        print(f" letter {guess} is not in choosen word :")
        print(f"Remaining lives {lives}")
        if lives==0:
            end=True
            print("Game over: ")
            
            print(f"***********************IT WAS {choosen_word} YOU LOSE**********************")
    
    print(stages[lives])
    if "_" not in display:
        end=True
        print("****************************YOU WIN****************************")
    
# printing the ascci art of the from the list stage
        
        
print(display)