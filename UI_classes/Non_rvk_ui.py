from Model_classes.Employee import Employee
from Logic_classes.Logic_API import Logic_API
from Model_classes.Vehicle import Vehicle
from Model_classes.Contract import Contract
from Model_classes.Customer import Customer
from UI_classes.Print_formats import Print_format
"""

11
As an employee of NaN Air I need to be able to update a rental contract to 
register the return time of a vehicle


"""
class Non_rvk_ui:
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


            title = 'welcome Employee {}'.format(self.login_id)
            self.format.print_title(title,self.width)
            menu = "( 1 ) Register New Vehicle,( 2 ) Loan Vehicle,( 3 ) Recieve Vehicle,( 4 ) Check Vehicle,( 5 ) Change Vehicle,( 6 ) delete Vehicle,( q ) Quit."

    
            self.format.print_space()
            self.format.print_main_menu(menu,self.width)
            self.format.print_line(len(title)*"_",self.width)

            option = input(self.format.question("Enter Choice here",self.width))


            if option == "1":
                self.Register_Vehicle()
                choice =1
            elif option == "2":
                self.Vehicle_lending()
                choice =1
            elif option == "3":
                self.Recieve_vehicle_()
                choice =1
            elif option == "4":
                self.Check_Vehicle()
                choice =1
            elif option == "q":
                break
            else:
                choice = 0

    #Register vehicle menu
    def Register_Vehicle(self):
        wrong = 0
        while True:
            

            #dictionary of questions and current answers
            #questions = {"vehicle_name":"empty","type":"empty","manufacturer":"empty","model":"empty","color":"empty","year_made":"empty","tax":"empty","available":"empty","location_id":"empty","license_type":"empty"}
            questions = {"vehicle_name":"empty","type":"empty","manufacturer":"empty","model":"empty","color":"empty","year_made":"empty","available":"empty","location_id":"empty","license_type":"empty"}

            # loop to answer each question
            for key,value in questions.items():
                self.liner()
                                #if person wrote a wrong input last time
                if wrong == 1:
                    self.format.warning("there is one or more wrong input!")
                    print("")
                    wrong = 0

                #formattin reigster vehicle
                title = ("Register new vehicle")
                self.format.print_title(title,self.width)
                self.format.print_space()
                self.format.print_questions(questions,self.width)
                self.format.print_space()
                self.format.print_line(len(title)*"_",self.width)
                option = input(self.format.question("Enter Choice here",self.width))
                questions[key] = option
                

            questions["age"] = questions["year_made"]

            # check if inputs are of the correct type
            try:
                #test = questions["vehicle_name"],questions["type"],questions["manufacturer"],questions["model"],questions["color"],int(questions["age"]),int(questions["tax"]),questions["available"],questions["location_id"],questions["license_type"]
                test = questions["vehicle_name"],questions["type"],questions["manufacturer"],questions["model"],questions["color"],int(questions["age"]),questions["available"],questions["location_id"],questions["license_type"]
                #self.logic.make_new_vehicle(questions["vehicle_name"],questions["type"],questions["manufacturer"],questions["model"],questions["color"],questions["age"],questions["tax"],questions["available"],questions["location_id"],questions["license_type"])
                self.logic.make_new_vehicle(questions["vehicle_name"],questions["type"],questions["manufacturer"],questions["model"],questions["color"],questions["age"],questions["available"],questions["location_id"],questions["license_type"])
            except:
                print()
                wrong = 1
                continue


            break

        return



    # Afhenda bilinn til utleigu
    def Vehicle_lending(self):
        wrong = 0

        while True:
            self.liner()

            if wrong == 1:
                self.format.warning("there is one or more wrong input!")
                print("")
                wrong = 0


            title =("Loan Vehicle")
            self.format.print_title(title)
            self.format.print_space()

            contract_id = input(self.format.question("input contract ID "))
            
            self.format.print_line(len(title)*"_")


            # cheeck if contract and customer


            try:
                fetch_date = input(self.format.question("date when vehicle is picked up (YYYY.MM.DD): "))
                self.logic.handover_vehicle(contract_id, fetch_date)
                break

            except:
                wrong = 1
                continue

        return


    # Taka a moti bilnum ur utleigu
    def Recieve_vehicle_(self):

        wrong =0 
        while True:
            self.liner()
            if wrong == 1:
                self.format.warning("there is one or more wrong input!")
                print("")
                wrong = 0
            #self.logic.recieve_vehicle(contractID, return_date, gbp_used)
            #nota bene GBP_used is a bool (True/False)
            

            title = ("Recive Vehicle")
            self.format.print_title(title)
            self.format.print_space()
            returning_contract_ID =         input(self.format.question("Input contract ID: "))
            return_date =                   input(self.format.question("Input return date: "))
            gbp_used =                   input(self.format.question("how much gbp does the customer want to use: "))
            returning_vehicle_condition =   input(self.format.question("Input vehicle condition(ok/bad): "))

            late_return = self.logic.recieve_vehicle(returning_contract_ID,return_date,gbp_used)


            self.format.print_line(len(title)*"_")

            try:
                contract = self.logic.get_contract(returning_contract_ID)
                customer_id = contract.customer_id
                customer = self.logic.get_customer(customer_id)
                vehicle_id = contract.vehicle_id
            except:
                wrong = 1
                continue
       



            if returning_vehicle_condition == "ok":
                vehicle_condition = {"available":"y"}
                self.logic.change_vehicle_info(vehicle_id,vehicle_condition)


            if late_return != True:
                print('')
                customer.gbp = int(customer.gbp) + 3
                self.logic.change_customer(customer.id,{"gbp":str(customer.gbp)})
                self.format.warning(f"You have {customer.gbp}, GBP to your exposal")

            else:
                print("Chuck is not happy!")
                


            break
        return
        # Adda gbp 






    def Check_Vehicle(self):
        #Here it needs to get the list of vehicles from Vehicles.csv and look up the Key word[ID] and print out everything about the car.
        self.liner()
        while True:
            title = ("Check Vehicle")

            self.format.print_title(title,self.width)
            self.format.print_space()
            checking_vehicle_ID = input(self.format.question("Enter vehicle ID",self.width))
            self.format.print_space()
            info = ("ID,Plate,Type,Manufacturer,Model,Color,Year made,Available,Location id,License type")
            vehicle = self.logic.get_vehicle(checking_vehicle_ID)


            self.format.print_title(checking_vehicle_ID,self.width)
            self.format.print_space()
            self.format.print_out_format(str(info),self.width)
            self.format.print_space(self.width)

            self.format.print_out_format(str(vehicle),self.width)

            self.format.print_line(len(checking_vehicle_ID)*"_",self.width)




            checking_more = input(self.format.question("Wish to check on more vehicles? y/n",self.width))

            if checking_more != "y" :
                break
 
        return









