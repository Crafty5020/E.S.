#Imports
from time import sleep
from src.modules.clear_term import clear

#Main function
def study():
	print("___________________________________________________________")
	print("Starting Study Time Analyzer...")
	sleep(1)
	print("-----------------------------------------------------------")
	#In a loop to make reusability
	while True:
		#Resets variables for reusability
		hours = 1.0
		classes = 5
		repeat = ""

		#Asks user some questions
		while True:
			try:
				clear()
				classes = int(input("How many classes to you plan to study?: "))
				if classes <= 0:
					print("___________________________________________________________")
					print("ERROR: value must be a positive value or not be 0")
					print("___________________________________________________________")
					sleep(0.5)
					continue
				break
			except ValueError:
				print("___________________________________________________________")
				print("ERROR: value must be an integer(a number without decimal point)")
				print("___________________________________________________________")
				sleep(0.5)

		#Asks user some questions
		while True:
			try:
				clear()
				hours = float(input("How much time to you wan't to study?(In hours): "))
				if hours <= 0:
					print("___________________________________________________________")
					print("ERROR: value must be a positive value or not be 0")
					print("___________________________________________________________")
					sleep(0.5)
					continue
				break
			except ValueError:
				print("___________________________________________________________")
				print("ERROR: value must be a number")
				print("___________________________________________________________")
				sleep(0.5)

		clear()
		#Runs the math
		stime(hours, classes)
		sleep(1)

		#Asks user if they wan't to use module again
		clear()

		repeat = input("To you wan't to repeat the study time anylizer?(Y,N): ").strip().capitalize()
		if repeat == "Y" or repeat == "YES":
			continue
		else:
			#Load the main script for main menu
			import src.modules.main as main

			#When loop breaks go to main.py
			clear()
			main.start()
			break

def stime(hours: float, classes: int):

	#Calculates the time in minutes
	time = 60 * (hours / classes)

	#Detects if time is way to big in minutes then use hours
	if time < 60.0:

		#Makes time string to use len and "endswith"
		time = str(time)

		#Makes sure that number not that big
		if len(time) > 5:
			time = float(time)
			time = round(time, 2)
			time = str(time)

		#Simplyfies the number
		if time.endswith(".0"):
			time = float(time)
			time = int(time)
		else:
			time = float(time)
		
		#Uses correct grammer
		if time != 1:
			print("Study each class for " + str(time) + " minutes")
		else:
			print("Study each class for " + str(time) + " minutes")
	else:

		#Calculates time from minutes to hours
		time /= 60

		#Makes time string to use len and "endswith"
		time = str(time)

		#Makes sure that number not that big
		if len(time) > 5:
			time = float(time)
			time = round(time, 2)
			time = str(time)
		
		#Simplyfies the number
		if time.endswith(".0"):
			time = float(time)
			time = int(time)
		else:
			time = float(time)
		
		#Uses correct grammer
		if time != 1:
			print("Study each class for " + str(time) + " hours")
		else:
			print("Study each class for " + str(time) + " hour")
