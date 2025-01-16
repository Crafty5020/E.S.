#Imports
from time import sleep
from main import start

#Starts the app
def starter():
	print("___________________________________________________________")
	print("Hello and welcome to Estudy Surfing version Stage 0.2")
	sleep(1)
	print("-----------------------------------------------------------")
	start()

#Checks if whe started the proggram and not using the imports
if __name__ == "__Loader__":
	starter()