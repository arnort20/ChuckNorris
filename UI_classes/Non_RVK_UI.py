from Logic_classes.logic_wrapper import LogicAPI 
from Model_classes.Vehicle import Vehicle
from Model_classes.Contract import Contract 


#def make_vehicle(ride):
#    print(vehicle(ride["ID"],ride["Vehicle name"],ride["Type"],ride["Manufacturer"],ride["Model"],ride["Color"],ride["age"],ride["tax"],ride["available"]))

class Non_Rvk():
    def __init__(self):
        self.logic = LogicAPI("1","1")
        self.employee_num = "69"
        self.gbp = "25"
        self.bbp = "25"



    #Maine menu loop
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


    def returner(self):
        return_to_mainmenu = input("Would you like to return to Main Menu? y/n: ")
        if return_to_mainmenu == "y":
            Non_Rvk().main_menu()
        else:
            return





    #Register vehicle menu
    def menu1(self):
        print("---------Register New Vehicle---------\n")
   
        vehicle_name = input("Vehicle name / licence plate: ")
        vehicle_type = input("Vehicle type: ") # What kinda vehicle can be from a Polar bear or scuba piledriver to a tricecle
        vehicle_model = input("Vehicle Model: ")
        vehicle_manufacturer = input("Input vehicle Manufacturer: ")
        vehicle_color = input("Vehicle Color: ")
        vehicle_condition = input("Vehicle Condition: ")
        vehicle_location = input("Input cars location: ")
        vehicle_id_type = input("license needed to drive vehicle: ")
        while True:
            try:
                vehicle_age = float(input("Input year that the vehicle was Manufacturerd: "))
                vehicle_tax = float(input("Input the tax on the vehicle rent: "))
                break
            except:
                print("Invalid input, Try again")

        if vehicle_condition == "ok":
            vehicle_condition = {"available":"available"}
        else:
            vehicle_condition = {"available":"unavailable"}

        self.logic.make_new_vehicle(vehicle_name,vehicle_type,vehicle_model,vehicle_manufacturer,vehicle_color,vehicle_location,vehicle_age,vehicle_tax,vehicle_id_type)

        register_more = input("Wish to register more vehicles? y/n: ")
        if register_more == "y" :
            Non_Rvk().menu1()
        
        # Making a dict list of the info of the newly registerd car
        

        Non_Rvk().returner()
        
        return




    # Afhenda bilinn til utleigu
    def menu2(self):
        print("---------Loan Vehicle---------\n")

        customer_id =       input("input customer ID: ")
        contract_id =       input("input contract ID: ")
        
        contract = LogicAPI.get_contract(contract_id)
        vehicle_ID = contract.vehicle_id
        
        vehicle_condition = {"available":"unavailable"}
        LogicAPI.change_information(vehicle_ID,vehicle_condition )

        return_to_mainmenu = input("Wish to return to main menu? y/n: ")

        if return_to_mainmenu == "y":
            Non_Rvk().main_menu()

        else:
            return



    # Taka a moti bilnum ur utleigu
    def menu3(self):
        print("---------Recive Vehicle---------\n")

        returning_contract_ID = input("Input contract ID: ")
        returning_vehicle_condition = input("Input vehicle condition(ok/bad): ")
        returning_vehicle_late = input("Is the car late? y/n ")

        if returning_vehicle_condition == "ok":
            vehicle_condition = {"available":"available"}
            contract = LogicAPI.get_contract(returning_contract_ID)
            LogicAPI.change_information(contract.vehicle_ID,vehicle_condition)


        if returning_vehicle_late == "n":
            self.gbp += 10
            print(f"You have {self.gbp}, GBP to your exposal")

        else:
            print("Chuck is not happy!")
            self.bbp += 2

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
  










