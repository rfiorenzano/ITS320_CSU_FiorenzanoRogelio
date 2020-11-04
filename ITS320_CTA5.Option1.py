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


# Capture of user input and placing into a list for later reversal

usr_strings = []

# Area to define String Reversal

def str_reversal():

# Special thanks to our LinkedIn video with kittens and reminding us to "return variable" for later use
	usr_strings.reverse() 
	return usr_strings
str_reversal()


# Area to define Main

def main():

	print("Hello fellow user! Please provide your input when prompted.\n\n\tSPECIAL NOTE!\n\nWhen done providing input, please type, \"QUIT\" to end capture of input.")
	
	# Special thanks to Thomas Streets Module 4 in developing my thoughts and decreasing my written code amount with the "while True:" advice for loops!
	
	while True:
		usr_str = input("\nPlease provide your input here: ")
		if usr_str == "QUIT":
			print("\n")
			print("Your original user inputs were: ", usr_strings)
			print("\n")
			print("Your original user inputs reversed are: ", str_reversal())
			break
		else:
			usr_strings.append(usr_str)

main()