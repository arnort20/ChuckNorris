#from Logic_classes.logic_wrapper import LogicAPI as logic

GBP = 0

class Non_Rvk():
    def __init__(self):
        self.employee_num = "69"

    def main_menu(self):
        print(""" 
    ------------------ Welcome, Employee {} ------------------\n
    ( 1 ) = Register New Vehicle.
    ( 2 ) = Loan Vehicle.
    ( 3 ) = Recieve Vehicle.
    ( 4 ) = Check Vehicle.

    ( q ) = Quit.
    
    -----------------------------------------------------------""".format(self.employee_num))

        option = input("Enter Choise here: ")
        if option == "1":
            Non_Rvk().menu1()
        elif option == "2":
            Non_Rvk().menu2()
        elif option == "3":
            Non_Rvk().menu3()
        elif option == "4":
            Non_Rvk().menu4()
        elif option == "q":
            return
        else:
            print("Not a valid Option!: ")
        
    def menu1(self):
        print("---------Register New Vehicle---------\n")

        vehicle_ID = input("Input Vehicle ID number: ")
        vehicle_name = input("Vehicle name / licence plate: ")
        vehicle_type = input("Vehicle type: ") # What kinda vehicle
        vehicle_model = input("Vehicle Model: ")
        vehicle_manufacturer = input("Input vehicle Manufacturer: ")
        vehicle_color = input("Vehicle Color: ")
        vehicle_condition = input("Vehicle Condition: ")
        vehicle_age = input("Input year the car was Manufacturerd: ")
        vehicle_tax = input("Input the tax on the vehicle rent: ")
        register_more = input("Wish to register more vehicles? y/n: ")

        new_car_info = [vehicle_name, vehicle_type, vehicle_manufacturer, vehicle_model, vehicle_color, vehicle_age, vehicle_tax,]
        vehicle_ID_dict = {}
        vehicle_ID_dict[vehicle_ID] = new_car_info 

        if register_more == "y" :
            Non_Rvk().menu1()
        else:
            return
        return vehicle_ID_dict

        #def make_vehicle(vehicle_ID_dict):
        #   print(Vehicle(ride["ID"],ride["Vehicle name"],ride["Type"],ride["Manufacturer"],ride["Model"],ride["Color"],ride["age"],ride["tax"],ride["available"])) 

    def menu2(self):
        print("---------Lone Vehicle---------\n")

        vehicle_ID = input("Input Vehicle ID number: ")
        loned_car_name = input("Vehicle name / Licence Plate: ")
        persons_licence = input("Driving Licence: ")
        use_GBP = input("Use GBP: ")
        return_to_mainmenu = input("Wish to return to main menu? y/n: ")
        if return_to_mainmenu == "y":
            Non_Rvk().main_menu()
        else:
            return
        # Adda is.digit
        # Need to add all the info to dict list

    def menu3(self):
        GBP = 0
        print("---------Recive Vehicle---------\n")

        returning_vehicle_ID = input("Input vehicle ID: ")
        returning_vehicle_name = input("Input vehicle name / licence plate: ")
        returning_vehicle_condition = input("Input vehicle condition: ")
        returning_vehicle_late = input("Is the car late? y/n ")
        if returning_vehicle_late == "n":
            GBP += 1
            print(f"You have {GBP}, GBP to your exposal")
        else:
            print("Chuck is not happy!")
        return GBP

        
        
        # Adda GBP 

    def menu4(self):
        print("---------Check Vehicle---------\n")
        checking_vehicle_ID = input("Enter vehicle ID: ")
        checking_more = input("Wish to check on more vehicles? y/n")
        if checking_more == "y" :
            Non_Rvk().menu4()



    def Register_Vehicle(self):
        pass

    

Non_Rvk().main_menu()
  










