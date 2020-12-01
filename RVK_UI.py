class RVK_emp():
    def __init__(self):
        self.employee_num = '69'

    def main_menu(self):
        print(
        '''----------------------Welcome, Employee {}----------------------
        
( 1 ) = Create new contract
( 2 ) = View contract
( 3 ) = Print contract
( 4 ) = Print report
( 5 ) = Add new employee
( 6 ) = Change employee
( 7 ) = Delete employee

( q ) = Quit
-------------------------------------------------------------------------------'''.format(self.employee_num))

        option = input('Type here: ')
        if option == '1':
            RVK_emp().menu1()
        elif option == '2':
            RVK_emp().menu2()
        elif option == '3':
            RVK_emp().menu3()
        elif option == '4':
            RVK_emp().menu4()
        elif option == '5':
            RVK_emp().menu5()
        elif option == '6':
            RVK_emp().menu6()
        elif option == '7':
            RVK_emp().menu7()
        elif option == 'q':
            return
        else:
            print('Not a valid option!')
            RVK_emp().main_menu()
    
    def menu1(self):
        print('''
-----Creating new Contract-------------------------------------
        
( 1 ) = Returning Customer
( 2 ) = New Customer

( r ) = Return
---------------------------------------------------------------''')
        option = input('Type here: ')
        if option == '1':
            RVK_emp().menu1_1
        if option == '2':
            RVK_emp().menu1_2
        if option == 'r':
            RVK_emp().main_menu()

    def menu2(self):
        print('''
------------Contract search-------------
 ''')
        conID = input('Contract ID: #')
        if len(conID) == 4 and conID.isdigit():
            print('Great Success!') #Don't really know what to add here
            #add three options ( c ) change, ( p ) print, ( r ) return
            RVK_emp().main_menu()
        else:
            print('Invalid contract ID!')
            RVK_emp().menu2() 

    def menu3(self):
        #Couldn't print contract just be a part of menu 2
        pass

    def menu4(self):
        #I might do it fokking later
        pass

    def menu5(self):
        print('''
------------------------New Employee-------------------------
''')
        empID = input('Employee ID: #') #should check whether a number is taken or not
        emp_name = input('\nName: ')
        emp_ssn = input('Social Security Number: ')
        emp_address = input('\nAddress: ')
        emp_location = input('Location: ')
        emp_email = input('\nEmail: ')
        emp_homephone = input('Home Telephone: ')
        emp_mobilephone = input('Mobile Phone: ')
        while True:
            emp_password = input('\nPassword: ')
            confirm_password = input('Confirm Password: ')
            if emp_password == confirm_password:
                break
            print('Passwords are not the same')
        while True:
            print('''

Add employee( y ):
Return ( r ):
--------------------------------------------------------------------
''')
            option = input('Type here: ')
            if option == 'y':
                emp_info = [emp_name, emp_ssn, emp_address, emp_location, emp_email, emp_homephone, emp_mobilephone, emp_password]
                emp_dict = {}
                emp_dict[empID] = emp_info #Here's is where the employee is added
            elif option == 'r':
                RVK_emp().main_menu()
            else:
                print('Not a valid option')

    def menu6(self):
        print('''
------------------------Change Employee------------------
''')
        empID = '21'
        emp_name = 'Herra Dæmi'
        emp_ssn = '200469-1337'
        emp_address = 'Órafjarlýju 42'
        emp_location = 'Þarna'
        emp_email = 'peepee@poopoo.com'
        emp_homephone = '800-588-2300'
        emp_mobilephone = '2'
        emp_password = 'chiblade'
        emp_info = [emp_name, emp_ssn, emp_address, emp_location, emp_email, emp_homephone, emp_mobilephone, emp_password]
        info_list = ['Name:', 'Social security number:', 'Address:', 'Location:', 'Email:', 'Home phone number:', 'Mobile phone number:', 'Password:']
        info_list2 = ['name',  'ssn', 'address', 'location', 'email', 'home phone', 'mobile phone', 'password']
        search = input('Employee ID: ') #the output should be able to extract a list of information from the employee id
        #here should emp_info come from the data bank
        for i in range(len(emp_info)):
            if info_list[i] == 'Password:':
                hidden_password = ''
                for i in range(len(emp_info[i])):
                    hidden_password += '*'
                print(info_list[i],hidden_password)
                option = input('change? ( y / n ): ')
                if option == 'y':
                    new = input('New {}: '.format(info_list2[i]))
                    emp_info[i] = new
            else:
                print(info_list[i],emp_info[i])
                option = input('change? ( y / n ): ')
                if option == 'y':
                    new = input('New {}: '.format(info_list2[i]))
                    emp_info[i] = new
            #return emp_info to data bank
        RVK_emp().main_menu()

    def menu7(self):
        print('''
------------------------Change Employee------------------
''')
        search = input('Employee ID: ')
        #here should emp_info come from the data bank
        delete_confirm = input('\nConfirm ( y / n )')
        if delete_confirm == 'y':
            emp_info = []
        RVK_emp().main_menu()   



RVK_emp().main_menu()