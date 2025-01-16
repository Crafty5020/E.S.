#imports
from time import sleep
import modules.studytime as st



def start():
	#Asks user what app they wan't to use any of the modules or close the app
	while True:
		try:
			selec = int(input("Input 0 to close app, 1 for study time anylizer: "))
			#Checks if what user inputed is in range
			if selec < 0 or selec > 1:
				print("___________________________________________________________")
				print("ERROR: value must be in the range from 0 to 1")
				print("___________________________________________________________")
				continue
			break
		except ValueError:
			print("___________________________________________________________")
			print("ERROR: value must be an integer(a number without decimal point)")
			print("___________________________________________________________")
	#checks for the number inputed to see what module to run
	if selec == 0:
		close()
	elif selec == 1:
		st.study()

#Starts the app	
def starter():
	print("___________________________________________________________")
	print("Hello and welcome to Estudy Surfing version Stage 0.1")
	sleep(1)
	print("-----------------------------------------------------------")
	start()

#Checks if whe started the proggram and not using the imports
if __name__ == "__main__":
	starter()

#Closes the app
def close():
	print("___________________________________________________________")
	print("Ill see you later!")
	print("___________________________________________________________")
	sleep(0.5)
	close()