#Imports
from time import sleep
import main

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
				classes = int(input("How many classes to you plan to study?: "))
				if classes <= 0:
					print("___________________________________________________________")
					print("ERROR: value must be a positive value or not be 0")
					print("___________________________________________________________")
					continue
				break
			except ValueError:
				print("___________________________________________________________")
				print("ERROR: value must be an integer(a number without decimal point)")
				print("___________________________________________________________")
		print("-----------------------------------------------------------")

		#Asks user some questions
		while True:
			try:
				hours = float(input("How much time to you wan't to study?(In hours): "))
				if hours <= 0:
					print("___________________________________________________________")
					print("ERROR: value must be a positive value or not be 0")
					print("___________________________________________________________")
					continue
				break
			except ValueError:
				print("___________________________________________________________")
				print("ERROR: value must be a number")
				print("___________________________________________________________")
		print("-----------------------------------------------------------")

		#Runs the math
		stime(hours, classes)
		sleep(0.2)

		#Asks user if they wan't to use module again
		repeat = input("To you wan't to repeat the study time anylizer?" + "(Y,N): ").strip().capitalize()
		if repeat == "Y" or repeat == "YES":
			print("-----------------------------------------------------------")
			continue
		else:
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
		print("-----------------------------------------------------------")
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
		print("-----------------------------------------------------------")

#When loop breaks go to main.py
main.start()