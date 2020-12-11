from Logic_classes.Logic_API import Logic_API
from Model_classes.Contract import Contract # Display all contracts overview
from Model_classes.Vehicle import Vehicle # 
from Model_classes.Bill import Bill
from UI_classes.Print_formats import Print_format
from UI_classes.Rvk_ui import Rvk_ui
import sys 


#--------------Allot of print formats used here, Check print_format in UI_classes for more information --------------#
#--------------Master Login only for Chuck--------------#
class Chuck_ui():
#--------------Spacer function--------------#
    def liner(self):
        print("\n"*12)
#--------------__init__--------------#
    def __init__(self, username, pword):
        self.logic = Logic_API(username, pword)
        self.printer = Print_format()
#--------------Chuck Norris's personal login menu--------------#

    def chuck_login(self):
        menus = True
        # While Loop for the menu, so it can go back to the main menu after each step has been finished.
        while menus:
            title = "Welcome Master Chuck!"
            self.liner()
            Print_format.print_title(self,title)
            self.printer.print_space()
            option = "( 1 ) Review Earnings Report,( 2 ) View Vehicle Reports,( 3 ) View Bill Overview,( 4 ) Round House Kick,( 5 ) View All Contracts,( 6 ) Register New Employee,( 7 ) Most Popular Vehicles,,( q ) Quit"
            self.printer.print_main_menu(option)
            Print_format.print_line(self,len(title)*"_")


            option = input(self.printer.question("Enter Choice here: "))
            print("")
            
            if option == "q":
                menus = False

            elif option == "1":
                self.Earnings_report()

            elif option == "2":
                self.Vehicle_reports()

            elif option == "3":
                self.Bill_overview()

            elif option == "4":
                self.Round_house()

            elif option == "5":
                self.All_contracts()
            
            elif option == "6":
                self.add_new_employee()

            elif option == "7":
                self.popular_vehicle()

            else:
                print("Not a valid input!" "\n")
                self.chuck_login()
#--------------Lets Chuck Norris register new employees--------------#
    def add_new_employee(self):
        #--------------Title,question and information are input in to print formats--------------#
        title = 'New Employee'
        questions = {"name":"empty","ssn":"empty","address":"empty","location_id":"empty","email":"empty","phone":"empty","password":"empty","confirm password":"empty"}
        information = ("( c ) Cancel, ( f ) Finish")        
        wrong = 0
        while True:
            if wrong != 0:
                questions = {"name":"empty","ssn":"empty","address":"empty","location_id":"empty","email":"empty","phone":"empty","password":"empty","confirm password":"empty"}
            for key,value in questions.items():

                #Format
                self.liner()
                if wrong == 1:
                    self.printer.warning("passwords don't match")
                    wrong = 0
                elif wrong == 2:
                    self.printer.warning("not all info filled in yet")
                    wrong = 0


                self.printer.question_box(questions,information,title)
                option = input(self.printer.question('Type here: '))

                #change for next print
            
                #Choices
                if option == "f" and questions["password"] != questions["confirm password"]:
                    wrong = 1
                    break
                elif option == 'c':
                    return
                elif option == 'f' and questions["confirm password"] != "empty" :
                    questions["emp_name"] = questions["name"]
                    self.logic.hire_employee(questions["emp_name"],questions["ssn"],questions["address"],questions["phone"],questions["email"],questions["location_id"],questions["password"])

                    self.liner()
                    item = self.logic.get_employees()
                    popped = item.pop()
                    information = popped.id + "Is the new Employee's ID"
                    title = "Employee ID"
                    self.printer.short_box(information,title)
                    go_back = input(self.printer.question("return"))
                    return
                elif option == 'f' and questions["confirm password"] == "empty" :
                    wrong =2
                    break
                else:
                    questions[key] = option

                
#--------------Lets Chuck Norris see earnings reports between given dates--------------#
    def Earnings_report(self):
        # Her we need to get the over all earnings report from Logic,(Finished)
        #--------------Title,question and information are input in to print formats--------------#
        questions = {"Input Location ID":"empty","Input Date From":"empty","Input Date To":"empty"}
        title = "Earnings Report"
        information = ("Date Format = (yy.mm.dd),( c ) Cancel")

        for key,value in questions.items():
            
            # Format
            self.liner()
            self.printer.question_box(questions,information,title)
            option = input(self.printer.question("Enter Input here"))
            
            # Change for next print.
            print("")
            questions[key] = option
            # Choices
            if option == "c":
                
                return
        # Gets the over all reports and prints them
        money = self.logic.filter_earnings(questions["Input Location ID"],questions["Input Date From"],questions["Input Date To"])
        self.liner()
        self.printer.question_box(questions,information,title)
        self.printer.print_space()
        self.printer.print_out_format("Money Made: " + str(money))
        Print_format.print_space(self)
        Print_format.print_title(self,len("Earning Report")*"_")
        go_back = input(self.printer.question("return: "))
        return
#--------------Lets Chuck Norris see reports on vehicles--------------#
    def Vehicle_reports(self):

        self.liner()
        Print_format.print_title(self,"Vehicle Reports")
        self.printer.print_space()

        information = ("ID,Vehicle Name,Type,Manufacturer,Model,Color,Age,Available,Location ID,Licence Type")
        Print_format.print_out_format(self,information)
        vehicle_report = self.logic.get_vehicles()
        Print_format.print_space(self)

        # For loop to iterate through the list and print it out.
        for item in vehicle_report:
            Print_format.print_out_format(self,str(item))
        Print_format.print_line(self,len("Vehicle Reports")*"_")
        go_back = input(self.printer.question("return: "))
        return
        # Hérna þarf að sækja alla bílana frá logic wrappernum, og sýna hvaða bílar eru eftirsóttastir(Finishes)
        # og hvaða rapport yfir alla bílana sem valið er.(Finished)
#--------------Lets Chuck see the over all the bills--------------#
    def Bill_overview(self):
        information = ("Contract ID,Start Date,Return Date,Location ID,Price")
        #Hérna þarf að sækja skýrslu frá samningum og skoða lista af öllum reikningum

        # Format
        self.liner()
        Print_format.print_title(self, "Bill Overview")
        self.printer.print_space()
        Print_format.print_out_format(self, information)
        Print_format.print_space(self)
        bills = self.logic.get_bills()

        # For loop to iterate through the list and print it out.
        for item in bills:
            Print_format.print_out_format(self,str(item))
        Print_format.print_title(self,len("Bill Overview")*"_")
        go_back = input(self.printer.question("return: "))
        return
#--------------Hidden Feature to everyone but Chuck Him Self, Lets him fire employees and kick customers(WARNING, DO NOT TRY TO INPUT CHUCK INTO THIS)--------------#
    def Round_house(self):
        #Something Something Something Dark Side, Somethin Something Something Complete.
        rhk = "Round House Kick"
        information = ("( 1 ) Kill Customer,( 2 ) Fire Employee ")
        
        # Format
        self.liner()
        self.printer.short_box(information,rhk)

        # Hérna kallar hann kill customer og fire employee. Og Round Housar þau. Þarf að fá til baka númer frá föllunum til að setja í print skipunina.(Finished)
        # Here we will input and call the kickdownstairs function.
        who_to_kill = input(self.printer.question("Enter Choice here: "))
        if who_to_kill == "1":
            cust_ID = input(self.printer.question("Enter victim's customer ID "))
            customer = self.logic.get_customer(cust_ID)
            if customer:
                cust_name = customer.customer_name
                print(self.kickdownstairs(cust_name).center(240))
                self.logic.kill_customer(cust_ID)
                go_back = input(self.printer.question("Return"))
            # Error check if customer does not exist.
            else:
                print("Customer not found")
        # Who to kill 
        elif who_to_kill == "2":
            emp_ID = input("Enter victim's employee ID: ")
            if emp_ID == "1":
                self.error_text()
                sys.exit()
            employee = self.logic.get_employee(emp_ID)
            
            if employee:
                emp_name = employee.employee_name
                print(self.kickdownstairs(emp_name).center(240))
                self.logic.fire_employee(emp_ID)
                go_back = input(self.printer.question("Return"))
            # Error check if employee does not exist.
            else:
                print("Employee not found")
        else:
            return
#--------------Lets Chuck see over all the contracts--------------#
    def All_contracts(self):
        # Hérna kallar hann í að sjá lista yfir alla contracts sem hafa gengið í geggnum fyrirtækið.(Finished)
        # Option,info input into a format for sexy print. 
        options = "( r ) return"
        info = "ID,Signed employee,Customer,Vehicle,Destination,Start date,End date,Paid,Day made"

        contracts = self.logic.all_contracts()
        title = "Contract list"
        contract_str_list = []
        for contract in contracts:
            customer = self.logic.get_customer(contract.customer_id)
            cust_name = customer.customer_name
            employee = self.logic.get_employee(contract.employee_id)
            emp_name = employee.employee_name
            vehicle = self.logic.get_vehicle(contract.vehicle_id)
            vehi_name = vehicle.vehicle_name
            destination = self.logic.get_destination(contract.destination_id)
            dest_name = destination.name
            modified_str = str(contract.id)+','+cust_name+','+emp_name+','+vehi_name+','+dest_name+','+str(contract.start_date)+','+str(contract.end_date)+','+str(contract.paid)+','+str(contract.day_made)
            contract_str_list.append(modified_str)
        #Format
        self.liner()
        self.printer.large_list_box(options,title,info,contract_str_list)
        go_back = input(self.printer.question("\tReturn"))
        return
#--------------Ascii art for Round_house--------------#
    def kickdownstairs(self, name):
        # Sexy Ascii print for fire employee and kill customer.
        output = ("""
            THIS IS NAN AIR!

         ○   < Chuck Norris
        <|/
         /
          ┗┓_         V {} V
             ┗┓_         \○/
                ┗┓_    \ / 
                   ┗┓_  /
                      ┗┓
            """).format(name)
        return output
#--------------Error message only used in Round_house--------------#
    def error_text(self):
        print("C̵̬̖̲̫̗̤̱̦͎͉̾͆̔ͅh̷̢̨̛̛͉͈̤̰̺̰̫̲͓̘͔̒́͌͆̽̄ȗ̴͙̭̲̩̪̤̞̥̟̯̅̂̀̈́̅́͠c̴̢̳̫̞͚̟̫̙̠̅̈́͜ͅk̴̦̀͒̓̊ ̶̧̡̯̭̪̖̪̇͛̏̀͆̈́̑̈́͗̾̓̆ͅN̸̩̞͖̻̟̯̞̙̥̞̯̝͂̒̄͝ọ̵͕͇̤̺͆̈̒̇̿́̐͠͝ŕ̶̡̛̰͓̱͓̗̌̑̽̓̋̚r̷̨̧̧̻͇̱̝̥͓͇̠̼̰̓̋̈́̇̏̿́̂͜͜ì̴̢̥̼̝̟̝̤͇͔͕̪̏͝s̷̼̺̥̟͈͕̗͙̹̺͙̋̔̔͜ ̶̣͈̲̺̗̬̻̜͒̇̈́̇̈́̒͒̿̀̿͐̿̏͝ͅa̵̦̬̗̐̓̑̓̿̓t̶̨̩̫̻̠̻͉͖̣͍̟̣̮͑̈̃͊̓̈̊̃̅͂͜ṭ̸̈́ę̵̢̡̛̰̹͉̰̙̥͍̞̍̏͗̈́̓̕ṃ̸̗̩͔̹̤͎͕͖͇̟͍̜̖̂̽͒̔͌͒̈̊̃̌ͅp̷̨̞̙̪͖̳̱̯̖̱̀̊͐̀̿̃͆̄̂̍̚͠ṫ̵̺̠̩͈̀͋͝͝ȅ̸̦͍̬̩̏̍̍̈́̄̾͊͑ͅd̸̡̲̖̳̔͋ ̷̧̡̤̘͕̝̗̃͂͗̅̑͗̽̓̒́̓t̶̺̭͋̓̄͑͛͛̐̓͂̾̕̚͠ͅo̵̥͎̳̜̖̬͖̳͎͉̍̀͒͝ ̴̟̪̑̿̊g̸̡̡̢̮͍̙͖̼̺͖̰͝ę̸̛͈͇̹̦̣̭͚̖̍́͜͠t̴̪̠̒̉̍̊̽̎̓̆̚ ̴͉͕̘̰̝͕̄r̸̢͈̋̌ḯ̶̪͈͖͕̦̞̺̬͙̥̱d̶̨̖̼̳͊̇̆̇ ̶͚̱͔̭̮̭̥̤̙̐̽̏͝͠ͅö̶̭͎͉̠̱͎̥̣̜̤̫̱̠́͑̌̇͐̕͜͜f̵̡̡̨̮͉̭͔͚͍͓͇̞̲̮̙͂̄̐̊̐̄̑̑͘̚ ̵̨̳͔̜͈̥͕͕͚̀́̇͗͒͋̓̄̒̏͛̚͠͠͠ͅh̴̢̨̥͈̦̘̺͖̹̥̩̞̞͛̉̇̀̈́̄̐̉̏͘̚̚͝ͅį̷̡̖͉͙̜̤͚̗͐̉̎͋̋͌̎m̷̡̨͉̙̠͙̊̅̄̚s̷̼͇̋e̸̱̞̺͍͕͉͆̉̍̈́͌͝l̴̢̨̨̢̢͍̼̣̣̜͇̜̜̲̈̔͝f̶̼͉̬̟̙͉̟͕͖̄̎̅̈̍͘,̴̧̛̩̹̤̬͎̍̎͐̍̽̿̇̀̾̾̑͝͠ ̸͖̖͕̻͉̜̰͈̱͕̺̃̈́̂̄̉̀̑͌̑͊͜͝͠t̶͇͍͕͊́̄̀̎̂̃͋͊̄͒̑̈͘ͅh̵̨̪̮̼̺̼̙͓̰̜̬͕̼͗̈́̉̀̌͊̂͝͝͠ĕ̵͈͌͋͊̕͝ ̶̢̑̉͗̓w̵̡̛͔̤̺͍̱͍̮̥̣͔̽͐̎̉̈̄̈͒͊͋̕͜͜͠ỏ̵̬̮̗͎͍̼͉̲͓̋̑͗͌̽̍͑͌̿̂̅͘r̵̥͙̥̈́̑̅͐͆̆͗̌̍̀̂̿͜͠͠l̶̬̗͌͋͂̂́̄́͑́̍̕̕d̴̤͎͕͇͉̙̫̑̄̿̌̑̿̋̕ ̷̨̧̦͚̞̬͔̮̭͕̺̗̻́͗̈́̎ͅį̴̢̡̯̻̘̠̦̩̭̳̱͓̈́̈́̇̽̋̍̓̍̈͗͘͝͠s̷͙̙̭̥͌͋̃̂̎͠ ̵͈͇̃̇̐̈̋̍̀͠e̴̯̽̒̍͆̾̄̒̏̂͛̾̊̕ñ̸̨̤̰̦̠͍̹̻͚̆̽̃͂̿̄̉ͅd̶̨̡̞̥̬̖̪̦̤̤͓̜̦̋́͊̋̐́̽̄͌̇̕͝ỉ̵̛̟̹̹̐̇̏̓̄̄͂̔̔͝ņ̶̢̨̙͉̝͙̖͚̝̱̣̤͉̾̀̑̒̈͂͌̂̌̎̍͛̓ͅg̶͖̥̗̋̂̔͗̓̑̒̊̕,̷͎̠̫̞̩̟̻̳̺͌ ̴̡̟̱͖͉̐̓̿́̅͋̂͐̇̋̕͝͠͝ͅḧ̸̨̧̜̬̤̮̰͙̦͎̬̈́ȁ̵̹̖͖͓͇̞̠͍̬̥̼̈́͛͝ͅv̵̧̢̡̺̟͎̤͉͈̩̆̈́̓͒̃̇̓͑͑ͅe̵̝͇͕̘͕̺̓̈́̀́͋̅͂̌ ̶̎ͅą̶͚̖̠̙̤̳̀̂̍̎͋̈͠ ̸̨̯̦͚̞͍͍̮͓̓̎ň̷̢̥̙̲̝̱̹͉̗̬̝̦͖̐́͝i̴̳̿͑̓͊͊̆̿͛̉̃͌͆͒̾̚ç̷̡̛̜̹̝̝̻̦͓̆͌͂̂̈́͂͝e̴̡̬̳̻̥̘̟̲̱͚͛̀͛͜ ̴̢̖̗̜͙̜̻̘͂́͂́͗͆̂͠d̶̥̬̩̟̟̺̳̮̈́̀̒̓͒͛̃͋͒͌̚a̶̧̞̪̻̱̞̠̦̰̰̱͔̓̈́́̑̚̚ẏ̵̳̳̯͓̼̥͎̪͐̓͌͂͊͛͛̉͜͜͝")
#--------------Lets Chuck see what vehicles are the most popular on given location--------------#
    def popular_vehicle(self):
        # Title,question,information are input into the print formats.
        title = "Most Popular Vehicle"
        question = {"Pick Location ID To See":"empty"}
        information = ("( c ) Cancel")

        # For loop to iterate through the list and print it.
        for key,value in question.items():
            self.liner()
            self.printer.question_box(question,information,title)
            option = input(self.printer.question("Enter Location ID"))
            print("")

            # Change for next print
            question[key] = option

        # Choices
        cars = self.logic.popular_vehicle_types(question["Pick Location ID To See"])
        destination = self.logic.get_destination(option)
        # For loop to iterate through the list and find the most common rented vehicle and print it.
        for key,value in cars.items():
            car = key
            amount = value
            self.printer.print_out_format(f"In {destination.name} " + car +" is the most rented car")

        # Format
        Print_format.print_space(self)
        Print_format.print_title(self,len("Most Popular Vehicle")*"_")
        go_back = input(self.printer.question("\tReturn"))
        return

