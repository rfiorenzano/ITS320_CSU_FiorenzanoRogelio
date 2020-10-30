# python3 (3.6)
# Coded on iPad Pro 2020 4th Generation
# Pythonista an Apple iPad App
# MIT License Copyright (c) 2020 Rogelio Fiorenzano
#
# ITS320: Basic Programming
# Colorado State University Global
# Dr. Joe Option #1: Repetition Control Structure - Five Floating Point Numbers

# Assignment Instructions
# Write a program that utilizes a loop to read a set of five floating-point values from user input. Ask the user to enter the values, then print the following data:

# Total
# Average
# Maximum
# Minimum
# Interest at 20% for each original value entered by the user.
# Use the formula: Interest_Value = Original_value + Original_value*0.2

# Welcoming my Professor to a unique experience

print("Thank you for choosing to bank with the Fiorezano's at\n\n"
			"Financial Fractions Factored Further From Fine Fellows (F7)\n\n"
			"          Where YOUR dollar becomes OUR Dollar,\n\n"
			"             and WE DO with YOUR Dollar what\n\n"
			"                        YOU\n\n"
			"                        WISH\n\n"
			"                        YOU\n\n"
			"                       COULD!\n\n"
			)

# Assigning CTA Variables for Review

int_rate = 20 # Interest variable to be calculated against user input
interest = (int_rate/100)

# Creating an empty investment list to capture user inputs and later calculate total 
investments = [] 

# Number of Cash Deposit (CD) Investments as user inputs 
cds = int(input("Please enter number of Cash Deposits (CD) planned for investing:  ")) 

print("\nYou have chosen to invest in %d CDs with F7\n" % (cds))

print("Please enter the cash US Dollar ($USD) amount for each CD investment in WHOLE $USD without change. (Example: 1000)")

# for loop Cash Deposit ("cds") iterations until user inputs complete. Per assignment example "5" would be an option.

for i in range(0,cds):
	cd = int(input("\n$USD amount for 'CD Investment %d':  " % (i+1)))
	investments.append(cd) # adding each CD to "investments" and eventually used in "total"


# Provide information about the investors CDs amounts

print("\n\nAll of your planned CDs initial investments values are in whole $USD at:")
print(investments)


# Assignment check on investors CDs "Total"

total = (sum(investments))
print("\n\nFor a total $USD initial investment amount of:  $%d USD" % (total))


# Assignment check on investors CDs "Average"

average = int(total/cds)
print("\n\nYour Average investment amount is:  $%d USD" % (average))


# Assignment check on investors CDs "Maximum"

maximum = max(investments)
print("\n\nYour Maximum investment amount is:  $%d USD" % (maximum))


# Assignment check on investors CDs "Minimum"

minimum = min(investments)
print("\n\nYour Minimum investment amount is:  $%d USD" % (minimum))


# Assignment check on investors CDs "Interest"

valuation = total + int(total*interest)
print("\n\nYour CD investments will increase at a percentage of %d%% and at the end of terms will be valued at:  $%d USD" % (int_rate,valuation))


# Continue to amuse Professor

print("\n\nWe here at F7 will on the otherhand own mansions and yachts off of your hard earned savings! Thank you for supporting our desired life style. #WeAreNotRecessionProof")