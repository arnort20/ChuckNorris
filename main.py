from UI_classes.Chuck_ui import Chuck_ui
from UI_classes.Rvk_ui import Rvk_ui
from UI_classes.Non_rvk_ui import Non_rvk_ui
from Logic_classes.Logic_API import Logic_API


def login_menu():
        print('''
----Login-----''')
        id_in = input('Employee ID: ')
        #a function should find out if this ID is correct
        password_in = input('Password: ')
        #a function should find out if this ID is correct
        return id_in, password_in

def check_your_privilege(username, pword):
    lAPI = Logic_API(username, pword)
    return lAPI.check_privilege()

if __name__ == "__main__":
    username, pword = login_menu()
    location = check_your_privilege(username, pword)
    if location == "1":
        user = Chuck_ui(username, pword)
        user.chuck_login()
    elif location == "2":
        user = Rvk_ui(username,pword)
        user.main_menu()
    elif location == 3:
        user = Non_rvk_ui(username, pword)
        user.main_menu()
    else:
        print("Invalid username-password combination!")



