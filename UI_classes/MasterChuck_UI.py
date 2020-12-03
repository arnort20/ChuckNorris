#from UI_classes.Login_UI import LoginUI


class Master_login():
    def __init__(self):
        pass

    def chuck_login(self):
        print("""
    ------------------Welcome Master Chuck!------------------

    ( 1 ) = Review Earnings Report.
    ( 2 ) = View Vehicle Reports.
    ( 3 ) = View Bill Overview.
    ( 4 ) = Round House Kick.

    ( q ) = Quit.
    ---------------------------------------------------------\n""")

    option = input("Enter Choice here")
    while True:

        if option == "1":
            Master_login().Earnings_report()
        elif option == "2":
            Master_login().Vehicle_reports()
        elif option == "3":
            Master_login().Bill_overview()
        elif option == "4":
            Master_login().Round_house()
        elif option == "q":
            break
        else:
            print("Not a valid input ")
            Master_login().chuck_login()

    def Earnings_report():
        pass
    
    def Vehicle_reports():
        pass

    def Bill_overview():
        pass

    def Round_house():
        pass

    
    
