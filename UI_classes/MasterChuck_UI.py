from Logic_classes.logic_wrapper import LogicAPI
#from UI_classes.Login_UI import LoginUI
from Model_classes.Contract import Contract # Display all contracts overview
#from Model_classes.Vehicle import Vehicle_reports Á eftir að búa til
#from Model_classes.Bill overview bæta inn.


class Master_login():
    def __init__(self):
        self.logic = LogicAPI("1","1")

    def chuck_login(self):
        print("""
    ------------------Welcome Master Chuck!------------------

    ( 1 ) = Review Earnings Report.
    ( 2 ) = View Vehicle Reports.
    ( 3 ) = View Bill Overview.
    ( 4 ) = Round House Kick.
    ( 5 ) = View All Contracts.

    ( q ) = Quit.
    ---------------------------------------------------------\n""")

        while True:
            option = input("Enter Choice here: ")
            if option == "1":
                Master_login().Earnings_report()
                break

            elif option == "2":
                Master_login().Vehicle_reports()
                break

            elif option == "3":
                Master_login().Bill_overview()
                break

            elif option == "4":
                Master_login().Round_house()
                break

            elif option == "5":
                Master_login().All_contracts()
                break

            elif option == "q":
                return False
                
            else:
                print("Not a valid input")
                Master_login().chuck_login()

    def Earnings_report(self):
        # Hérna þarf að sækja overall Reportið í logic wrapper, hérna er speninding vs earnings
        pass
        
    def Vehicle_reports(self):
        # Hérna þarf að sækja alla bílana frá logic wrappernum, og sýna hvaða bílar eru eftirsóttastir
        pass

    def Bill_overview(self):
        # Hérna þarf að sækja skýrslu frá samningum og skoða lista af öllum reikningum
        pass

    def Round_house(self):
        # Hérna kallar hann kill customer og fire employee. Og Round Housar þau. Þarf að fá til baka númer frá föllunum til að setja í print skipunina.
        # Print(f"Employee {} you have been Roundhoused out of this company! ")
        pass

    def All_contracts(self):
        # Hérna kallar hann í að sjá lista yfir alla contracts sem hafa gengið í geggnum fyrirtækið.
        print("----------------------------------- Contract Overview-----------------------------------")
        information = ("ID,Employee ID,Customer ID,Vehicle ID,Start Date,End Date,Paid")
        splitt_info = information.split(",")
        for info in splitt_info:
            print("{:15}".format(info),end="")
           
        print("\n")
        contracts = self.logic.all_contracts()
        for item in contracts:
            new_item = str(item)
            splitted = new_item.split()
            for word in splitted: 
                print("{:8}".format(word),end="")
        print("\n")

        def kickdownstairs(self, name):
            output = """
            THIS IS NAN AIR!
    ○ 
    く|)へ
    〉 
    ￣￣┗┓          {}
    　 　 ┗┓　     ヾ○ｼ
    　　   ┗┓   ヘ/ 　 　 
    　        ┗┓ノ 
    　 　 　 　 　 ┗┓
            """.format(name)
            return output
            
        
    
Master_login().chuck_login()
