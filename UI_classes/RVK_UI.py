class RVK_emp():
    def __init__(self):
        self.employee_num = '69'

    def main_menu(self):
        print(
        '''----------------------Welcome, Employee {}----------------------
        
( 1 ) = Create new contract
( 2 ) = View contract
( 3 ) = Print report
( 4 ) = Add new employee
( 5 ) = Change employee
( 6 ) = Delete employee

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
            RVK_emp().menu1_1()
        if option == '2':
            RVK_emp().menu1_2()
        if option == 'r':
            RVK_emp().main_menu()

    def menu1_1(self):
        print('''
-----Returning Customer------''')
        option = input('Driving registration nr :')
        while True:
            print('''
( r ) = Return
( f ) = Finish
------------------------------------------''')
            option = input('Type here: ')
            if option == 'r':
                RVK_emp().menu1()
            elif option == 'f':
                #finish?
                pass
            else:
                print('Invalid option')

    def menu1_2(self):
        print('''
----New customer---------------------''')
        cust_info = []
        info_list = ['Name: ', 'License #: ', 'Phone number: ','Address: ', 'Email: ', "Driver's licence type: "]
        for i in range(len(info_list)):
            info = input('{}'.format(info_list[i]))
            cust_info.append(info)
        while True:
            print(''' 
( r ) = Return
( f ) = Finish
------------------------------------------''')
            option = input('Type here: ')
            if option == 'r':
                RVK_emp().menu1()
            if option == 'f':
                #finish?
                pass
            else:
                print('Invalid option')
        

    def menu2(self):
        print('''
------------Contract search-------------
 ''')
        conID = input('Contract ID: #')
        if len(conID) == 4 and conID.isdigit():
            print('Great Success!') #Don't really know what to add here
            #add three options ( c ) change, ( p ) print, ( r ) return
            print('''\n( c ) change
( p ) print
( r ) return
----------------------------------------''')
            while True:
                option = input('Type here: ')
                if option == 'c':
                    RVK_emp().menu2_1()
                elif option == 'p':
                    RVK_emp().menu2_2()
                elif option == 'r':
                    RVK_emp().main_menu()
                else:
                    print('Not a valid option')
        else:
            print('Invalid contract ID!')
            RVK_emp().menu2() 

    def menu2_1(self):
        'Changes contract info'
        plate_num = 'BR UH21'
        start = 'yesterday'
        end = 'today'
        info_list = ['Vehicle plate: ', 'Start date: ', 'End date: ']
        contract_info = [plate_num, start, end]
        print('''
------------Changing contract---------------
''')
        for i in range(len(info_list)):
            option = input('{}{}\nchange? ( y / n ): '.format(info_list[i],contract_info[i]))
        while True:
            print('''
 
( f ) = finish
( c ) = Cancel
----------------------------------------''')
            option = input('Type Here: ')
            if option == 'c':
                RVK_emp().menu2()
            elif option == 'f':
                #finish?
                pass
            else:
                print('Not a valid option!')

    def menu2_2(self):
        'Prints contract'
    def menu3(self):
        #I might do it fokking later
        pass

    def menu4(self):
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

    def menu5(self):
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

    def menu6(self):
        print('''
------------------------Change Employee------------------
''')
        search = input('Employee ID: ')
        #here should emp_info come from the data bank
        delete_confirm = input('\nConfirm ( y / n )')
        if delete_confirm == 'y':
            #kalla á logicið til þess að eyða
            pass
        RVK_emp().main_menu()   



RVK_emp().main_menu()