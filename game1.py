"""Author: Agnt X, Game1.py is the main game script with several rooms
and a simplistic interface
https://www.pycon.it/conference/talks/developing-android-apps-completely-in-python

please enjoy!!"""

import time
import config

def gold_room():
    """Gold Room Functions"""
    print("You enter a room full of gold. Do you want to go inside? Press 1 for Yes and 0 for No.")

    next_step = input("> ")

    if "1" in next_step: # 10---true
        print("How much do you need?")
        how_much = input("> ")
        h_m = int(how_much)
    else:
        dead("Man, learn to type a number")

    if h_m <= 500:
        print(("You may take %d gold! You win!") %(h_m))
    else:
        print("\nYou greedy bastard, You stumble on a knife and die!")
        config.Life = 0
        print("Life: ", config.Life)

def bear_room():
    """Bear Room"""
    print("""Great job on passing the room, there is another door here.
    Do you want to enter? 
    There may be food here!
    Press 1 to enter.""")
    next_step = input("> ")

    if next_step == "1":
        print("\nThere is a bear with a pot of honey in front.")
        print("\nWhat do you do?")
        print("""There is a knife on your left and
        a sleeping dart on your right. 
        Which do you want?""")
        print("\nEnter 1 for knife and 0 for darts.")
        weapon = input("> ")

        if weapon == "1":
            print("Do you want to try to kill the bear with a knife. Press 1 for Yes and 0 for No.")
            kill = input("> ")

            if kill == "1":
                print("\nYou killed the bear but the bear chewed off your hand!")
                print("\nYou take the honey pot and eat to live another day.")
                print("\nYou see a door on your left. You enter.")
                config.Life = config.Life - 2
                print("You lose 2 Life points")
                rapidfire_room()
            else:
                print("Why did you even take the knife?")
                print("\nThe bear sees you and kills you")
                dead("Game Over")

        elif weapon == "0":
            print("Do you want to put the bear to sleep?")
            print("\nPress 1 for Yes and 0 for No")
            sleep = input("> ")

            if sleep == "1":
                print("\nGreat the bear is asleep. You take the pot and run away.")
                print("\nWow, the honey must be tasty.")
                print("\nYou see a door on your left. You enter as the bear might wake up")
                rapidfire_room()
            else:
                dead("\nWhy did you even take the darts? The bear sees you and rips your face off!")
        else:
            dead("You try to eat some rats and die a slow and painful death. Great Job!")
    else:
        labrinth()

def labrinth():
    """ Labrynth room"""
    i = 1
    j = -1
    k = ["Red are apples, _______ are oranges", "2 into 2 is 4, _________ into _______ is 16"]

    for i in range(1, 3):
        #This loop will run only till the condition is met.
        i = i + 1
        j = j + 1
        print("You enter a room full of rooms aka a labrynth.")
        print(("""
        There is but one way
        To break the spell. And only 2 chances.
        You will fall in a pit to your doom upon loss of
        your chances.

        Clues: 
        
        Comeplete the phrase:
        %s
        *Enter in lowercase only""") % (k[j]))
        clue = input("Enter the answer : ")

        if clue == "orange" or clue == "4" and i <= 3:
            print("You are Right. The Answer is %s " % (clue))
            break
        elif clue != "oranges" or clue != "4" and i < 2:
            print("\nOops! Try again!")
        elif i > 2:
            dead("You fell a 100ft to your death on a Bed of Razors! Ouch!")
    rapidfire_room()

def dead(why):
    """ Function defining DEATH command"""
    print(why, "Good Job!")
    exit(0)

def start():
    """The game begins here"""
    print("\nYou are in a Weird room. With grotesque pictures of dead men and Naked Women")
    print("\nThere are two doors, Blue and Red. Which one do you want to go in?")
    print("There is a warning sign: Beware of traps and good luck.")
    print("Life : %s" % config.Life)

    next_step = input("> ")

    if next_step == "blue" or next_step == "Blue":
        bear_room()
    elif next_step == "red" or next_step == "Red":
        labrinth()
    else:
        dead("\nYou stumbled on a knife and died. Great job!")


def rapidfire_room():
    """Rapid fire Q&A room"""
    print("You enter a room with a TV on the wall.")
    print("The screen says: Welcome to your doom!")
    print("""You can not escape this room until you answer 5 questions correctly in the given time.
    \nEach wrong answer will cost you dearly""")

    with open("questions_rfroom.txt", encoding="utf-8") as file:
        questions = [q.strip('Q:') for q in file]
    with open("answers_rfroom.txt", encoding="utf-8") as file:
        answers_rfroom = [a.strip('A:') for a in file]

    print("Life: ", config.Life)
    print("Ready? Press Enter to start")
    try:
        input()  # If Enter is pressed only then process
        timer = 60
        print("Started, please wait for 5 seconds for the TV to download.")
        print("As the internet here sucks. By the way you have only: ", timer, "secs")
        print("And Life: ", config.Life)
        i1 = 0
        for i1 in range(1, 6):
            print(i1)
            time.sleep(1.5)
        start_time = time.time()
        j1 = 0
        for j1 in range(0, 5):
            print("Here's your question: " + questions[j1])
            rfans = input("> ")

            if answers_rfroom[j1] in rfans and timer > 0 and config.Life > 0:
                print("Correct!")
                time.sleep(2)
                end_time = time.time()
                rem_time = timer - (end_time - start_time)
                print("Remaining Time: ", round(rem_time, 0), "secs")
                print("Life: ", config.Life)
            elif answers_rfroom[j1] not in rfans and timer > 0 and config.Life > 0:
                print("Wrong answer! A saw is thrown in the room.")
                print("TV says: CUT a body part.")
                time.sleep(2)
                print("You cut your %s. Great!" % (config.parts[j1]))
                del config.parts[j1]
                config.Life = config.Life - 2
                print("Life remaining", config.Life)
                end_time = time.time()
                rem_time = timer - (end_time - start_time)
                print("Remaining Time: ", round(rem_time, 0), "secs")
                time.sleep(2)
            elif timer == 0:
                print("OOPS! The time has run out. Now You DIE!")
                time.sleep(2)
                print("The ceiling falls and kills you! Great Job!")
                config.Life = 0
                print("Life: ", config.Life)
            elif config.Life == 0 or j1 > 5:
                time.sleep(2)
                print("Your Life is 0. You have died!")
                break
            else:
                dead("You died!")
    except KeyboardInterrupt:
        dead("Learn to type!")
    gold_room()

start()
