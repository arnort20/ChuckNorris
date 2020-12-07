from Logic_classes.employee_logic import Employee
from Logic_classes.logic_wrapper import LogicAPI 
from Model_classes.Vehicle import Vehicle
from Model_classes.Contract import Contract
from Model_classes.Customer import Customer
from UI_classes.Print_formats import Print_format


#def make_vehicle(ride):
#    print(vehicle(ride["ID"],ride["Vehicle name"],ride["Type"],ride["Manufacturer"],ride["Model"],ride["Color"],ride["age"],ride["tax"],ride["available"]))

class Non_rvk():
    def __init__(self, username, pword):
        self.logic = LogicAPI(username, pword)
        self.employee_num = username
        self.login_id = username
        self.format = Print_format()

    def returner(self):
        return_to_mainmenu = input("Would you like to return to Main Menu? y/n: ")
        if return_to_mainmenu == "y":
            self.main_menu()
        else:
            return 


    #Maine menu loop
    def main_menu(self,gogo = "yes"):
        title = 'welcome Employee{}'.format(self.login_id)
        self.format.print_title(title)
        menu = "( 1 ) Register New Vehicle,( 2 ) Loan Vehicle,( 3 ) Recieve Vehicle,( 4 ) Check Vehicle,,( q ) Quit."
        self.format.print_main_menu(menu)
        self.format.print_title(len(title)*"-")

    #     print(""" 
    # ------------------ Welcome, Employee {} ------------------\n
    # ( 1 ) = Register New Vehicle.
    # ( 2 ) = Loan Vehicle.
    # ( 3 ) = Recieve Vehicle.
    # ( 4 ) = Check Vehicle.

    # ( q ) = Quit.
    
    # -----------------------------------------------------------""".format(self.employee_num)):
        while True:
            if gogo == None:
                break
            option = input("Enter Choice here: ")
            if option == "1":
                self.menu1()
            elif option == "2":
                self.menu2()
            elif option == "3":
                self.menu3()
            elif option == "4":
                self.menu4()
            elif option == "q":
                break
            else:
                print("Not a valid Option! ")








    #Register vehicle menu
    def menu1(self):
        title = ("Register new vehicle")
        self.format.print_title(title)

        name = input(self.format.question("Vehicle name / licence plate "))
        typer = input(self.format.question("Vehicle type "))    # What kinda vehicle can be from a Polar bear or scuba piledriver to a tricecle
        model = input(self.format.question("Vehicle Model "))
        manufacturer = input(self.format.question("Input vehicle Manufacturer "))
        color = input(self.format.question("Vehicle Color "))
        condition = input(self.format.question("is car ok ( y / n ) "))
        location = input(self.format.question("Input cars location "))
        id_type = input(self.format.question("license needed to drive vehicle "))

        while True:
            try:
                age = float(input(self.format.question("Manufacturing Year: ")))
                tax = float(input(self.format.question("vehicle tax: ")))
                break
            except:
                print("Invalid input, Try again")

        self.format.print_title(len(title)*"-")

        

        if condition == "ok":
            condition = "available"
        else:
            condition = "unavailable"

        self.logic.make_new_vehicle(name,typer,manufacturer,model,color,age,tax,condition,location,id_type)

        register_more = input("Wish to register more vehicles? y/n: ")
        if register_more == "y" :
            self.menu1()
        
        # Making a dict list of the info of the newly registerd car
        self.returner()
        
        return None




    # Afhenda bilinn til utleigu
    def menu2(self):
        title =("Loan Vehicle")
        self.format.print_title(title)

        customer_id =       input(self.format.question("input customer ID "))
        contract_id =       input(self.format.question("input contract ID "))
        
        self.format.print_title(len(title)*"-")


        contract = self.logic.get_contract(contract_id)
        vehicle_ID = contract.vehicle_id

        vehicle_condition = {"available":"unavailable"}
        self.logic.change_information(vehicle_ID,vehicle_condition )

        self.returner()
        return


    # Taka a moti bilnum ur utleigu
    def menu3(self):

        title = ("Recive Vehicle")

        self.formatter.print_title(title)
        returning_contract_ID =         input(self.format.question("Input contract ID: "))
        returning_vehicle_condition =   input(self.format.question("Input vehicle condition(ok/bad): "))
        returning_vehicle_late =        input(self.format.question("Is the vehicle late(y/n): "))

        self.format.print_title(len(title)*"-")

        contract = self.logic.get_contract(returning_contract_ID)
        customer_id = contract.customer_id
        customer = self.logic.get_customer(customer_id)
        vehicle_id = contract.vehicle_id

        if returning_vehicle_condition == "ok":
            vehicle_condition = {"available":"available"}
            self.logic.change_vehicle_info(vehicle_id,vehicle_condition)


        if returning_vehicle_late == "n":
            print(f"You have {customer.gbp}, GBP to your exposal")

        else:
            print("Chuck is not happy!")
            customer.bbp += 2
        
        self.returner()
        return
        # Adda gbp 






    def menu4(self):
        #Here it needs to get the list of vehicles from Vehicles.csv and look up the Key word[ID] and print out everything about the car.
        title = ("Check Vehicle")
        self.formatter.print_title(title)
        checking_vehicle_ID = input("Enter vehicle ID: ")
        self.formatter.print_title(len(title)*"-")


        vehicle = self.logic.get_vehicle(checking_vehicle_ID)
        print(vehicle)

        checking_more = input("Wish to check on more vehicles? y/n: ")

        if checking_more == "y" :
            self.menu4()
        else:
            self.returner()
            return









