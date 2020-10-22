# python3 (3.6)
# Coded on iPad Pro 2020 4th Generation
# Pythonista an Apple iPad App
# MIT License Copyright (c) 2020 Rogelio Fiorenzano
#
# ITS320: Basic Programming
# Colorado State University Global
# Dr. Joe Turano

# Option #2: Create a Python Application
# Assignment Instructions
#
# Implement a program that reads in a year and outputs the approximate value of a Ferrari 250 GTO in that year. Use the following table that describes the estimated value of a GTO at different times since 1962.

# Below is an outline of years and values for the Ferrari 250 GTO.

price_group_1 = 18500		# Price for Years 1962-1964

price_group_2 = 6000		# Price for Years 1965-1968

price_group_3 = 12000		# Price for Years 1969-1971

price_group_4 = 48000		# Price for Years 1972-1975

price_group_5 = 200000		# Price for Years 1976-1980

price_group_6 = 650000		# Price for Years 1981-1985

price_group_7 = 35000000	# Price for Years 1986-2012 (Holy cow what a spike!)

price_group_8 = 52000000	# Price for Years 2013-2014 (If you can afford this, your fireplace burns money)


# Provide initial instruction for input method and character type

print("Car manufacture year should be input as a 4-digit year. Example: 1980")

# Begin acquiring year from input

year = int(input("Please input the year of your pretentious display car ownership:\n"))

if year is 