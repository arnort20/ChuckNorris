#from UI_classes.MasterChuck_UI import Master_login
from UI_classes.RVK_UI import RVK_emp
from UI_classes.Non_RVK_UI import Non_Rvk
from Logic_classes.logic_wrapper import LogicAPI 

def login_menu():
        print('''
----Login-----''')
        id_in = input('Employee ID: ')
        #a function should find out if this ID is correct
        password_in = input('')
        #a function should find out if this ID is correct
        return id_in, password_in

def check_your_privilege(username, pword):
    lAPI = LogicAPI(username, pword)
    return lAPI.check_privilege()

if __name__ == "__main__":
    username, pword = login_menu()
    location = check_your_privilege(username, pword)
    if location == 1:
        print("welcome, chuck")
        #user = Master_login()
    elif location == 2:
        user = RVK_emp(username, pword)
    elif location == 3:
        user = Non_Rvk(username, pword)
    else:
        print("Invalid username-password combination!")


