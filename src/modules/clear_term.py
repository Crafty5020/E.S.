import os

def clear():
    lambda: os.system('cls' if os.name == 'nt' else 'clear')
