from Logic_classes.logic_wrapper import LogicAPI 
from Model_classes.Vehicle import Vehicle
from Model_classes.Contract import Contract
from Model_classes.Customer import Customer


#def make_vehicle(ride):
#    print(vehicle(ride["ID"],ride["Vehicle name"],ride["Type"],ride["Manufacturer"],ride["Model"],ride["Color"],ride["age"],ride["tax"],ride["available"]))

class Non_Rvk():
    def __init__(self):
        self.logic = LogicAPI("1","1")
        self.employee_num = "69"

    #Maine menu loop
    def main_menu(self,going = 0):
        print(""" 
    ------------------ Welcome, Employee {} ------------------\n
    ( 1 ) = Register New Vehicle.
    ( 2 ) = Loan Vehicle.
    ( 3 ) = Recieve Vehicle.
    ( 4 ) = Check Vehicle.

    ( q ) = Quit.
    
    -----------------------------------------------------------""".format(self.employee_num))
        if going == 0:
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
        else:
            print("Bye bye")


    def returner():
        return_to_mainmenu = input("Would you like to return to Main Menu? y/n: ")
        if return_to_mainmenu == "y":
            Non_Rvk.main_menu()
        else:
            Non_Rvk.main_menu(25)





    #Register vehicle menu
    def menu1(self):
        print("---------Register New Vehicle---------\n")
   
        name = input("Vehicle name / licence plate: ")
        typer = input("Vehicle type: ") # What kinda vehicle can be from a Polar bear or scuba piledriver to a tricecle
        model = input("Vehicle Model: ")
        manufacturer = input("Input vehicle Manufacturer: ")
        color = input("Vehicle Color: ")
        condition = input("Vehicle Condition: ")
        location = input("Input cars location: ")
        id_type = input("license needed to drive vehicle: ")
        while True:
            try:
                age = float(input("Input year that the vehicle was Manufacturerd: "))
                tax = float(input("Input the tax on the vehicle rent: "))
                break
            except:
                print("Invalid input, Try again")

        if condition == "ok":
            condition = "available"
        else:
            condition = "unavailable"

        self.logic.make_new_vehicle(name,typer,manufacturer,model,color,age,tax,condition,location,id_type)

        register_more = input("Wish to register more vehicles? y/n: ")
        if register_more == "y" :
            Non_Rvk().menu1()
        
        # Making a dict list of the info of the newly registerd car
        Non_Rvk.returner()
        
        return




    # Afhenda bilinn til utleigu
    def menu2(self):
        print("---------Loan Vehicle---------\n")

        customer_id =       input("input customer ID: ")
        contract_id =       input("input contract ID: ")
        
        contract = self.logic.get_contract(contract_id)
        vehicle_ID = contract.vehicle_id
        
        vehicle_condition = {"available":"unavailable"}
        LogicAPI.change_information(vehicle_ID,vehicle_condition )

        Non_Rvk.returner()
        return


    # Taka a moti bilnum ur utleigu
    def menu3(self):

        print("---------Recive Vehicle---------\n")


        returning_contract_ID =         input("Input contract ID: ")
        returning_vehicle_condition =   input("Input vehicle condition(ok/bad): ")
        returning_vehicle_late =        input("Is the vehicle late(y/n): ")


        contract = self.logic.get_contract(returning_contract_ID)
        customer_id = contract.customer_id
        customer = self.logic.get_customer(customer_id)
        vehicle_id = contract.vehicle_id

        if returning_vehicle_condition == "ok":
            vehicle_condition = {"available":"available"}
            self.logic.change_information(vehicle_id,vehicle_condition)


        if returning_vehicle_late == "n":
            print(f"You have {customer.gbp}, GBP to your exposal")

        else:
            print("Chuck is not happy!")
            customer.bbp += 2
        
        Non_Rvk.returner()
        return
        # Adda gbp 

    def menu4(self):
        #Here it needs to get the list of vehicles from Vehicles.csv and look up the Key word[ID] and print out everything about the car.
        print("---------Check Vehicle---------\n")
        checking_vehicle_ID = input("Enter vehicle ID: ")
        vehicle = self.logic.get_vehicle(checking_vehicle_ID)
        print(vehicle)

        checking_more = input("Wish to check on more vehicles? y/n: ")

        if checking_more == "y" :
            Non_Rvk().menu4()
        else:
            Non_Rvk.returner()
            return









