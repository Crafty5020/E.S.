import os
import sys
from time import sleep
from src.modules.clear_term import clear

def quiz():
    print("___________________________________________________________")
    print("Starting Quizzie...")
    sleep(1)
    ("-----------------------------------------------------------")
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
    
    if creator == 1:
        selector(True)
    else:
        selector(False)

def create():
    pass

def selector(Creator: bool):

    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
        quizzes = os.path.join(application_path, 'quizzes')
    elif __file__:
        quizzes = os.path.join(sys.path[0], 'quizzes')

    if not os.path.exists(quizzes):
        os.makedirs(quizzes)
    
