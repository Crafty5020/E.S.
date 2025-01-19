#Imports
import src.modules.main as main
from time import sleep
import sys
import os
from src.modules.clear_term import clear

#Starts the app
def starter():
	if getattr(sys, 'frozen', False):
		os.chdir(sys._MEIPASS)
	print("___________________________________________________________")
	print("Hello and welcome to Estudy Surfing version Stage 0.2")
	sleep(1)
	print("-----------------------------------------------------------")
	clear()
	main.start()

#Checks if whe started the proggram and not using the imports
if __name__ == "__main__":
	starter()