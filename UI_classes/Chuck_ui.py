from Logic_classes.Logic_API import Logic_API
from Model_classes.Contract import Contract # Display all contracts overview
from Model_classes.Vehicle import Vehicle
from Model_classes.Bill import Bill
from UI_classes.Print_formats import Print_format
from UI_classes.Rvk_ui import Rvk_ui
import sys #Spurning að breyta yfir í orginal loggin skjá

"""
3
As Chuck Norris and/or employee of NaN Air I need to be able to 
register new employees, a list of their information, and their position
    check
10
As an employee of NaN Air I need to be able to register and list all rental 
contracts
"""

class Chuck_ui():

    def liner(self):
        print("\n"*12)
        
    def __init__(self, username, pword):
        self.logic = Logic_API(username, pword)
        self.printer = Print_format()
        
        
    def chuck_login(self):
        menus = True

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



    def add_new_employee(self):
        title = 'New Employee'
        questions = {"name":"empty","ssn":"empty","address":"empty","location_id":"empty","email":"empty","phone":"empty","password":"empty","confirm password":"empty"}
        information = ("( c ) Cancel, ( f ) Finish")        

        while True:
            for key,value in questions.items():

                #Format
                self.liner()
                self.printer.question_box(questions,information,title)
                option = input(self.printer.question('Type here: '))

                #change for next print
                questions[key] = option

                #Choices
                if questions["password"] != questions["confirm password"]:
                    self.printer.warning("passwords don't match")
                if option == 'c':
                    return
                elif option == 'f' and questions["confirm password"] != "empty" :
                    questions["emp_name"] = questions["name"]
                    self.logic.hire_employee(questions["emp_name"],questions["ssn"],questions["address"],questions["phone"],questions["email"],questions["location_id"],questions["password"],)
                    return



    def Earnings_report(self):
        # Hérna þarf að sækja overall Reportið í logic wrapper, spendinding vs earnings
        # Mögulega eitthvað fleirra
        questions = {"Input Location ID":"empty","Input Date From":"empty","Input Date To":"empty"}
        title = "Earnings Report"
        information = ("Date Format = (yy.mm.dd),( c ) Cancel")

        for key,value in questions.items():

            self.liner()
            self.printer.question_box(questions,information,title)
            option = input(self.printer.question("Enter Input here"))

            print("")
            questions[key] = option

            if option == "c":
                return
        money = self.logic.filter_earnings(questions["Input Location ID"],questions["Input Date From"],questions["Input Date To"])
        self.liner()
        self.printer.question_box(questions,information,title)
        self.printer.print_space()
        self.printer.print_out_format("Money Made: " + str(money))
        Print_format.print_space(self)
        Print_format.print_title(self,len("Earning Report")*"_")
        go_back = input(self.printer.question("return: "))
        return

        


    def Vehicle_reports(self):

        self.liner()
        Print_format.print_title(self,"Vehicle Reports")
        self.printer.print_space()

        information = ("ID,Vehicle Name,Type,Manufacturer,Model,Color,Age,Tax,Available,Location ID,Licence Type")
        Print_format.print_out_format(self,information)
        vehicle_report = self.logic.get_vehicles()
        Print_format.print_space(self)

        for item in vehicle_report:
            Print_format.print_out_format(self,str(item))
        Print_format.print_line(self,len("Vehicle Reports")*"_")
        go_back = input(self.printer.question("return: "))
        return
        # Hérna þarf að sækja alla bílana frá logic wrappernum, og sýna hvaða bílar eru eftirsóttastir
        # og hvaða rapport yfir alla bílana sem valið er.



    def Bill_overview(self):
        information = ("Contract ID,Start Date,Return Date,Location ID,Price")
        #Hérna þarf að sækja skýrslu frá samningum og skoða lista af öllum reikningum

        #Format
        self.liner()
        Print_format.print_title(self, "Bill Overview")
        self.printer.print_space()
        Print_format.print_out_format(self, information)
        Print_format.print_space(self)
        bills = self.logic.get_bills()


        for item in bills:
            Print_format.print_out_format(self,str(item))
        Print_format.print_title(self,len("Bill Overview")*"_")
        go_back = input(self.printer.question("return: "))
        return

    def Round_house(self):
        rhk = "Round House Kick"
        information = ("( 1 ) Kill Customer,( 2 ) Fire Employee ")


        self.liner()
        self.printer.print_title(rhk)
        self.printer.print_out_format(information)

        #Something Something Something Dark Side
        who_to_kill = input(self.printer.question("Enter Choice here: "))
        # Hérna kallar hann kill customer og fire employee. Og Round Housar þau. Þarf að fá til baka númer frá föllunum til að setja í print skipunina.
        if who_to_kill == "1":
            cust_ID = input("Enter victim's customer ID ")
            customer = self.logic.get_customer(cust_ID)
            if customer:
                cust_name = customer.customer_name
                print(self.kickdownstairs(cust_name))
                self.logic.kill_customer(cust_ID)

            else:
                print("Customer not found")

        elif who_to_kill == "2":
            emp_ID = input("Enter victim's employee ID: ")
            if emp_ID == "1":
                self.error_text()
                sys.exit()
            employee = self.logic.get_employee(emp_ID)


            if employee:
                emp_name = employee.employee_name
                print(self.kickdownstairs(emp_name))
                self.logic.fire_employee(emp_ID)
            else:
                print("Employee not found")
        else:
            return

    def All_contracts(self):
        # Hérna kallar hann í að sjá lista yfir alla contracts sem hafa gengið í geggnum fyrirtækið.
        options = "( r ) return"
        info = "ID,employee ID,customer ID,vehicle ID,destination ID,start date,end date,paid?"

        contracts = self.logic.all_contracts()
        title = "Contract list"

        #Format
        self.liner()
        self.printer.large_list_box(options,title,info,contracts)
        go_back = input(self.printer.question("\tReturn"))
        return
 

    def kickdownstairs(self, name):
        output = ("""
            THIS IS NAN AIR!

         ○   < Chuck Norris
        く|)へ
          〉
        ￣￣┗┓_         V {} V
    　 　      ┗┓_       ヾ○ｼ
    　　          ┗┓_   ヘ/ 　 　
    　               ┗┓_ノ
    　 　 　 　 　      ┗┓
            """).format(name)
        return output

    def error_text(self):
        print("C̵̬̖̲̫̗̤̱̦͎͉̾͆̔ͅh̷̢̨̛̛͉͈̤̰̺̰̫̲͓̘͔̒́͌͆̽̄ȗ̴͙̭̲̩̪̤̞̥̟̯̅̂̀̈́̅́͠c̴̢̳̫̞͚̟̫̙̠̅̈́͜ͅk̴̦̀͒̓̊ ̶̧̡̯̭̪̖̪̇͛̏̀͆̈́̑̈́͗̾̓̆ͅN̸̩̞͖̻̟̯̞̙̥̞̯̝͂̒̄͝ọ̵͕͇̤̺͆̈̒̇̿́̐͠͝ŕ̶̡̛̰͓̱͓̗̌̑̽̓̋̚r̷̨̧̧̻͇̱̝̥͓͇̠̼̰̓̋̈́̇̏̿́̂͜͜ì̴̢̥̼̝̟̝̤͇͔͕̪̏͝s̷̼̺̥̟͈͕̗͙̹̺͙̋̔̔͜ ̶̣͈̲̺̗̬̻̜͒̇̈́̇̈́̒͒̿̀̿͐̿̏͝ͅa̵̦̬̗̐̓̑̓̿̓t̶̨̩̫̻̠̻͉͖̣͍̟̣̮͑̈̃͊̓̈̊̃̅͂͜ṭ̸̈́ę̵̢̡̛̰̹͉̰̙̥͍̞̍̏͗̈́̓̕ṃ̸̗̩͔̹̤͎͕͖͇̟͍̜̖̂̽͒̔͌͒̈̊̃̌ͅp̷̨̞̙̪͖̳̱̯̖̱̀̊͐̀̿̃͆̄̂̍̚͠ṫ̵̺̠̩͈̀͋͝͝ȅ̸̦͍̬̩̏̍̍̈́̄̾͊͑ͅd̸̡̲̖̳̔͋ ̷̧̡̤̘͕̝̗̃͂͗̅̑͗̽̓̒́̓t̶̺̭͋̓̄͑͛͛̐̓͂̾̕̚͠ͅo̵̥͎̳̜̖̬͖̳͎͉̍̀͒͝ ̴̟̪̑̿̊g̸̡̡̢̮͍̙͖̼̺͖̰͝ę̸̛͈͇̹̦̣̭͚̖̍́͜͠t̴̪̠̒̉̍̊̽̎̓̆̚ ̴͉͕̘̰̝͕̄r̸̢͈̋̌ḯ̶̪͈͖͕̦̞̺̬͙̥̱d̶̨̖̼̳͊̇̆̇ ̶͚̱͔̭̮̭̥̤̙̐̽̏͝͠ͅö̶̭͎͉̠̱͎̥̣̜̤̫̱̠́͑̌̇͐̕͜͜f̵̡̡̨̮͉̭͔͚͍͓͇̞̲̮̙͂̄̐̊̐̄̑̑͘̚ ̵̨̳͔̜͈̥͕͕͚̀́̇͗͒͋̓̄̒̏͛̚͠͠͠ͅh̴̢̨̥͈̦̘̺͖̹̥̩̞̞͛̉̇̀̈́̄̐̉̏͘̚̚͝ͅį̷̡̖͉͙̜̤͚̗͐̉̎͋̋͌̎m̷̡̨͉̙̠͙̊̅̄̚s̷̼͇̋e̸̱̞̺͍͕͉͆̉̍̈́͌͝l̴̢̨̨̢̢͍̼̣̣̜͇̜̜̲̈̔͝f̶̼͉̬̟̙͉̟͕͖̄̎̅̈̍͘,̴̧̛̩̹̤̬͎̍̎͐̍̽̿̇̀̾̾̑͝͠ ̸͖̖͕̻͉̜̰͈̱͕̺̃̈́̂̄̉̀̑͌̑͊͜͝͠t̶͇͍͕͊́̄̀̎̂̃͋͊̄͒̑̈͘ͅh̵̨̪̮̼̺̼̙͓̰̜̬͕̼͗̈́̉̀̌͊̂͝͝͠ĕ̵͈͌͋͊̕͝ ̶̢̑̉͗̓w̵̡̛͔̤̺͍̱͍̮̥̣͔̽͐̎̉̈̄̈͒͊͋̕͜͜͠ỏ̵̬̮̗͎͍̼͉̲͓̋̑͗͌̽̍͑͌̿̂̅͘r̵̥͙̥̈́̑̅͐͆̆͗̌̍̀̂̿͜͠͠l̶̬̗͌͋͂̂́̄́͑́̍̕̕d̴̤͎͕͇͉̙̫̑̄̿̌̑̿̋̕ ̷̨̧̦͚̞̬͔̮̭͕̺̗̻́͗̈́̎ͅį̴̢̡̯̻̘̠̦̩̭̳̱͓̈́̈́̇̽̋̍̓̍̈͗͘͝͠s̷͙̙̭̥͌͋̃̂̎͠ ̵͈͇̃̇̐̈̋̍̀͠e̴̯̽̒̍͆̾̄̒̏̂͛̾̊̕ñ̸̨̤̰̦̠͍̹̻͚̆̽̃͂̿̄̉ͅd̶̨̡̞̥̬̖̪̦̤̤͓̜̦̋́͊̋̐́̽̄͌̇̕͝ỉ̵̛̟̹̹̐̇̏̓̄̄͂̔̔͝ņ̶̢̨̙͉̝͙̖͚̝̱̣̤͉̾̀̑̒̈͂͌̂̌̎̍͛̓ͅg̶͖̥̗̋̂̔͗̓̑̒̊̕,̷͎̠̫̞̩̟̻̳̺͌ ̴̡̟̱͖͉̐̓̿́̅͋̂͐̇̋̕͝͠͝ͅḧ̸̨̧̜̬̤̮̰͙̦͎̬̈́ȁ̵̹̖͖͓͇̞̠͍̬̥̼̈́͛͝ͅv̵̧̢̡̺̟͎̤͉͈̩̆̈́̓͒̃̇̓͑͑ͅe̵̝͇͕̘͕̺̓̈́̀́͋̅͂̌ ̶̎ͅą̶͚̖̠̙̤̳̀̂̍̎͋̈͠ ̸̨̯̦͚̞͍͍̮͓̓̎ň̷̢̥̙̲̝̱̹͉̗̬̝̦͖̐́͝i̴̳̿͑̓͊͊̆̿͛̉̃͌͆͒̾̚ç̷̡̛̜̹̝̝̻̦͓̆͌͂̂̈́͂͝e̴̡̬̳̻̥̘̟̲̱͚͛̀͛͜ ̴̢̖̗̜͙̜̻̘͂́͂́͗͆̂͠d̶̥̬̩̟̟̺̳̮̈́̀̒̓͒͛̃͋͒͌̚a̶̧̞̪̻̱̞̠̦̰̰̱͔̓̈́́̑̚̚ẏ̵̳̳̯͓̼̥͎̪͐̓͌͂͊͛͛̉͜͜͝")





    def popular_vehicle(self):
        title = "Most Popular Vehicle"
        question = {"Pick Location ID To See":"empty"}
        information = ("( c ) Cancel")


        for key,value in question.items():
            self.liner()
            self.printer.question_box(question,information,title)
            option = input(self.printer.question("Enter Location ID"))
            print("")
            question[key] = option


        cars = self.logic.popular_vehicle_types(question["Pick Location ID To See"])
        destination = self.logic.get_destination(option)

        for key,value in cars.items():
            car = key
            amount = value
            self.printer.print_out_format(f"In {destination.name} " + car +" is the most rented car")

        Print_format.print_space(self)
        Print_format.print_title(self,len("Most Popular Vehicle")*"_")
        go_back = input(self.printer.question("\tReturn"))
        return

