from Logic_classes.Logic_API import Logic_API
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
            self.liner()
            title = "Welcome, Employee {}".format(self.employee_num)
            self.print.print_title(title)
            self.print.print_space()
            option = "( 1 ) Contract menu,( 2 ) Employee menu,( 3 ) Vehicle menu,( 4 ) Branch review,( q ) Quit"

            #Contract menu has create contract,view contract,print report,bill stuff
            #Employee menu has add employee,delete employee,change employee
            #vehicle menu has vehicle management and to see taxes
            # see branch review

            self.print.print_main_menu(option)

            self.print.print_line(len(title)*"")
            option = input(self.print.question('Type here'))
            if option == '1':
                self.contract_menu()
            elif option == '2':
                self.employee_menu()
            elif option == '3':
                self.vehicle_menu()
            elif option == '4':
                self.branch_review()
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
    


    def contract_menu(self):
        while True:
            self.liner()
            title = "Contract Menu"
            self.print.print_title(title)
            self.print.print_space()
            information = ("( 1 ) Create contract,( 2 ) View contract,( 3 ) Print report ,( r ) Return")
            self.print.print_main_menu(information)
            self.print.print_line(len(title)*"_")

            option = input(self.print.question('Type here'))
            if option == '1':
                self.create_contract()

            elif option == '2':
                self.view_contract()

            elif option == '3':
                self.print_report()

            elif option.lower() == 'r':
                return

            elif option == '':
                print('Please input an option')

            else:
                print('Invalid option')

        
    def employee_menu(self):
        while True:
            title = "Employee Menu"
            self.print.print_title(title)
            self.print.print_space()
            information = ("( 1 ) Add employee,( 2 ) Change employee,( 3 ) Delete employee,( r ) Return")
            self.print.print_main_menu(information)
            self.print.print_line(len(title)*"_")

            option = input(self.print.question('Type here'))
            if option == '1':
                self.add_new_employee()

            elif option == '2':
                self.change_employee()

            elif option == '3':
                self.delete_employee()

            elif option.lower() == 'r':
                return

            elif option == '':
                print('Please input an option')

            else:
                print('Invalid option')

    def vehicle_menu(self):
        while True:
            title = "Vehicle menu"
            self.print.print_title(title)
            self.print.print_space()
            information = ("( 1 ) Search vehicle,( 2 ) Vehicle tax,( r ) Return")
            self.print.print_main_menu(information)
            self.print.print_line(len(title)*"_")

            option = input(self.print.question('Type here'))
            if option == '1':
                self.search_vehicle()

            elif option == '2':
                self.vehicle_tax()

            elif option.lower() == 'r':
                return

            elif option == '':
                print('Please input an option')

            else:
                print('Invalid option')

    def branch_review(self):
        while True:
            title = "Branch review"
            self.print.print_title(title)
            self.print.print_space()
            information = ("Choose a branch id")
            self.print.print_main_menu(information)
            self.print.print_line(len(title)*"_")

            option = input(self.print.question('Type here'))

            self.Logic_API.get_destination(option)




    # Contract-----------------
    #eftir ad breyta nafni
    def create_contract(self):
        while True:
            title = "Creating New Contract"
            self.liner()
            self.print.print_title(title)
            self.print.print_space()
            information = ("( 1 ) Returning Customer,( 2 ) New Customer, ( r ) Return")
            self.print.print_main_menu(information)
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
        title = "returning customer"
        questions = {"customer ID": "empty"}
        information = ("( c ) Cancel, ( f ) Finish")

        while True:
            for key,value in questions.items():

                self.liner()
                self.print.print_title(title)
                #efri gluggi
                self.print.print_space()
                self.print.print_out_format(information)
                self.print.print_space()
                self.print.print_line(len(title)*"_")

                #nedri
                self.print.print_space()
                self.print.print_questions(questions)
                self.print.print_space()
                self.print.print_line(len(title)*"_")

                option = input(self.print.question("Enter Choice here"))
                questions[key] = option

                if option == 'c':
                    return
                elif option == 'f' and questions["customer ID"] != "empty" :
                    self.new_contract(questions["customer ID"])

                    return
                    
                else:
                    self.print.warning("please select option")




    def new_customer(self):


        cust_info = []
        info_list = {'ID':"empty","customer_name":"empty","ssn":"empty",'email':"empty",'phone':"empty",'address':"empty", "license_type":"empty"}
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
                        
                    self.logic.new_customer(info_list['ID'],info_list['customer_name'],info_list['ssn'],info_list['email'],info_list['phone'],info_list['address'],info_list['license_type'])
                    self.new_contract(info_list['ID'])
                    return
                else:
                    self.print.warning("please select option")


    # Contract-----------------
    def new_contract(self, customer_id):
        #previous says from what menu you came from
        title = 'New Contract'
        customer = self.logic.get_customer(customer_id)
        print(customer)

        gbp = customer.gbp


        self.liner()


        self.print.print_title(title)
        self.print.print_space()
        self.print.print_out_format('good boy points: {}'.format(gbp))
        self.print.print_line(len(title)*"_")

        
        use_gbp = input(self.print.question('\t\tUse Good Boy Points ( y / n )'))

        if use_gbp == 'y':
            #þarf að implementa gbp notkun
            pass



        questions = {'start date (dd/mm/yy)':"empty",'end date (dd/mm/yy)':"empty",'vehicle_id':"empty",'destination_id':"empty",}
        while True:
            for key,value in questions.items():
                self.liner()
                information = ("( c ) Cancel, ( f ) Finish")
                self.print.print_title(title)
                #efri gluggi
                self.print.print_space()
                self.print.print_out_format(information)
                self.print.print_space()
                self.print.print_line(len(title)*"_")


                self.print.print_space()    
                self.print.print_questions(questions)
                self.print.print_line(len(title)*"_")
                option = input(self.print.question("\tEnter Choice here"))
                questions[key] = option
                
                if option == 'c':
                    return

                elif option == 'f' and questions["destination_id"] != "empty" :
                    questions["start_date"],questions["end_date"] = questions['start date (dd/mm/yy)'],questions['end date (dd/mm/yy)']
                    self.logic.make_new_contract()



        # for spinning dates----------------------------------------------------------------------
        # date_list =  end_date.split("/")
        # date_list[1],date_list[3] = date_list[3],date_list[1]
        # fixed_date = "/".join(date_list)
                  



    # Contract-----------------
    def view_contract(self):
        while True:
            title = "Contract Search"
            information = ("( c ) Cancel,,")
            options = '( c ) Change,( r ) Return'

            self.liner()
            self.print.print_title(title)
            self.print.print_space()
            self.print.print_out_format(information)
            self.print.print_space()
            self.print.print_line(len(title)*"_")
            conID = input(self.print.question("Contract ID"))  

            if conID == 'c':
                return

            contract = self.logic.get_contract(conID)

            while True:
                title = "Contract: " + contract.id
                self.liner()
                self.print.print_title(title)
                self.print.print_space()
                self.print.print_out_format(options)
                self.print.print_space()
                self.print.print_line(len(title)*"_")
                #efri
                self.print.print_space()
                self.print.print_out_format("ident,employee_id,customer_id,vehicle_id,destination_id,start_date,end_date,paid")
                self.print.print_space()
                self.print.print_out_format(str(contract))
                self.print.print_space()
                self.print.print_line(len(title)*"_")

                option = input(self.print.question('Type here: ')).lower()
                if option == 'c':
                    self.change_contract(contract)
                elif option == 'r':
                    return
                else:
                    print('Not a valid option')




    # Contract-----------------
    def change_contract(self,contract):
        title = "Changing contract"
        information = ("( c ) Cancel, ( f ) Finish")


        questions = {"start_date":contract.start_date,"end_date":contract.end_date,"vehicle_id":contract.vehicle_id}
        while True:
            for key,value in questions.items():
                self.liner()
                self.print.print_title(title)
                self.print.print_space()

                self.print.print_out_format(information)
                self.print.print_space()
                self.print.print_line(len(title)*"_")


                self.print.print_space()    
                self.print.print_questions(questions)
                self.print.print_line(len(title)*"_")
                option = input(self.print.question("\tEnter Choice here"))

                if option == 's':
                    continue
                else:
                    questions[key] = option
                    
                if option == 'c':
                    return

                if option == "f":
                    self.logic.change_contract(contract.id,questions)
                    return




    # Report----------------------
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

            
    def liner(self):
        print("\n"*12)

    def add_new_employee(self):
        title = 'New Employee'
        questions = {"name":"empty","ssn":"empty","address":"empty","location_id":"empty","email":"empty","phone":"empty","password":"empty","confirm password":"empty"}
        information = ("( c ) Cancel, ( f ) Finish")        

        while True:
            for key,value in questions.items():
                self.liner()
                self.print.print_title(title)
                self.print.print_space()
                self.print.print_out_format(information)
                self.print.print_space()
                self.print.print_line(len(title)*"_")
                #efri
                self.print.print_space()
                self.print.print_space()
                self.print.print_questions(questions)
                self.print.print_space()
                self.print.print_line(len(title)*"_")
                option = input(self.print.question('Type here: '))

                questions[key] = option

                if questions["password"] != questions["confirm password"]:
                    self.print.warning("passwords don't match")

                if option == 'c':
                    return
                elif option == 'f' and questions["confirm password"] != "empty" :
                    questions["emp_name"] = questions["name"]
                    self.logic.hire_employee(questions["emp_name"],questions["ssn"],questions["address"],questions["phone"],questions["email"],questions["password"],)

                else:
                    print('Not a valid option')




    def change_employee(self):

        title = 'New Employee'

        questions = ()

        while True:
            title = "employee search"
            information = ("( c ) Cancel,,")

            self.liner()
            self.print.print_title(title)
            self.print.print_space()
            self.print.print_out_format(information)
            self.print.print_space()
            self.print.print_line(len(title)*"_")
            employee_id = input(self.print.question("employee ID"))  

            if employee_id == 'c':
                return

            employee = self.logic.get_employee(employee_id)
            information = ("( c ) Cancel, ( f ) Finish, ( s ) skip")
            questions = {"address":employee.address,"phone":employee.phone,"email":employee.email,"location":employee.location,"password":employee.password,"confirm password":employee.password} # address,phone,email,location,password

            while True:
                for key,value in questions.items():
                    self.liner()
                    self.print.print_title(title)
                    self.print.print_space()

                    self.print.print_out_format(information)
                    self.print.print_space()
                    self.print.print_line(len(title)*"_")


                    self.print.print_space()    
                    self.print.print_questions(questions)
                    self.print.print_line(len(title)*"_")
                    option = input(self.print.question("\tEnter Choice here"))

                    if option == 'c':
                        return

                    if option == 's':
                        continue

                    questions[key] = option

                    if questions["password"] != questions["confirm password"]:
                        self.print.warning("passwords don't match")
                    elif option == "f":
                        del questions["confirm password"]
                        self.logic.change_employee(employee_id,questions)
                        return

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




