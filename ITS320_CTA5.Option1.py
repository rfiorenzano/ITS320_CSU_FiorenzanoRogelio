# python3 (3.6)
# Coded on iPad Pro 2020 4th Generation
# Pythonista an Apple iPad App
# MIT License Copyright (c) 2020 Rogelio Fiorenzano
#
# ITS320: Basic Programming
# Colorado State University Global
# Dr. Joseph Turano

# Option #1: String Values in Reverse Order

# Assignment Instructions

# Write a Python function that will accept as input three string values from a user. The method will return to the user a concatenation of the string values in reverse order. The function is to be called from the main method.
# In the main method, prompt the user for the three strings.


# Area to define String Reversal




# Area to define Main

def main():

	print("Hello fellow user! Please provide your input when prompted. When done providing input, please type, "QUIT" to end capture of input.")
	
# Capture of user input and placing into a list for later reversal

usr_strings = []
	
	usr_str = input("Please provide your input here: ")
	if usr_str == "QUIT":
		print(usr_strings)
	else:
		usr_strings.append(usr_str)