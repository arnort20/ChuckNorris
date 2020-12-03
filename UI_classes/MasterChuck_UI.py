#from UI_classes.Login_UI import LoginUI


class Master_login():
    def __init__(self):
        self

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
                print("Not a valid input ")
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
        #Print(f"Employee {} you have been Roundhoused out of this company! ")
        pass

    def All_contracts(self):
        # Hérna kallar hann í að sjá lista yfir alla contracts sem hafa gengið í geggnum fyrirtækið.
        pass
    
Master_login().chuck_login()
