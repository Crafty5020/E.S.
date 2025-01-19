import os
import sys
from time import sleep
from src.modules.clear_term import clear
import json

if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
    quizzesf = os.path.join(application_path, 'quizzes')
elif __file__:
    quizzesf = os.path.join(sys.path[0], 'quizzes')

if not os.path.exists(quizzesf):
    os.makedirs(quizzesf)

quizzes = os.listdir(quizzesf)

def quiz():
    print("___________________________________________________________")
    print("Starting Quizzie...")
    print("-----------------------------------------------------------")
    sleep(1)

    while True:
        try:
            clear()
            creator = int(input("Enter 1 to use the creator or 2 if not(1, 2): "))
            if creator < 1 or creator  > 2:
                print("___________________________________________________________")
                print("ERROR: value must be 1 or 2")
                print("___________________________________________________________")
                sleep(1)
                continue
            break
        except ValueError:
            print("___________________________________________________________")
            print("ERROR: value must be an integer(a number without decimal point)")
            print("___________________________________________________________")
            sleep(1)
    
    clear()
    if creator == 1:
        selector(True)
    else:
        selector(False)


def selector(Creator: bool):

    if len(quizzes) == 0 and Creator == False:
        clear()
        print("Looks like you didn't create any quizzes.")
        print("-----------------------------------------------------------")
        sleep(1)
        while True:
            o = input("To you wan't to create a quiz?(Y, N): ").strip().lower()
            if o != "y" and o != 'n':
                print("___________________________________________________________")
                print("ERROR: value must be Y or N")
                print("___________________________________________________________")
                sleep(1)
                print("-----------------------------------------------------------")
            else:
                break
    
        if o == 'y':
            create(True, "", False, False)
            return
        else:
            clear()
            print("Returning to main menu")
            sleep(1)
            import src.modules.main as main

            main.start()
            return
    clear()
    if Creator == True:
        print("You activated the creator for quizzes")
        print("-----------------------------------------------------------")
        sleep(1)
        while True:
            try:
                clear()
                c = int(input("Enter 1 for the creator," 
                             + "2 to rename a quizz, and 3 to delete: "))
                if c > 3 or c < 1:
                    print("___________________________________________________________")
                    print("ERROR: value must be from 1 to 3")
                    print("___________________________________________________________")
                    sleep(1)
                    continue
                break
            except ValueError:
                print("___________________________________________________________")
                print("ERROR: value must be an integer(a number without decimal point)")
                print("___________________________________________________________")
                sleep(1)
    
        clear
        if c == 2:
            ren = True
        elif c == 3:
            dele = True

    print("You have " + str(len(quizzes)) + " quizzes")
    sleep(1)
    while True:
        clear()
        quizzesl = os.scandir(quizzesf)
        for entry in quizzesl:
            if entry.is_dir() or entry.is_file():
                print(entry.name)
        print("-----------------------------------------------------------")
        f = input("Type the name of one of those quizzes to run a quizz: " )
        if not f in quizzes:
            print("___________________________________________________________")
            print("ERROR: No quizz called " + f + " exists")
            print("___________________________________________________________")
            sleep(1)
            continue
        elif Creator == False:
            run(f)
            break
        else:
            create(False, f, ren, dele)
            break

def run(quizz: str):
    q = os.path.join(quizzesf, quizz)

    with open(q, 'r') as file:
        quiz_data = json.load(file)

    score = 0
    letters = ['a', 'b', 'c', 'd']

    while True:
        clear()
        o = input("To you wan't the questions to be random or not?(Y, N): ").strip().lower()
        if o != "y" and o != "n":
            print("___________________________________________________________")
            print("ERROR: value must be Y or N")
            print("___________________________________________________________")
            sleep(1)
            continue
        break
    
    question_keys = list(quiz_data)
    if o == "y":
        import random
        random.shuffle(question_keys)
    

    for key in question_keys:
        question = quiz_data[key]

        clear()
        
        if question['type'] == 'question':
            prompt = input(question['question'] + ": ")

            if prompt == question['answer']:
                print("You are correct!")
                sleep(1)
                score += 1
            else:
                print("You are incorrect! The correct answer is " + question["answer"])
                sleep(1)

        if question['type'] == 'pick':
            print(question['question'])
            for option in letters:
                print(option + ': ' + question[option])
            
            while True:
                prompt = input("Input a, b, c, or d based on the options above: ").strip().lower()
                if not prompt in letters:
                    print("___________________________________________________________")
                    print("ERROR: value is not any of the options (a, b, c, d)")
                    print("___________________________________________________________")
                    continue
                break

            if prompt == question["answer"]:
                print("You are correct!")
                sleep(1)
                score += 1
            else:
                print("You are incorrect! The correct answer is " + question["answer"])
                sleep(1)
    
    clear()
    print("Quizz complete!")
    print("You got " + str(score) + " out of "
            + str(len(quiz_data)) + " which is %"
            + str(score/len(quiz_data)) + " in percentage")
    sleep(2)
    print("-----------------------------------------------------------")
    while True:
        reset = input("To yo wan't to reset quizzie(Y, N): ")
        if reset != "y" and reset != "n":
            print("___________________________________________________________")
            print("ERROR: value must be Y or N")
            print("___________________________________________________________")
            sleep(1)
            continue
        break

    clear()
    if reset == "y":
        selector()
    else:
        print("Returning to main menu")
        sleep(1)
        import src.modules.main as main

        main.start()

def create(empty: bool, file: str, rename: bool, delete: bool,):
    clear()
    if empty == True:
        q = input("What to you wanna name your quizz: ")
        q = os.path.join(quizzesf, q)
        with open(q, 'a'):
            pass