import os
import sys
from time import sleep
from src.modules.clear_term import clear

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
                sleep(0.5)
                continue
            break
        except ValueError:
            print("___________________________________________________________")
            print("ERROR: value must be an integer(a number without decimal point)")
            print("___________________________________________________________")
            sleep(0.5)
    
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
        sleep(0.5)
        while True:
            o = input("To you wan't to create a quiz?(Y, N): ").strip().lower()
            if o != "y" and o != 'n':
                print("___________________________________________________________")
                print("ERROR: value must be Y or N")
                print("___________________________________________________________")
                sleep(0.5)
                print("-----------------------------------------------------------")
            else:
                break
    
        if o == 'y':
            create(True)
            return
        else:
            clear()
            print("Returning to main menu")
            sleep(1)
            import src.modules.main as main

            main.start()
            return
    
    clear()
    print("You have " + str(len(quizzes)) + " quizzes")
    sleep(0.5)
    while True:
        clear()
        print(os.scandir(quizzesf))
        print("-----------------------------------------------------------")
        f = input("Type the name of one of those quizzes to run a quizz: " )
        if not f in quizzes:
            print("___________________________________________________________")
            print("ERROR: No quizz called " + f + " exists")
            print("___________________________________________________________")
        else:
            run()

def run(quizz: str)
    pass

def create(empty: bool, file: str):
    pass