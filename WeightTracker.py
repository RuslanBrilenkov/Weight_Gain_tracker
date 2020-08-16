# importing necessary libraries
import numpy as np
import datetime
import os, sys

# defining the function
def WeightTracker():
	# very simple docstring file
	"""
	This is a help doc
	
	To EXIT/QUIT interactive mode - press "q"
	
	This function is waiting for additional 
	command-line (terminal) argument upon call.
	
		python <this code>.py <kg>
	e.g., 
		python WeightTracker.py 67.8
	
	Otherwise an exception is thrown.
	~~~
	Good luck and have a nice day!
	"""
	
	# current date time
	currentDT = datetime.datetime.now()
	# try-catch block for catching errors:
	try:
		# reading a weight value from command-line
		daily_kg = sys.argv[1]
		# appending array of weight values
		mass_array = []
		mass_array.append(daily_kg)
		# defining a file name for a file
		filename = "My_weight_gain.txt"
		
		# checking if file exists from before
		if os.path.isfile(filename):
			print("file exists\nappending with provided data")
			# writing down a weight value in a file
			with open(filename, "a") as file:
				file.write("{:>20} {:>20}\n".format(str(currentDT), daily_kg))
		else:
			# if file does not exist, creating it with a header
			# and writing 
			print("file does not exists\ncreating {}".format(filename))
			with open(filename, "w") as file:
				file.write("{:>20} {:>20}\n".format("Time", "Mass (kg)"))
				file.write("{:>20} {:>10}\n".format(str(currentDT), daily_kg))
	except Exception as e:
		# in case an Exception/Error arises, do the following:
		print("\nError: {}\n".format(e))
		messageFromDeveloper = "You need to provide the mass in (kg) as the first argument as \npython <this code>.py <kg>"
		print(messageFromDeveloper.ljust(40, '-'))
		messageFromDeveloper2 = "\nFor more help type\nprint(WeightTracker.__doc__)\nor\nhelp(WeightTracker)"
		print(messageFromDeveloper2.ljust(40, '-'))

if (__name__ =="__main__"):
	#print(WeightTracker.__doc__)
	#help(WeightTracker)
	WeightTracker()
