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

car_brand = str(input("Please provide your vehicle's Make:\n"))
#car_brand 			= str(input())

car_model = str(input("\nPlease provide your vehicle's Model:\n"))
#car_model 			= str(input())

car_year = int(input("\nPlease provide your vehicle's year:\n")) 
#car_year 			= int(input())

car_odo_start = int(input("\nPlease provide your vehicle's mileage at purchase:\n"))
#car_odo_start 	= int(input())

car_odo_end = int(input("\nPlease provide your vehicle's mileage currently:\n"))
#car_odo_end	= int(input())

car_mileage = float(input("\nPlease provide your vehicle's average mileage:\n"))
#car_mileage			= float(input())

car_mileage_avg = str(round(car_mileage,2))

car_info = {
	'Brand': car_brand,
	'Model': car_model,
	'Year': car_year,
	'Starting Odometer': car_odo_start,
	'Ending Odometer': car_odo_end,
	'Estimated Mileage': car_mileage
}

print("\n\n This is the collected information for the car in dict type:\n\n")
print(car_info)

print("\n\n\tPlease verify the information noted below.\n"\
	"\tYou have identified your vehicle's year, make, and model as a:\n\n"\
	"\t\t %d %s %s\n\n"\
	"\tAdditionally, you identified your mileage at purchase as:\n\n"\
	"\t\t%d miles\n\n"\
	"\tand the current mileage as of today as:\n\n"\
	"\t\t%d miles\n\n"
	"\tFinally, you have indicated your average mileage of the vehicle\n"\
	"\tas being approximately:\n\n"\
	"\t\t %s/gallon"
	% (car_year,car_brand,car_model,car_odo_start,car_odo_end,car_mileage_avg)
)
