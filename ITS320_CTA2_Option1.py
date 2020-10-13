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
# Develop a Python application that incorporates using appropriate data types and provides program output in a logical manner.  Your program should prompt a user to enter a car brand, model, year, starting odometer reading, an ending odometer reading, and the estimated miles per gallon consumed by the vehicle. Store your data in a dictionary and print out the contents of the dictionary.

car_brand 			= print("Please provide your vehicle's Make:" str(input())\n)

car_model 			= print("Please provide your vehicle's Model:"  str(input())\n)

car_year 			= print("Please provide your vehicle's make:" int(input())\n)

car_odo_start 	= print("Please provide your vehicle's mileage at purchase:" int(input())\n)

car_odo_end	= print("Please provide your vehicle's mileage currently:" int(input())\n)

car_mileage			= print("Please provide your vehicle's average mileage:" float(input())\n)

print("\tPlease verify the information noted below.\n"\
	"\tYou have identified your vehicle's year, make, and model as,\n"\
	"\ta \t %d %s %s.\n"\
	"\tAdditionally, you identified your mileage at purchase as %d,\n"
	"\tand the current mileage as of today as, %d."
	"\tFinally, you have indicated your average mileage of the vehicle\n"\
	"\tas being approximately %f per gallon."
	% (car_year,car_brand,car_model,car_odo_start,car_odo_end,car_mileage)
)