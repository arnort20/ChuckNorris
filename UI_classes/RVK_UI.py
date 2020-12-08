from Logic_classes.logic_API import Logic_API
from UI_classes.Print_formats import Print_format

import datetime


class RVK_emp:
    def __init__(self, username, pword):
        self.employee_num = username
        self.pword = pword
        self.logic = Logic_API(username, pword)

    def main_menu(self):
        title = "(Welcome, Employee {})".format(self.employee_num)
        print_format.print_title(self,title)
        option = "( 1 ) Create new contract,( 2 ) View contract,( 3 ) Print report,( 4 ) Add new employee,( 5 ) Change employee, ( 6 ) Delete employee,( q )  Quit "
        print_format.print_main_menu(self,option)
        print_format.print_title(self,len(title)*"-")

        while True:

            option = input('Type here: ')
            if option == '1':
                RVK_emp(self.employee_num, self.pword).create_contract()
            elif option == '2':
                RVK_emp(self.employee_num, self.pword).view_contract()
            elif option == '3':
                RVK_emp(self.employee_num, self.pword).print_report()
            elif option == '4':
                RVK_emp(self.employee_num, self.pword).add_new_employee()
            elif option == '5':
                RVK_emp(self.employee_num, self.pword).change_employee()
            elif option == '6':
                RVK_emp(self.employee_num, self.pword).delete_employee()
            elif option.lower() == 'q':
                return
                #maybe go back to loginUI?
            elif option == '':
                    print('Please input an option')
            else:
                print('Not a valid option')
                RVK_emp(self.employee_num, self.pword).main_menu()
    




    def create_contract(self):
        while True:
            Print_format.print_title("Creating New Contract")
            information = ("( 1 ) Returning Customer,( 2 ) New Customer, ( r ) Return")
            Print_format.print_out_format(self, information)

            option = input('Type here: ')
            if option == '1':
                RVK_emp(self.employee_num, self.pword).returning_customer()
            elif option == '2':
                RVK_emp(self.employee_num, self.pword).new_customer()
            elif option.lower() == 'r':
                RVK_emp(self.employee_num, self.pword).main_menu()
            elif option == '':
                print('Please input an option')
            else:
                print('Invalid option')




    def returning_customer(self):
        print_format.print_title(self,"Returning Customer")
        information = ("( c ) Cancel, ( f ) Finish")
        print('''
-----Returning Customer-------------------''')
        cost_reg = input('Driving registration nr: ')
        while True:
            print('''
( c ) = Cancel
( f ) = Finish
------------------------------------------''')
            option = input('Type here: ').lower()
            if option == 'c':
                RVK_emp(self.employee_num, self.pword).create_contract()
            elif option == 'f':
                #finds the costumer and creates a new contract
                RVK_emp(self.employee_num, self.pword).menu1_3(1)
            elif option == '':
                print('Please input an option')
            else:
                print('Invalid option')




    def new_customer(self):
        print('''
----New customer---------------------''')
        cust_info = []
        info_list = ['Name: ', 'License #: ', 'Phone number: ','Address: ', 'Email: ', "Driver's licence type: "]
        for i in range(len(info_list)):
            info = input('{}'.format(info_list[i]))
            cust_info.append(info)
        while True:
            print(''' 
( c ) = Cancel
( f ) = Finish
------------------------------------------''')
            option = input('Type here: ').lower()
            if option == 'c':
                RVK_emp(self.employee_num, self.pword).create_contract()
            elif option == 'f':
                #register new costumer and create new contract
                RVK_emp(self.employee_num, self.pword).menu1_3(2)
                pass
            elif option == '':
                print('Please input an option')
            else:
                print('Invalid option')
        



    def menu1_3(self, previous):
        #previous says from what menu you came from
        print('''
-----Creating new Contract------
good boy points: {}''')#here should good boy points be extracted from data
        while True:
            use_gbp = input('Use Good Boy Points ( y / n ): ')
            if use_gbp == 'y':
                pass
                #not sure about function
            #start_date = datetime.date(int(input('Rental start date (yyyy/mm/dd): ')))
            print(start_date)
            #start_date_list = create_date_list(start_date) 
            #the string inputted should be outputted as a list of ints [DD, MM, YY]
            end_date = input('Rental end date (dd/mm/yy): ')
            location = input('Location: ')
            while True:
                option = input('''\n( r ) = Return
( f ) = Finish
------------------------------------------
Type here: ''').lower()
            if option == 'r':
                if previous == 1:
                    RVK_emp(self.employee_num, self.pword).returning_customer()
                elif previous == 2:
                    RVK_emp(self.employee_num, self.pword).new_customer()
            elif option == 'f':
                pass
                #register new contract
                RVK_emp(self.employee_num, self.pword).main_menu()
            elif option == '':
                print('Please input an option')
            else:
                print('Not a valid option')




    def view_contract(self):
        while True:
            print('''
------------Contract search-------------
 ''')
            conID = input('Contract ID: #')
            if len(conID) == 4 and conID.isdigit():
                #should be able to ask the logic wrapper for the whole contract
                print('Great Success!')
                #add three options ( c ) change, ( p ) print, ( r ) return
                print('''\n( c ) Change
( p ) = Print
( r ) = Return
----------------------------------------''')
                while True:
                    option = input('Type here: ').lower()
                    if option == 'c':
                        RVK_emp(self.employee_num, self.pword).menu2_1()
                    elif option == 'p':
                        RVK_emp(self.employee_num, self.pword).menu2_2()
                    elif option == 'r':
                        RVK_emp(self.employee_num, self.pword).main_menu()
                    elif option == '':
                        print('Please input an option')
                    else:
                        print('Not a valid option')
            else:
                print('Invalid contract ID!')





    def menu2_1(self):
        'Changes contract info'
        info_list = ['Vehicle plate: ', 'Start date: ', 'End date: ']
        contract_info = [plate_num, start, end]
        print('''
------------Changing contract---------------
''')
        for i in range(len(info_list)):
            while True:
                option = input('{}{}\nchange? ( y / n ): '.format(info_list[i],contract_info[i])).lower()
                if option == 'y':
                    contract_info = input('New {}'.format(info_list[i].lower()))
                elif option == 'n':
                    pass
                elif option == '':
                    print('Please input an option')
                else:
                    print('Invalid option')   
        while True:
            print('''
 
( f ) = Finish
( c ) = Cancel
----------------------------------------''')
            option = input('Type Here: ')
            if option == 'c':
                RVK_emp(self.employee_num, self.pword).view_contract()
            elif option == 'f':
                #saves the contracts
                pass
            elif option == '':
                print('Please input an option')
            else:
                print('Invalid option')





    def menu2_2(self):
        'Prints contract'
        pass




    def menu3(self):
        #I might do it fokking later
        pass


    def print_report(self):
        while True:
            Print_format.print_title("Print bill report")
            information = "( r ) Return" 
            Print_format.print_out_format(information)

            option = input('Input contract ID: ')
            if option == "r":

            bill_dict = self.logic.get_bill_info(option)

    def add_new_employee(self):
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

( y ) = Add employee
( r ) = Return
--------------------------------------------------------------------
''')
            option = input('Type here: ').lower()
            if option == 'y':
                emp_info = [emp_name, emp_ssn, emp_address, emp_location, emp_email, emp_homephone, emp_mobilephone, emp_password]
                emp_dict = {}
                emp_dict[empID] = emp_info #Here's is where the employee is added
            elif option == 'r':
                RVK_emp(self.employee_num, self.pword).main_menu()
            elif option == '':
                print('Please input an option')
            else:
                print('Not a valid option')





    def change_employee(self):
        print('''
------------------------Change Employee------------------
''')
        info_list = ['Name: ', 'Address: ', 'Location: ', 'Email: ', 'Home telephone: ', 'Mobile phone: ', 'Password: ']
        search = input('Employee ID: ') #the output should be able to extract a list of information from the employee id
        #here should emp_info come from the data bank
        for i in range(len(emp_info)):
            if info_list[i] == 'Password:':
                hidden_password = ''
                for i in range(len(emp_info[i])):       #for each letter in the password
                    hidden_password += '*'              #an asterisk (*) is added
                print(info_list[i],hidden_password)     #and displayed
                option = input('Change? ( y / n ): ')
                if option == 'y':
                    new = input('New {}: '.format(info_list2[i]))
                    emp_info[i] = new
            else:
                print(info_list[i],emp_info[i])
                option = input('Change? ( y / n ): ')
                if option == 'y':
                    new = input('New {}: '.format(info_list2[i]))
                    emp_info[i] = new
            #return emp_info to data bank
        RVK_emp(self.employee_num, self.pword).main_menu()





    def delete_employee(self):
        print('''
------------------------Delete Employee------------------
''')
        search = input('Employee ID: ')
        #here should emp_info come from the data bank
        while True:
            delete_confirm = input('\nConfirm ( y / n )').lower()
            if delete_confirm == 'y':
                #makes the logic wrapper find it to delete
                RVK_emp(self.employee_num, self.pword).main_menu()
            elif delete_confirm == 'n':
                RVK_emp(self.employee_num, self.pword).main_menu()
            elif delete_confirm == '':
                print('Please input an option')
            else:
                print('Invalid option')




