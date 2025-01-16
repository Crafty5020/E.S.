#imports
from time import sleep


import modules.studytime as st
import modules.quizzie as q


def start():
	#Asks user what app they wan't to use any of the modules or close the app
	while True:
		try:
			selec = int(input("Input 0 to close app, 1 for study time anylizer, 2 for quizzie: "))
			#Checks if what user inputed is in range
			if selec < 0 or selec > 2:
				if selec != 2853 or selec != 1234:
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
		#Intis module studytime
		import modules.studytime as st
		st.study()
	elif selec == 2:
		#Intis module quizzie
		import modules.quizzie as q
		q.quiz()
	elif selec == 2853:


#Closes the app
def close():
	print("___________________________________________________________")
	print("Ill see you later!")
	print("___________________________________________________________")
	sleep(0.5)
	exit()