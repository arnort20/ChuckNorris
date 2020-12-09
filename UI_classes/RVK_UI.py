from Logic_classes.logic_API import Logic_API
from UI_classes.Print_formats import Print_format

"""
3
As Chuck Norris and/or employee of NaN Air I need to be able to 
register new employees, a list of their information, and their position
(check)

4
As an employee of NaN Air I need to be able to put together a rental 
contract (check)

5
As an employee of NaN Air I need to be able to find an employees 
information and edit it (check)

6
As an employee of NaN Air I need to be able to register new vehicles 
into a list of all vehicles

7
As an employee of NaN Air I need to be able to list all vehicles according 
to location and availability

8
As an employee of NaN Air I need to be able to list all vehicles according to 
location and damage status

10
As an employee of NaN Air I need to be able to register and list all rental 
contracts

12
As an employee of NaN Air I need to be able to change the loan time and 
vehicle of the rental contract (CHECK)

13
As an employee of NaN Air I need to be able to invalidate a rental contract

14
As an employee of NaN Air I need to be able to register new destinations and 
list all of them

15
As an employee of NaN Air I need to be able to print an invoice based on the 
information on the rental contract

16
As an employee of NaN Air I need to be able to see and edit how high the taxes 
are for each type of vehicle and add taxes to new types of vehicles

17
As an employee of NaN Air I need to be able to see if the customer has the 
credentials to use certain types of vehicles (CHECK)

18
As an employee of NaN Air I need to make sure that the customer's charges are 
collected so that he will not get charged multiple times (CHECK)

19
As an employee of NaN Air I need to be able to make a report of my branch's 
performance
"""

class Rvk_ui:
    def __init__(self, username, pword):
        self.employee_num = username
        self.pword = pword
        self.logic = Logic_API(username, pword)
        self.print = Print_format()

    def main_menu(self):
        while True:
            title = "Welcome, Employee {}".format(self.employee_num)
            self.print.print_title(title)
            self.print.print_space()
            option = "( 1 ) Create new contract,( 2 ) View contract,( 3 ) Print report,( 4 ) Add new employee,( 5 ) Change employee,( 6 ) Delete employee,,( q )  Quit "
            self.print.print_main_menu(option)
            self.print.print_line(len(title)*"")
            option = input(self.print.question('Type here'))
            if option == '1':
                self.create_contract()
            elif option == '2':
                self.view_contract()
            elif option == '3':
                self.print_report()
            elif option == '4':
                self.add_new_employee()
            elif option == '5':
                self.change_employee()
            elif option == '6':
                self.delete_employee()
            #needs:
            #vehicle management stuff
            #search vehicles
            #view all contracts
            #invalidate rental contract
            #destination management
            #destination information
            #print invoice
            #see taxes for vehicles by type
            #make report of my branch performance
            elif option.lower() == 'q':
                break
                #maybe go back to loginUI?
            elif option == '':
                    print('Please input an option')
            else:
                print('Not a valid option')
                self.main_menu()
    




    def create_contract(self):
        while True:
            title = "Creating New Contract"
            self.print.print_title(title)
            self.print.print_space()
            information = ("( 1 ) Returning Customer,( 2 ) New Customer, ( r ) Return")
            self.print.print_out_format(information)
            self.print.print_line(len(title)*"_")

            option = input(self.print.question('Type here'))
            if option == '1':
                self.returning_customer()

            elif option == '2':
                self.new_customer()

            elif option.lower() == 'r':
                return

            elif option == '':
                print('Please input an option')

            else:
                print('Invalid option')




    def returning_customer(self): 
        self.print.print_title("Returning Customer")
        information = ("( c ) Cancel, ( f ) Finish")
        cost_reg = input('Costumer ID: ')
        while True:
            self.print.print_out_format(information)
            option = input('Type here: ').lower()
            if option == 'c':
                self.create_contract()
            elif option == 'f':
                #finds the costumer and creates a new contract
                self.menu1_3(1)
            elif option == '':
                print('Please input an option')
            else:
                print('Invalid option')




    def new_customer(self):


        cust_info = []
        info_list = {'ID':"empty","customer_name":"empty",'email':"empty",'phone':"empty",'address':"empty", "license_type":"empty"}
        title = 'New Customer'
        option = 0

        while True:
            for key,value in info_list.items():
                self.liner()
                information = ("( c ) Cancel, ( f ) Finish")
                self.print.print_title(title)
                #efri gluggi
                self.print.print_space()
                self.print.print_out_format(information)
                self.print.print_space()
                self.print.print_line(len(title)*"_")

                #nedri
                self.print.print_space()
                self.print.print_questions(info_list)
                self.print.print_space()
                self.print.print_line(len(title)*"_")

                option = input(self.print.question("Enter Choice here"))
                info_list[key] = option

                if option == 'c':
                    return
                elif option == 'f' and info_list["license_type"] != "empty" :
                        
                    self.logic.new_customer(info_list['ID'],info_list['customer_name'],info_list['email'],info_list['phone'],info_list['address'],info_list['license_type'])
                    self.menu1_3(2)
                    return
                else:
                    self.print.warning("please select option")
        return



    def menu1_3(self, previous):
        #previous says from what menu you came from
        title = 'New Contract'
        if previous == 1:
            pass #get gbp
        else:
            gbp = 0

        self.liner()
        self.print.print_title(title)
        self.print.print_space()
        self.print.print_out_format('good boy points: {}'.format(gbp))
        self.print.print_line(len(title)*"_")

        
        use_gbp = input(self.print.question('Use Good Boy Points ( y / n )'))

        if use_gbp == 'y':
            #þarf að implementa gbp notkun
            pass



        questions = {'start date (dd/mm/yy)':"empty",'end date (dd/mm/yy)':"empty",'location':"empty"}

        for key,value in questions.items():
            self.liner()
            self.print.print_title(title)
            self.print.print_space()    
            self.print.print_questions(questions)
            self.print.print_line(len(title)*"_")
            option = input(self.print.question("Enter Choice here"))
            questions[key] = option
            

        # for spinning dates----------------------------------------------------------------------
        # date_list =  end_date.split("/")
        # date_list[1],date_list[3] = date_list[3],date_list[1]
        # fixed_date = "/".join(date_list)
                  
        while True:
            option = input('''\n( r ) = Return

( f ) = Finish
------------------------------------------
Type here: ''').lower()
            if option == 'r':
                if previous == 1:
                    self.returning_customer()
                elif previous == 2:
                    self.new_customer()
            elif option == 'f':
                pass
                #register new contract
                self.main_menu()
            elif option == '':
                print('Please input an option')
            else:
                print('Not a valid option')




    def view_contract(self):
        information = '( c ) Change,( p ) = Print,( r ) = Return'
        while True:
            self.print.print_title('Contract Search')
            conID = input('Contract ID: #')
            contract = self.logic.get_contract(conID)
            if contract:
                print('Great Success!')
                #add three options ( c ) change, ( p ) print, ( r ) return
                self.print.print_out_format(information)
                while True:
                    option = input('Type here: ').lower()
                    if option == 'c':
                        self.menu2_1(contract)
                    elif option == 'p':
                        self.menu2_2(contract)
                    elif option == 'r':
                        self.main_menu()
                    elif option == '':                        
                        print('Please input an option')
                    else:
                        print('Not a valid option')
            else:
                print('Invalid contract ID')





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
                self.view_contract()
            elif option == 'f':
                #saves the contracts
                pass
            elif option == '':
                print('Please input an option')
            else:
                print('Invalid option')





    def menu2_2(self):
        'Prints contract'
        while True:
            print('''
------------Contract search-------------
 ''')
            conID = input('Contract ID: #')
            if len(conID) == 4 and conID.isdigit():
                contract = Logic_API.get_contract(conID)
                print(contract)
            else:
                print('Invalid contract ID!')

    def print_report(self):
        self.print.print_title("Print bill")
        information = "( # ) Input the contract ID,( r ) Return" 
        self.print.print_main_menu(information)
        self.print.print_line()
        option = input(self.print.question('Input contract ID: '))
        if option == "r":
            return
        bill_dict = self.logic.get_bill_info(option)
        relevant_dict = {}
        relevant_dict["start"] = bill_dict["start_date"]
        relevant_dict["end"] = bill_dict["end_date"]
        relevant_dict["Pickup date"] = bill_dict["fetch_date"]
        relevant_dict["Return date"] = bill_dict["return_date"]
        relevant_dict["Vehicle tax"] = bill_dict["tax"]
        relevant_dict["Returned late?"] = bill_dict["late_tax"]
        true_period = bill_dict["true_period"]
        contract_period = bill_dict["contract_period"]
        if relevant_dict["Returned late?"]:
            relevant_dict["days"] = true_period
        else:
            relevant_dict["days"] = contract_period
        relevant_dict["gbp_used"] = bill_dict["gbp_discount"]
        relevant_dict["Total price"] = self.logic.calculate_bill(bill_dict)
        self.print.print_title("Bill for contract #{}".format(option))
        self.print.print_questions(relevant_dict)
        self.print.print_line()


    # def print_report(self):
    #     while True:
    #         self.print.print_title("Print bill report")
    #         information = "( # ) Input the contract ID associated with the bill, ( r ) Return" 
    #         self.print.print_main_menu(information)

    #         option = input('Input contract ID: ')
    #         if option == "r":
    #             break

    #         bill_dict = self.logic.get_bill_info(option)
            
    #         self.print.print_questions(bill_dict)
    #         self.print.print_line()
            
    def liner(self):
        print("\n"*12)

    def add_new_employee(self):
        self.print.print_title('New Employee')
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
                self.main_menu()
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
        self.main_menu()





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
                self.main_menu()
            elif delete_confirm == 'n':
                self.main_menu()
            elif delete_confirm == '':
                print('Please input an option')
            else:
                print('Invalid option')




