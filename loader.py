#Imports
import src.modules.main as main
from time import sleep


#Starts the app
def starter():
	clear()
	if getattr(sys, 'frozen', False):
		os.chdir(sys._MEIPASS)
	print("Hello and welcome to Estudy Surfing version Stage 0.2")
	sleep(1)
	clear()
	main.start()

#Checks if whe started the proggram and not using the imports
if __name__ == "__main__":
	starter()