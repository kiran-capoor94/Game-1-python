"""Labrynth Room for the Survival Horror
Game made by Author: Kiran Capoor"""

i = 1
j = -1
k = ["Red are apples, _______ are oranges", "2 into 2 is 4, _________ into _______ is 16"]

for i in range(1, 3):
    #This loop will run only till the condition is met.
    i = i + 1
    j = j + 1
    print("You enter a room full of rooms aka a labrynth.")
    print(("""There is but one way
    To break the spell. And only 2 chances.
    You will fall in a pit to your doom upon loss of
    your chances.

    Clues: 
    
    Comeplete the phrase:
    %s
    *Enter in lowercase only""")%(k[j]))
    clue = input("Enter the answer : ")

    if clue == "orange" or clue == "4" and i <= 3:
        print("You are Right. The Answer is %s " % (clue))
        break
    elif clue != "oranges" or clue != "minime" or clue != "mini me" and i < 2:
        print("\nOops! Try again!")
    elif i > 3:
        print("You fell a 100ft to your death on a Bed of Razors! Ouch!")
        break
