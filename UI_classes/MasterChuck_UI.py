from Logic_classes.logic_wrapper import LogicAPI
from Model_classes.Contract import Contract # Display all contracts overview
#from Model_classes.Vehicle import Vehicle_reports Á eftir að búa til
#from Model_classes.Bill overview bæta inn.
from UI_classes.Print_formats import Print_format
import sys #Spurning að breyta yfir í orginal loggin skjá

class Master_login():
    def __init__(self, username, pword):
        self.logic = LogicAPI(username, pword)
        

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

    def returner(self):
        print("")
        return_to_mainmenu = input("Would Mr.Chuck like to return to the Main Menu? y/n: ")
        if return_to_mainmenu == "y":
            self.chuck_login()
        else:
            return None

    def chuck_login(self):
        menus = True
        title = "Welcome Master Chuck!"
        Print_format.print_title(self,title)
        option = "( 1 ) Review Earnings Report,( 2 ) View Vehicle Reports,( 3 ) View Bill Overview,( 4 ) Round House Kick,( 5 ) View All Contracts,( q ) Quit"
        Print_format.print_main_menu(self,option)
        Print_format.print_title(self,len(title)*"-")


        option = input("Enter Choice here: ")
        while menus:
            if option == "q":
                menus = False
                sys.exit() # Þessu hérna

            elif option == "1":
                Master_login().Earnings_report()
                menus = False

            elif option == "2":
                Master_login().Vehicle_reports()
                menus = False

            elif option == "3":
                Master_login().Bill_overview()
                menus = False

            elif option == "4":
                Master_login().Round_house()
                menus = False

            elif option == "5":
                Master_login().All_contracts()
                menus = False

            else:
                print("Not a valid input!" "\n")
                Master_login().chuck_login()

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
        # Print_format.print_title("Round House Kick")
        # information = ("( 1 ) Kill Customer,( 2 ) Fire Employee ")
        #Something Something Something Dark Side
        # Hérna kallar hann kill customer og fire employee. Og Round Housar þau. Þarf að fá til baka númer frá föllunum til að setja í print skipunina.
        # Print(f"Employee {} you have been Roundhoused out of this company! ")
        pass

    def All_contracts(self):
        # Hérna kallar hann í að sjá lista yfir alla contracts sem hafa gengið í geggnum fyrirtækið.
        Print_format.print_title(self,"Contract Overview")
        information = ("ID,Employee ID,Customer ID,Vehicle ID,Start Date,End Date,Paid")
        Print_format.print_out_format(self,information)
        contracts = self.logic.all_contracts()
        for item in contracts:
            Print_format.print_out_format(self,str(item))
        Print_format.print_title(self,len("Contract Overview")*"-")

        Master_login.returner(self)


    def kickdownstairs(self, name):
        output = ("""
            THIS IS NAN AIR!
        ○
        く|)へ
        〉
        ￣￣┗┓_         {}
    　 　      ┗┓_     ヾ○ｼ
    　　          ┗┓_   ヘ/ 　 　
    　               ┗┓ノ_
    　 　 　 　 　        ┗┓
            """).format(name)
        return output



Master_login().chuck_login()
