from Logic_classes.logic_wrapper import LogicAPI as logic
from Model_classes.Vehicle import Vehicle as vehicle


#def make_vehicle(ride):
#    print(vehicle(ride["ID"],ride["Vehicle name"],ride["Type"],ride["Manufacturer"],ride["Model"],ride["Color"],ride["age"],ride["tax"],ride["available"]))

class Non_Rvk():
    def __init__(self):
        self.employee_num = "69"
        self.gbp = "25"

    def main_menu(self):
        print(""" 
    ------------------ Welcome, Employee {} ------------------\n
    ( 1 ) = Register New Vehicle.
    ( 2 ) = Loan Vehicle.
    ( 3 ) = Recieve Vehicle.
    ( 4 ) = Check Vehicle.

    ( q ) = Quit.
    
    -----------------------------------------------------------""".format(self.employee_num))

        while True:
            option = input("Enter Choice here: ")
            if option == "1":
                Non_Rvk().menu1()
            elif option == "2":
                Non_Rvk().menu2()
            elif option == "3":
                Non_Rvk().menu3()
            elif option == "4":
                Non_Rvk().menu4()
            elif option == "q":
                return False
            else:
                print("Not a valid Option! ")
                Non_Rvk().main_menu()

    def menu1(self):
        print("---------Register New Vehicle---------\n")
   
        vehicle_ID = input("Input Vehicle ID number: ")
        vehicle_name = input("Vehicle name / licence plate: ")
        vehicle_type = input("Vehicle type: ") # What kinda vehicle can be from a Polar bear or scuba piledriver to a tricecle
        vehicle_model = input("Vehicle Model: ")
        vehicle_manufacturer = input("Input vehicle Manufacturer: ")
        vehicle_color = input("Vehicle Color: ")
        vehicle_condition = input("Vehicle Condition: ")
        vehicle_location = input("Input cars location: ")

        while True:

            try:
                vehicle_age = float(input("Input year that the vehicle was Manufacturerd: "))
                vehicle_tax = float(input("Input the tax on the vehicle rent: "))
                break

            except:
                print("Invalid input, Try again")
            
        register_more = input("Wish to register more vehicles? y/n: ")
        if register_more == "y" :
            Non_Rvk().menu1()
        
        # Making a dict list of the info of the newly registerd car
        new_car_info = [vehicle_name, vehicle_type, vehicle_manufacturer, vehicle_model, vehicle_color, vehicle_age, vehicle_tax, vehicle_condition, vehicle_location]
        vehicle_ID_dict = {}
        vehicle_ID_dict[vehicle_ID] = new_car_info

        return_to_mainmenu = input("Would you like to return to Main Menu? y/n: ")
        if return_to_mainmenu == "y":
            Non_Rvk().main_menu()
        else:
            return
        
        return vehicle_ID_dict

    def menu2(self):
        print("---------Lone Vehicle---------\n")

        vehicle_ID = input("Input Vehicle ID number: ")
        loned_car_name = input("Vehicle name / Licence Plate: ")
        persons_licence = input("Driving Licence: ")
        use_gbp = input("Use GBP y/n: ")

        if use_gbp == "y":
            print(f"gbp ballance {self.gbp}: \n you have used your GBP ")
            print(f"your gbp ballance is now {self.gbp - self.gbp}")
        
        return_to_mainmenu = input("Wish to return to main menu? y/n: ")

        vehicle_info = [loned_car_name, persons_licence]
        loned_dict = {}
        loned_dict[vehicle_ID] = vehicle_info

        if return_to_mainmenu == "y":
            Non_Rvk().main_menu()

        else:
            return
        return self.gbp
        # Adda is.digit
        # Need to add all the info to dict list

    def menu3(self):
        print("---------Recive Vehicle---------\n")

        returning_vehicle_ID = input("Input vehicle ID: ")
        returning_vehicle_name = input("Input vehicle name / licence plate: ")
        returning_vehicle_condition = input("Input vehicle condition: ")
        returning_vehicle_late = input("Is the car late? y/n ")

        if returning_vehicle_late == "n":
            self.gbp += 10
            print(f"You have {self.gbp}, GBP to your exposal")

        else:
            print("Chuck is not happy!")
        return_to_mainmenu = input("Would you like to return to Main Menu? y/n: ")
        
        if return_to_mainmenu == "y":
            Non_Rvk().main_menu()

        else:
            return None
        return self.gbp

        # Adda gbp 

    def menu4(self):
        #Here it needs to get the list of vehicles from Vehicles.csv and look up the Key word[ID] and print out everything about the car.
        print("---------Check Vehicle---------\n")
        checking_vehicle_ID = input("Enter vehicle ID: ")
        
        checking_more = input("Wish to check on more vehicles? y/n: ")
        if checking_more == "y" :
            Non_Rvk().menu4()
        return_to_mainmenu = input("Would you like to return to Main Menu? y/n: ")
        if return_to_mainmenu == "y":
            Non_Rvk().main_menu()
        else:
            return None




Non_Rvk().main_menu()
  










