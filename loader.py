#Imports
import src.modules.main as main
from time import sleep

try:
	import pyi_splash as sp
	while sp.is_alive():
		sp.update_text('Loading Estudy Surfing')
	sp.close()
except ImportError:
	pass

#Starts the app
def starter():
	print("___________________________________________________________")
	print("Hello and welcome to Estudy Surfing version Stage 0.2")
	sleep(1)
	print("-----------------------------------------------------------")
	main.start()

#Checks if whe started the proggram and not using the imports
if __name__ == "__main__":
	starter()