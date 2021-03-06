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
                self.format.warning("Invalid Choice",self.width)


            title = 'welcome Employee {}'.format(self.login_id)
            self.format.print_title(title,self.width)
            menu = "( 1 ) Register New Vehicle,( 2 ) Loan Vehicle,( 3 ) Recieve Vehicle,( 4 ) Check Vehicle,( 5 ) Change Vehicle,,( q ) Quit."

    
            self.format.print_space()
            self.format.print_main_menu(menu,self.width)
            self.format.print_line(len(title)*"_",self.width)

            option = input(self.format.question("Enter Choice here",self.width))


            if option == "1":
                self.Register_Vehicle()
                choice = 1
            elif option == "2":
                self.Vehicle_lending()
                choice = 1
            elif option == "3":
                self.Recieve_vehicle_()
                choice = 1
            elif option == "4":
                self.Check_Vehicle()
                choice = 1
            elif option == "5":
                self.change_vehicle()
                choice = 1 
        
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
            
            title = ("Register new vehicle")
            information = ("( c ) Cancel,( f ) Finish")
            questions = {"vehicle_name":"empty","type":"empty","manufacturer":"empty","model":"empty","color":"empty","year_made":"empty","available ( yes / no )":"empty","location_id":"empty","license_type":"empty"}
            # loop to answer each question
            while True:
                if wrong != 0:
                    questions = {"vehicle_name":"empty","type":"empty","manufacturer":"empty","model":"empty","color":"empty","year_made":"empty","available":"empty","location_id":"empty","license_type":"empty"}
                for key,value in questions.items():
                    self.liner()
                                    #if person wrote a wrong input last time
                    if wrong == 1:
                        self.format.warning("vehicle info not filled in yet")
                        print("")
                        wrong = 0

                    #formattin reigster vehicle

                    self.format.question_box(questions,information,title)
                    option = input(self.format.question("Enter Input here",self.width))

                    if option == 'c':
                        return
                    elif option == 'f' and questions["license_type"] != "empty" :
        
                        questions["age"] = questions["year_made"]
                        test = questions["vehicle_name"],questions["type"],questions["manufacturer"],questions["model"],questions["color"],int(questions["age"]),questions["available"],questions["location_id"],questions["license_type"]
                    
                        self.logic.make_new_vehicle(questions["vehicle_name"],questions["type"],questions["manufacturer"],questions["model"],questions["color"],questions["age"],questions["available ( yes / no )"],questions["location_id"],questions["license_type"])
                        return
                    elif option == 'f' and questions["license_type"] == "empty" :
                        wrong =1
                        break
                    else:
                        questions[key] = option

    # Afhenda bilinn til utleigu
    def Vehicle_lending(self):
        wrong = 0
        questions = {"Input contract ID":"empty","vehcile lending date":"empty"}
        information = ("Date Format (yy.mm.dd),( f ) Finish,( c ) Cancel")
        while True:
            self.liner()

            if wrong == 1:
                self.format.warning("there is one or more wrong input!")
                print("")
                wrong = 0

            title = ("Loan Vehicle")
            for key,value in questions.items():

                self.liner()
                self.format.question_box(questions,information,title)
                
                option = input(self.format.question("Enter Input here "))
                #Change for next print
                questions[key] = option        

                #Choices
                contract = self.logic.get_contract(questions["Input contract ID"])
                vehicle = self.logic.get_vehicle(contract.vehicle_id)

                if vehicle != None and contract != None:
                    self.logic.change_vehicle_info(contract.vehicle_id,{"available":"no"})
                    self.logic.handover_vehicle(questions["Input contract ID"],questions["vehcile lending date"])

                if option == "c":
                    return
            self.liner()
            self.format.question_box(questions,information,title)
            option = input(self.format.question("Return"))
            return





    # Taka a moti bilnum ur utleigu
    def Recieve_vehicle_(self):
        wrong =0 
        info = "( c ) Cancel,( F ) Finish"
        title ="Recieve vehicle"
        questions = {"Input Contract ID":"empty","Input return date":"empty","does customer want to use gbp( y / n )":"empty","Input vehicle condition(ok/bad)":"empty"}

        # printing error statements
        while True:
            if wrong != 0:
                questions = {"Input Contract ID":"empty","Input return date":"empty","does customer want to use gbp( y / n )":"empty","Input vehicle condition(ok/bad)":"empty"}
            self.liner()
            if wrong == 1:
                self.format.warning("there is one or more wrong input!")
                print("")
            if wrong == 2:
                self.format.warning("Date input was wrong")
                print("")


        # print out the format
            for key,value in questions.items():
                #Format
                if wrong == 0:
                    self.liner()
                else:
                    wrong = 0

                self.format.question_box(questions,info,title)
                option = input(self.format.question('Insert input here'))



                # change for next print
                print("")
                
                #choices
                if option == "c":
                    return
                if option == "f" and questions["Input vehicle condition(ok/bad)"] != "empty":

                    returning_contract_ID = questions["Input Contract ID"]
                    return_date =questions["Input return date"]
                    returning_vehicle_condition = questions["Input vehicle condition(ok/bad)"]
                    use_gbp = questions["does customer want to use gbp( y / n )"]



                    # check if gbp is used
                    if use_gbp == "y":
                        gbp_used = True
                    else:
                        gbp_used = False



                    #check if date format is correcty
                    try:
                        late_return = self.logic.recieve_vehicle(returning_contract_ID,return_date,gbp_used)
                    except:
                        wrong = 2
                        break

                    self.format.print_line(len(title)*"_")



                    #test if contracts and customer exist
                    try:
                        contract = self.logic.get_contract(returning_contract_ID)
                        customer_id = contract.customer_id
                        customer = self.logic.get_customer(customer_id)
                        vehicle_id = contract.vehicle_id
                    except:
                        wrong = 1
                        continue
            
                    # sign into csv condition of vehicle
                    if returning_vehicle_condition == "ok":
                        vehicle_condition = {"available":"yes"}
                    else:
                        vehicle_condition = {"available":"damaged"}
                    self.logic.change_vehicle_info(vehicle_id,vehicle_condition)


                    # adds gbp if vehicle is not late
                    if late_return != True:
                        print('')
                        customer.gbp = int(customer.gbp) + 3
                        self.logic.change_customer(customer.id,{"gbp":str(customer.gbp)})
                        self.liner()
                        self.format.short_box(f"You have {customer.gbp} GBP at your exposal","gbp amount")
                        go_back = input(self.format.question("Return"))
                    return

                    #sends user to error if a field is left empty
                elif option == "f" and questions["Input vehicle condition(ok/bad)"] == "empty":
                    wrong =1 
                    break
                else:
                    questions[key] = option
                    continue

                        

                        


                    
                    return

    def Check_Vehicle(self):
        #Here it needs to get the list of vehicles from Vehicles.csv and look up the Key word[ID] and print out everything about the car.
        wrong =0
        while True:
            title = ("Check Vehicle")
            self.format.liner()
            if wrong == 1:
                self.format.warning("Incorrect Vehicle ID")

            #Format
            self.format.short_box("Enter Vehicle ID below",title)
            checking_vehicle_ID = input(self.format.question("Enter vehicle ID",self.width))
            info = ("ID,Plate,Type,Manufacturer,Model,Color,Year made,Available,Location id,License type")
            vehicle = self.logic.get_vehicle(checking_vehicle_ID)

            if vehicle == None:
                wrong = 1 
                continue

            options = ("( r ) return")
            self.format.liner()
            self.format.list_box(title,options,info,str(vehicle))
            
            checking_more = input(self.format.question("Wish to check on more vehicles? y/n",self.width))


            if checking_more != "y":
                break
 
        return


    #users can go here to remove vehicles from a state of being in repair to being available and to change its color
    def change_vehicle(self):
        #Info
        title = "Vehicle Search"
        information = ("( r ) Return,,| Insert ID below |")
        wrong = 0
        while True:

            #Format
            self.liner()

            if wrong != 0:
                self.format.warning("Wrong vehicle ID")
                wrong =0         

            self.format.short_box(information,title)
            vehicle_id = input(self.format.question("Vehicle ID")) 

            if vehicle_id == 'r':
                return

            try:
                vehicle = self.logic.get_vehicle(vehicle_id)
                vehicle.id
                break

            except:
                wrong = 1
                continue

        #Info
        title = "Changing vehicle"
        information = ("( c ) Cancel,( f ) Finish,( d ) Delete,( s ) skip")
        questions = {"color":vehicle.color,"available( yes / no / damaged)":vehicle.available}

        while True:
            for key,value in questions.items():

                #Format
                self.liner()
                self.format.question_box(questions,information,title)
                option = input(self.format.question("Enter input here"))

                #Choices
                if option == 's':
                    continue
                if option == 'c':
                    return
                if option == "f":
                    dicter = {"color":questions["color"],"available":questions["available( yes / no / damaged)"]}
                    self.logic.change_vehicle_info(vehicle.id,dicter)
                    return

                if option == "d":
                    self.delete_Vehicle(vehicle_id)
                    return
                #changing for next print
                questions[key] = option



    def delete_Vehicle(self,vehicle_id):

        while True:
            #info
            title = "Deleting vehicle"
            information = ("( c ) Cancel,( d ) Delete")

            #Format
            self.liner()
            self.format.short_box(information,title)
            confirm = input(self.format.question("Confirm")) 

            if confirm == "c":
                return
            elif confirm == "d":
                self.logic.kill_vehicle(vehicle_id)
                return
            else:
                self.format.warning("Wrong input")






