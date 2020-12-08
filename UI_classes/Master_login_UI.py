from Logic_classes.logic_API import Logic_API
from Model_classes.Contract import Contract # Display all contracts overview
#from Model_classes.Vehicle import Vehicle_reports Á eftir að búa til
#from Model_classes.Bill overview bæta inn.
from UI_classes.Print_formats import Print_format
import sys #Spurning að breyta yfir í orginal loggin skjá

"""
3
As Chuck Norris and/or employee of NaN Air I need to be able to 
register new employees, a list of their information, and their position

10
As an employee of NaN Air I need to be able to register and list all rental 
contracts
"""

class Master_login():
    def __init__(self, username, pword):
        self.logic = Logic_API(username, pword)
        self.printer = Print_format()
        
    # Upprunalega print formatið ef hitt skyldi fara í klessu!
    # def print_title(self,title):
    #     # Title = Nafn á Völdum kosti
    #     print("")
    #     name_title = ('{:-^125}'.format(title))
    #     print(name_title)
    #     #Þurfum ekki að hafa center með þessu formati
    #     print("")

    # def print_main_menu(self,option):
    #     # Prentar út Main menu textan í ákveðnu formati
    #     splitt_info = option.split(",")
    #     for info in splitt_info:
    #         print("|{:^40}|".format(info))
    #         #Þurfum ekki að hafa center með þessu formati
    #         #print("{0: >40}".format(info))

    # def print_out_format(self,information):
    #     # Information = Efsta línan sem er upplysingar um hvað er hvað.
    #     splitt_info = information.split(",")
    #     for info in splitt_info:
    #         print(info.center(20), end="")

    #    print("")

    def chuck_login(self):
        menus = True
        title = "Welcome Master Chuck!"
        Print_format.print_title(self,title)
        option = "( 1 ) Review Earnings Report,( 2 ) View Vehicle Reports,( 3 ) View Bill Overview,( 4 ) Round House Kick,( 5 ) View All Contracts,,( q ) Quit"
        self.printer.print_main_menu(option)
        Print_format.print_line(self,len(title)*"_")


        option = input(self.printer.question("Enter Choice here: "))
        while menus:
            if option == "q":
                menus = False
                sys.exit() # Þessu hérna

            elif option == "1":
                self.Earnings_report()
                menus = False

            elif option == "2":
                self.Vehicle_reports()
                menus = False

            elif option == "3":
                self.Bill_overview()
                menus = False

            elif option == "4":
                self.Round_house()
                menus = False

            elif option == "5":
                self.All_contracts()
                menus = False

            else:
                print("Not a valid input!" "\n")
                self.chuck_login()

    def Earnings_report(self):
        # Print_format.print_title(self, "Earning Report")
        # information = ("Something fun")
        # Print_format.print_out_format(self,information)
        # #earnings = self.logic_wrapper.HER COMES EARNINGS REPORT
        # for item in earnings:
        #     Print_format.print_out_format(self,str(item))
        #     Print_format.print_title(self,len("Earning Report")*"-")
        # Hérna þarf að sækja overall Reportið í logic wrapper, spendinding vs earnings
        # Mögulega eitthvað fleirra
        # Add a Returner
        pass

    def Vehicle_reports(self):
        # Print_format.print_title(self,"Vehicle Reports")
        # information = ("Something about cars")
        # Print_format.print_out_format(self,information)
        # vehicle_report = self.logic_wrapper.Vehicle_reports <---- Possible change
        # for item in vehicle_report:
        #     Print_format.print_out_format(self,str(vehicle_report))
        #     Print_format.print_title(self,len("Vehicle Reports")*"-")
        # Hérna þarf að sækja alla bílana frá logic wrappernum, og sýna hvaða bílar eru eftirsóttastir
        # og hvaða rapport yfir alla bílana sem valið er.
        #Add a Returner
        pass

    def Bill_overview(self):
        # #Hérna þarf að sækja skýrslu frá samningum og skoða lista af öllum reikningum
        # Print_format.print_title(self, "Bill Overview")
        # information = ("info")
        # Print_format.print_out_format(self, information)
        # bills = self.logic.Bill_overview() <---- Possible change
        # for item in bills:
        #      Print_format.print_out_format(self,str(item))
        #      Print_format.print_title(self,len("Bill Overview")*"-")

        pass
    def Round_house(self):
        rhk = "Round House Kick"
        self.printer.print_title(rhk)
        information = ("( 1 ) Kill Customer,( 2 ) Fire Employee ")
        self.printer.print_out_format(information)
        #Something Something Something Dark Side
        who_to_kill = input(self.printer.question("Enter Choice here: "))
        # Hérna kallar hann kill customer og fire employee. Og Round Housar þau. Þarf að fá til baka númer frá föllunum til að setja í print skipunina.
        if who_to_kill == "1":
            cust_ID = input("Enter victim's customer ID ")
            customer = self.logic.get_customer(cust_ID)
            if customer:
                cust_name = customer.customer_name
                self.kickdownstairs(cust_name)
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
        self.printer.print_title("Contract Overview")
        information = ("ID,Employee ID,Customer ID,Vehicle ID,Destination ID,Start Date,End Date,Paid")
        self.printer.print_out_format(information)
        contracts = self.logic.all_contracts()
        for item in contracts:
            self.printer.print_out_format(str(item))
        self.printer.print_line(len("Contract Overview")*"_")
        
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

