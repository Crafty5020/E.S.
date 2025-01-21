import os
import sys
from time import sleep
from src.modules.clear_term import clear
import json
import pathlib

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
    new = False
    dele = False


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
                c = int(input("1 to delete, and 2 to make a new quizz: "))
                if c > 2 or c < 1:
                    print("___________________________________________________________")
                    print("ERROR: value must be from 1 to 2")
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
            new = True
        elif c == 1:
            dele = True

    if new != True:
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
                create(False, f, dele, new)
                break
    else:
        clear()
        print("Creating new quizz...")
        sleep(2)
        create(False, "", dele, new)

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
        reset = input("To yo wan't to reset quizzie?(Y, N): ").strip().lower()
        creator = input("To you want to activate the creator?(Y, N): ").strip().lower()
        if reset != "y" and reset != "n" and creator != 'y' and creator != 'n':
            print("___________________________________________________________")
            print("ERROR: value must be Y or N")
            print("___________________________________________________________")
            sleep(1)
            continue
        break

    clear()
    if reset == "y":

        if creator == 'y':
            creator = True
        else:
            creator = False
        selector(creator)
    else:
        print("Returning to main menu")
        sleep(1)
        import src.modules.main as main

        main.start()

def create(empty: bool, file: str, delete: bool, new: bool):
    quiz_content = {}

    clear()
    if empty == True or file == "" or new == True:
        quiz = input("What to you wanna name your quizz: ")
        quiz = os.path.join(quizzesf, quiz)
        quiz_data = open(quiz, "w+")
        empty = False
        file = quiz
    else:
        quiz = os.path.join(quizzesf, file)
        with open(quiz, 'r') as quiz_data:
            pass
    
    if delete == False:
        while True:
            try:
                countidy_questions = int(input("How many questions to you"
                                        + " wan't your quiz to be?: "))
                break
            except ValueError:
                print("___________________________________________________________")
                print("ERROR: value must be an integer(a number without decimal point)")
                print("___________________________________________________________")

    if delete == True:
        print("Deleting quizz...")
        sleep(2)
        clear
        pathlib.Path.unlink(quiz)
        while True:
            clear()
            reset = input("To you wan't to go back to the selector?(Y, N): ").strip().lower()
            if reset != "y" and reset != "n":
                print("___________________________________________________________")
                print("ERROR: value must be Y or N")
                print("___________________________________________________________")
                sleep(1)
                continue
            break
        while True:
            clear()
            resetc = input("To you wan't to use the creator?(Y, N): ").strip().lower()
            if resetc != "y" and resetc != "n":
                print("___________________________________________________________")
                print("ERROR: value must be Y or N")
                print("___________________________________________________________")
                sleep(1)
                continue
            break
        if reset == "y" and resetc == "y":
            selector(True)
            return
        elif reset == "y" and resetc == "n":
            selector(False)
            return
        else:
            print("Returning to main menu...")
            sleep(2)
            import src.modules.main as main

            main.start()
            return


    if delete == False:
        for question_number in range(countidy_questions):
            quiz_content[str(question_number)] = {}
            question_number_print = question_number + 1
            while True:
                clear()
                print(quiz_content)
                type_question = input("What type of question to you wan't your " + str(question_number_print) + " question be?(Multiple Choice, Question): ").strip().lower()
                if type_question != "multiple choice" and type_question != "question" and type_question != "choice":
                    print("___________________________________________________________")
                    print("ERROR: value must be multiple choice or question")
                    print("___________________________________________________________")
                    sleep(1)
                    continue
                break
            
            if type_question == "multiple choice":
                type_question = "choice"

            quiz_content[str(question_number)]['type'] = type_question
        
            clear()
            question = input("What question to you wan't your " + str(question_number_print) + "question be?: ")

            quiz_content[str(question_number)]['question'] = question

            if type_question == "choice":
                options = {}
                for letter in ['a', 'b', 'c', 'd']:
                    clear()
                    option = input("What's the option for letter " + letter + ": ")
                    options[letter] = option
                while True:
                    clear()
                    print(options)
                    print("-----------------------------------------------------------")
                    answer = input("Which of the following options are the correct answer?: ").strip().lower()
                    if not answer in ['a', 'b', 'c', 'd']:
                        print("___________________________________________________________")
                        print("ERROR: value is not any of the options (a, b, c, d)")
                        print("___________________________________________________________")
                        continue
                    break
                
                quiz_content[str(question_number)]["answer"] = answer
                quiz_content.update([str(question_number)][options])
            else:
                clear()
                answer = input("What the answer of the question?: ")
                quiz_content[str(question_number)]["answer"] = answer
            
            json.dump(quiz_content, quiz_data)
            quiz_data.close()
            clear()
            print("Creation process finished")
            sleep(1)
            print("-----------------------------------------------------------")
            print("Returning to main menu...")
            import src.modules.main as main

            main.start()
    else:
        while True:
            r = input("To you wan't to return to main menu or select a quizz?(Main, Selector): ").strip().lower()
            if r != "main" and r != "selector":
                print("___________________________________________________________")
                print("ERROR: value must be 'Main' or 'Selector'")
                print("___________________________________________________________")
                continue
            break
        
        if r == "main":
            import src.modules.main as main

            main.start()
        else:
            selector(False)
        
        

            




        