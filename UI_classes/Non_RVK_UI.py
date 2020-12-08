from Model_classes.Employee import Employee
from Logic_classes.logic_API import Logic_API 
from Model_classes.Vehicle import Vehicle
from Model_classes.Contract import Contract
from Model_classes.Customer import Customer
from UI_classes.Print_formats import Print_format


#def make_vehicle(ride):
#    print(vehicle(ride["ID"],ride["Vehicle name"],ride["Type"],ride["Manufacturer"],ride["Model"],ride["Color"],ride["age"],ride["tax"],ride["available"]))

class Non_rvk():
    def __init__(self, username, pword):
        self.logic = Logic_API(username, pword)
        self.employee_num = username
        self.login_id = username
        self.format = Print_format()
        self.width = 200

    def liner(self):
        print("\n"*12)

    #Maine menu loop
    def main_menu(self):
        choice =1
        while True:
   
            self.liner()
            if choice == 0:
                print("")
                self.format.print_main_menu("Invalid Choice",self.width)
                print("")


            title = 'welcome Employee {}'.format(self.login_id)
            self.format.print_title(title,self.width)
            menu = "( 1 ) Register New Vehicle,( 2 ) Loan Vehicle,( 3 ) Recieve Vehicle,( 4 ) Check Vehicle,,( q ) Quit."
            self.format.print_main_menu(menu,self.width)
            self.format.print_line(len(title)*"_",self.width)


            option = input(self.format.question("Enter Choice here",self.width))
            if option == "1":
                self.menu1()
                choice =1
            elif option == "2":
                self.menu2()
                choice =1
            elif option == "3":
                self.menu3()
                choice =1
            elif option == "4":
                self.menu4()
                choice =1
            elif option == "q":
                break
            else:
                choice = 0









    #Register vehicle menu
    def menu1(self):


        # name = input(self.format.question("Vehicle name / licence plate ",self.width))
        # typer = input(self.format.question("Vehicle type ",self.width))    # What kinda vehicle can be from a Polar bear or scuba piledriver to a tricecle
        # model = input(self.format.question("Vehicle Model ",self.width))
        # manufacturer = input(self.format.question("Input vehicle Manufacturer ",self.width))
        # color = input(self.format.question("Vehicle Color ",self.width))
        # condition = input(self.format.question("is car ok ( y / n ) ",self.width))
        # location = input(self.format.question("Input cars location ",self.width))
        # id_type = input(self.format.question("license needed to drive vehicle ",self.width))

        # while True:
        #     try:
        #         age = float(input(self.format.question("Manufacturing Year: ",self.width)))
        #         tax = float(input(self.format.question("vehicle tax: ",self.width)))
        #         break
        #     except:
        #         print("")
        #         self.format.print_main_menu("Invalid input Try again",self.width)
        #         print("")


        questions = {"vehicle_name":"empty","type":"empty","manufacturer":"empty","model":"empty","color":"empty","age":"empty","tax":"empty","available":"empty","location_id":"empty","license_type":"empty"}
        for key,value in questions.items():
            self.liner()
            title = ("Register new vehicle")
            self.format.print_title(title,self.width)
            self.format.print_questions(questions,self.width)
            self.format.print_line(len(title)*"_",self.width)
            option = input(self.format.question("Enter Choice here",self.width))
            questions[key] = option


        if questions["license_type"] != "empty":
            self.logic.make_new_vehicle(questions["vehicle_name"],questions["type"],questions["manufacturer"],questions["model"],questions["color"],questions["age"],questions["tax"],questions["available"],questions["location_id"],questions["license_type"])

        # register_more = input(self.format.question("Wish to register more vehicles? y/n",self.width))
        # if register_more == "y" :
        #     self.menu1()
         
        return



    # Afhenda bilinn til utleigu
    def menu2(self):
        self.liner()
        title =("Loan Vehicle")
        self.format.print_title(title)

        customer_id =       input(self.format.question("input customer ID "))
        contract_id =       input(self.format.question("input contract ID "))
        
        self.format.print_line(len(title)*"_")


        contract = self.logic.get_contract(contract_id)
        vehicle_ID = contract.vehicle_id

        vehicle_condition = {"available":"n"}
        self.logic.change_information(vehicle_ID,vehicle_condition )

        return


    # Taka a moti bilnum ur utleigu
    def menu3(self):
        self.liner()
        title = ("Recive Vehicle")

        self.format.print_title(title)
        returning_contract_ID =         input(self.format.question("Input contract ID: "))
        returning_vehicle_condition =   input(self.format.question("Input vehicle condition(ok/bad): "))
        returning_vehicle_late =        input(self.format.question("Is the vehicle late(y/n): "))

        self.format.print_line(len(title)*"_")

        contract = self.logic.get_contract(returning_contract_ID)
        customer_id = contract.customer_id
        customer = self.logic.get_customer(customer_id)
        vehicle_id = contract.vehicle_id

        if returning_vehicle_condition == "ok":
            vehicle_condition = {"available":"y"}
            self.logic.change_vehicle_info(vehicle_id,vehicle_condition)


        if returning_vehicle_late == "n":
            print(f"You have {customer.gbp}, GBP to your exposal")

        else:
            print("Chuck is not happy!")
            customer.bbp += 2

        return
        # Adda gbp 






    def menu4(self):
        #Here it needs to get the list of vehicles from Vehicles.csv and look up the Key word[ID] and print out everything about the car.
        self.liner()
        while True:
            title = ("Check Vehicle")
            self.format.print_title(title,self.width)
            checking_vehicle_ID = input(self.format.question("Enter vehicle ID",self.width))
            info = ("ID,Plate,Type,Manufacturer,Model,Color,Age,Tax,Available,Location id,License type")
            vehicle = self.logic.get_vehicle(checking_vehicle_ID)


            self.format.print_title(checking_vehicle_ID,self.width)
            self.format.print_out_format(str(info),self.width)
            self.format.print_space(self.width)

            self.format.print_out_format(str(vehicle),self.width)

            self.format.print_line(len(checking_vehicle_ID)*"_",self.width)




            checking_more = input(self.format.question("Wish to check on more vehicles? y/n",self.width))

            if checking_more != "y" :
                break
 
        return









