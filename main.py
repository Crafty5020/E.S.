#imports
from time import sleep

#Modules
import modules.studytime as st
import modules.quizzie as q


def start():
	#Asks user what app they wan't to use any of the modules or close the app
	while True:
		try:
			selec = int(input("Input 0 to close app, 2 for study time anylizer: "))
			#Checks if what user inputed is in range
			if selec < 0 or selec > 2:
				print("___________________________________________________________")
				print("ERROR: value must be in the range from 0 to 2")
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
	elif selec == 2:
		q.quiz()

#Closes the app
def close():
	print("___________________________________________________________")
	print("Ill see you later!")
	print("___________________________________________________________")
	sleep(0.5)
	exit()