#imports
from time import sleep



def start():
	#Asks user what app they wan't to use any of the modules or close the app
	while True:
		try:
			selec = int(input("Input 0 to close app, 1 for study time anylizer, 2 for quizzie: "))
			#Checks if what user inputed is in range
			if selec < 0 or selec > 2:
				if selec != 847250 or selec != 1234:
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
		import studytime as st
		st.study()
	elif selec == 2:
		#Intis module quizzie
		import quizzie as q
		q.quiz()
	elif selec == 847250:
		print("___________________________________________________________")
		print("Initializing rasberry mode")
		print("___________________________________________________________")

		sleep(1)
		while True:
			rasber = input("To you have a raspberry pi pico or the Sense HAT or both?(Sense, Pico, Both, or Nothing): ").strip().capitalize()

			if rasber != "SENSE" or rasber != "PICO" or rasber != "N" or rasber != "NOTHING" or rasber != "":
				print('ERROR: value must be "Pico", Sense, or "Nothing"')
			else:
				if rasber == "SENSE":
					rasber = 1
				elif rasber == "PICO":
					rasber = 2
				elif rasber == "BOTH":
					rasber = 3
				else:
					rasber = 0
				break
		
		import ras.rasb as r

		r.raspberry(rasber)


#Closes the app
def close():
	print("___________________________________________________________")
	print("Ill see you later!")
	print("___________________________________________________________")
	sleep(0.5)
	exit()