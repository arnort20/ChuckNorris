
from UI_classes.RVK_UI import RVK_UI
from UI_classes.Non_RVK_UI import Non_rvk
from UI_classes.Master_login_UI import Master_login

class Login_UI():
    def __init__(self):
        pass

    def login_menu(self):
        print('''
----Login-----''')
        ID_in = input('Employee ID: ')
        #a function should find out if this ID is correct
        password_in = input('')
        #a function should find out if this ID is correct
        if ID_in and password_in:
            ui = RVK_UI()