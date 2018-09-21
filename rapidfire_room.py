""" Rapid fire room module"""
import time
import config

def rapidfire_room():
    """Rapid fire Q&A room"""
    print("You enter a room with a TV on the wall.")
    print("The screen says: Welcome to your doom!")
    print("""You can not escape this room until you answer 5 questions correctly in the given time.
    \nEach wrong answer will cost you dearly""")

    parts = ["a finger", "a toe", "hand", "leg", "nose", "ear"]

    with open("questions_rfroom.txt", encoding="utf-8") as file:
        questions = [q.strip() for q in file]
    with open("answers_rfroom.txt", encoding="utf-8") as file:
        answers_rfroom = [a.strip() for a in file]

    print("Life: ", config.Life)
    print("Ready? Press Enter to start")
    try:
        input()#If Enter is pressed only then process
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
                rem_time = timer-(end_time - start_time)
                print("Remaining Time: ", round(rem_time, 0), "secs")
                print("Life: ", config.Life)
            elif answers_rfroom[j1] not in rfans and timer > 0 and config.Life > 0:
                print("Wrong answer! A saw is thrown in the room.")
                print("TV says: CUT a body part.")
                time.sleep(2)
                print("You cut your %s. Great!" % (parts[j1]))
                del parts[j1]
                config.Life = config.Life - 2
                print("Life remaining", config.Life)
                end_time = time.time()
                rem_time = timer - (end_time - start_time)
                print("Remaining Time: ", round(rem_time, 0), "secs")
                time.sleep(2)
            elif timer == 0:
                print("OOPS! The time has run out. Now You DIE!")
                time.sleep(2)
                print("The ceiling falls on you and kills you! Great Job!")
                config.Life = 0
                print("Life: ", config.Life)
            elif config.Life == 0 or j1 > 5:
                time.sleep(2)
                print("Your Life is 0. You have died!")
                break
            else:
                print("You died!")

    except KeyboardInterrupt:
        print("Learn to type!")
        exit(0)

rapidfire_room()
