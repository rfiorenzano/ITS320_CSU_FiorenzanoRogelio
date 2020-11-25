# python3 (3.6.8)
# Coded on Windows 10 PC
# Microsoft Visual Studio Code - Open Source IDE Code-Server
# GitHub Repo: https://github.com/cdr/code-server
# MIT License Copyright (c) 2020 Rogelio Fiorenzano
#
# ITS320: Basic Programming
# Colorado State University Global
# Dr. Joe Turano

# Option #1: Program Corrections, Lessons Learned, and Vehicle Inventory Program
# Assignment Instructions
#
# Final program:
# Create a final program that meets the requirements outlined below.
# 
# 	Create an automobile class that will be used by a dealership as a vehicle inventory program.
# 	The following attributes should be present in your automobile class:
# 	private string make
# 	private string model
#	private string color
# 	private int year
# 	private int mileage

# Your program should have appropriate methods such as:
# 
# 	constructor
# 	add a new vehicle
# 	remove a vehicle
# 	update vehicle attributes

# At the end of your program, it should allow the user to output all vehicle inventory to a text file.
# 
# Your final program submission materials must include your source code and screenshots of the 
# application executing the application and the results.

print("""
    
    Hello Billy Bob's New & Used Car Dealership Employee! I hope you are having a diddly do right day!
    This here is our con-pewter system where we work to get our inventory sichee-ated! Geet er dun!!!

                        Nah make sure yer readin' them instructions nah, ya hear!

	""")

def main():

	# Vehicle class to identify attributes
    class vehicle:
        def __init__(self):
            self.year = 0
            self.make = ""
            self.model = ""
            self.color = ""
            self.mileage = 0

	# Vehicle management 
        def add_vehicle(self):
            self.year = int(input("Please input vehicle's manufacture year (Example: 2010): "))
            self.make = str(input("Please input vehicle's make (Example: Ford): "))
            self.model = str(input("Please input vehicle's model (Example: Mustang): "))
            self.color = str(input("Please input vehicle's color (Example: Black or White): "))
            self.mileage = int(input("Please input vehicle's mileage (Example: 1500): "))

        def __str__(self):
            return (
                "%d %s %s Color: %s Mileage: %d" % 
                (self.year,self.make,self.model,self.color,self.mileage)
            )

        def edit(vehicle_inv):
            inv_item = (int(input("Which vehicle do you want to modify details for?: ")))
            new_inv = vehicle.add_vehicle
            new_inv = vehicle.__str__()
            vehicle_inv[pos-1] = new_inv
            print("Vehicle details updated.")

    vehicle_inv = []

    # Begin user interactive console 

    
    while True:
        try:
            print ("""
        1. Add a Vehicle
        2. Delete a Vehicle
        3. View Inventory
        4. Update Inventory
        5. Create Inventory File
        6. Quit

        Why not mash one of them keys and lemme know whacha wanna do? (Press 6 to quit):
		    """)

            user_input = ""
            user_input = int(input())

            while True:

                if user_input == 1: 
                    v = vehicle()
                    v.add_vehicle()
                    vehicle_inv.append(v.__str__())
                    break

                elif user_input == 2:
                    for i in vehicle_inv:
                        vehicle_inv.pop(int(input("Enter position of vehicle to remove: ")))
                        print("Successfully removed vehicle.")
                        raise IndexError
                        break

                elif user_input == 3:
                    for cars in vehicle_inv:
                        print(cars)
                    break

                elif user_input == 4:
                    edit(vehicle_inv)

# Making a call out against myself here - as I have not been able to get open()  to work for me at all :(
# I am not sure what I am doing wrong here.

                elif user_input == 5:
                    f = open('vehicle_inv.txt', 'w')
                    f.write(str(vehicle_inv))
                    f.close()
                    raise IOError

                elif user_input < 0:
                    raise ValueError

                elif user_input > 6:
                    raise ValueError

# Here is another area I have no succeeded in as well. I cannot get the application to actually quit.
# The menu is recycled and the script loops.

                elif user_input == 6:
                    print ("Adios amigo!")
                    break

        except ValueError:
            print ("Ya done goofed amigo! Pick a number definitely not a letter! Try again!")

        except IndexError:
            print ("Ya picked a car that doesn't exist amigo! Try again!")

        except IOError:
            print ("Sumtins wrong with your inventory file amigo! Try again or call IT!")

main()
