# python3 (3.6)
# Coded on iPad Pro 2020 4th Generation
# Pythonista an Apple iPad App
# MIT License Copyright (c) 2020 Rogelio Fiorenzano
#
# ITS320: Basic Programming
# Colorado State University Global
# Dr. Joseph Turano

# Option #2: List Computations

# Assignment Instructions

# Compute the Cartesian product of two lists AxB where each list has no more than 10 numbers

# For example, if the user supplies the two input lists:
#    A = [1,2]
#    B = [3,4]

#    then the Cartesian product output should be:
#    AxB = [(1,3),(1,4),(2,3),(2,4)]

print("In mathematics, the Cartesian product of two sets A and B, is a new set of all items froms sets A and B combined as pairs.\n\nItems in set A are combined with items from set B when the Cartesian product is created.\n\nThe best way to describe this is to imagine a table with rows and columns.\n\nRows are made up from set A, and Columns from set B.\n\nA table can be created by taking the Cartesian product of the set of rows and set of columns.\n\n")


def main():

# Create empty lists for both Set A and Set B

	A = []
	B = []

# Create function for use to do Cartesian multiplication list
	
	def cartesian_multiplication(AB):
		if not AB:
			yield ()
		else:
			for newlist in AB[0]:
				for product in cartesian_multiplication(AB[1:]):
					yield (newlist,)+product  

# Create class to hold inputs to reduce the amount of code
	
	class Cartesian_Inputs:
			def __init__(self):
				self.list = 0
				self.items = []

# Begin coding of capture for user inputs and use of class

# Code for Set A

	alist = Cartesian_Inputs()
	alist.items = []
	A = alist.items

	while True:
		alist = int(input("\tPlease input the desired number of items for list A? Note: Please limit to a max of 10. "))
		
		if alist > 10:
			print("\n")
			print("Please limit items for list to 10 or less. Example: 1-10. ")
			print("\n")
			print("To 'QUIT' enter a negative number. Example: -1")
			print("\n")
			alist = int(input("Number of items in list A (10 max): "))

		elif alist < 0:
			print("Exiting program.")
			break

		else:
			print("\n")
			print("Please input items for List A")
			for i in range(alist):
				userinput = int(input(": "))
				A.append(userinput)
		break

# Code for Set B

	blist = Cartesian_Inputs()
	blist.items = []
	B = blist.items

	while True:
		blist = int(input("\n\tPlease input the desired number of items for B list? Note: Please limit to a max of 10. "))

		if blist > 10:
			print("\n")
			print("Please limit items for list to 10 or less. Example: 1-10.")
			print("\n")
			print("To 'QUIT' enter a negative number. Example: -1")
			print("\n")
			blist = int(input("Number of items in list B (10 max): "))
			
		elif blist < 0:
			print("Exiting program.")
			break
	
		else:
			print("\n")
			print("Please input items for List B")
			for i in range(blist):
				userinput = int(input(": "))
				B.append(userinput)
		break

# Code to output the product of both Set A & Set B

	print("\n")
	print("The Cartesian product of Sets A and B are listed below.\n")
	print("\t",list(cartesian_multiplication([A,B])))


main()