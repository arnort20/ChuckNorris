from Model_classes.Customer import Customer
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

    def liner(self):
        print("\n"*12)

    def __init__(self, username, pword):
        self.employee_num = username
        self.pword = pword
        self.logic = Logic_API(username, pword)
        self.print = Print_format()


                                                                                #needs:
                                                                                #invalidate rental contract
                                                                                #destination management
                                                                                #destination information
                                                                                #print invoice
                                                                                #see taxes for vehicles by type
                                                                                #make report of my branch performance


                                                                                #Contract menu has create contract,view contract,print report,bill stuff
                                                                                #Employee menu has add employee,delete employee,change employee
                                                                                #vehicle menu has vehicle management and to see taxes
                                                                                # see branch review

#-------------START MENU FOR RVK EMPLOYEE---------------
    def main_menu(self):
        while True:
            self.liner()
            title = "Welcome, Employee {}".format(self.employee_num)
            self.print.print_title(title)
            self.print.print_space()

            option = "( 1 ) Contract menu,( 2 ) Employee menu,( 3 ) Branch review,( 4 ) search vehicles,,( q ) Quit"
            self.print.print_main_menu(option)
            self.print.print_line(len(title)*"")
            print()
            option = input(self.print.question('Type here'))

            if option == '1':
                self.contract_menu()
            elif option == '2':
                self.employee_menu()
            elif option == '3':
                self.branch_review()
            elif option == "4":
                self.search_vehicles()

            elif option.lower() == 'q':
                break
                #maybe go back to loginUI?
            elif option == '':
                    print('Please input an option')
            else:
                print('Not a valid option')
                self.main_menu()
    

#---------------CONTRACT MENU FOR RVK EMPLOYEE-------------
    def contract_menu(self):
        while True:
            self.liner()
            title = "Contract Menu"
            self.print.print_title(title)
            self.print.print_space()
            information = ("( 1 ) Create contract,( 2 ) View contract,( 3 ) Delete contract ,( 4 ) Print all contracts ,( 5 ) Print report ,,( r ) Return")
            self.print.print_main_menu(information)
            self.print.print_line(len(title)*"_")
            print()
            option = input(self.print.question('Type here'))
            if option == '1':
                self.customer_select()

            elif option == '2':
                self.view_contract()

            elif option == '3':
                self.delete_contract()

            elif option == '4':
                self.all_contracts()

            elif option == "5":
                self.print_report()

            elif option.lower() == 'r':
                return

            elif option == '':
                print('Please input an option')

            else:
                print('Invalid option')



#------------EMPLOYEE MENU FOR RVK EMPLOYEE-----------
    def employee_menu(self):
        while True:
            self.liner()
            title = "Employee Menu"
            self.print.print_title(title)
            self.print.print_space()
            information = ("( 1 ) Add employee,( 2 ) Change employee,( 3 ) Delete employee,( r ) Return")
            self.print.print_main_menu(information)
            self.print.print_line(len(title)*"_")
            print()
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


    def branch_review(self):
        while True:
            title = "Branch review"
            self.print.print_title(title)
            self.print.print_space()
            information = ("Choose a branch id")
            self.print.print_main_menu(information)
            self.print.print_line(len(title)*"_")

            option = input(self.print.question('Type here'))

            overview=self.Logic_API.get_destination(option)
            print(overview)



#---------choosing which kind of customer were dealing with
    def customer_select(self):
        information = ("( 1 ) Returning Customer,( 2 ) New Customer, ( r ) Return")
        title = "Creating New Contract"
        while True:
            
            #Format
            self.liner()
            self.print.short_box(information,title)
            option = input(self.print.question('Type here'))


            #choices
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



#---------If it is a returning customer--------
    def returning_customer(self): 
        wrong = 0
        title = "returning customer"
        questions = {"customer ID": "empty"}
        information = ("( c ) Cancel, ( f ) Finish")

        while True:
            for key,value in questions.items():
                self.liner()


                # printing warning
                if wrong != 0:
                    self.print.warning("wrong id")
                    wrong = 0

                #Format
                self.print.question_box(questions,information,title)
                option = input(self.print.question("Enter Choice here"))
                test = self.logic.get_customer(questions["customer ID"])
                #change answer
                try:
                    if option == 'f':
                        jim = test.id
                        self.new_contract(questions["customer ID"])
                        return
                except:
                    wrong = 1
                    continue

                #Choices
                if option == 'c':
                    return


                questions[key] = option




#------------Creating New customer---------
    def new_customer(self):

        #start info
        info_list = {'ID':"empty","customer_name":"empty","ssn":"empty",'email':"empty",'phone':"empty",'address':"empty", "license_type":"empty"}
        title = 'New Customer'
        information = ("( c ) Cancel, ( f ) Finish")
        option = 0
        wrong = 0

        while True:
            for key,value in info_list.items():
                self.liner()

                # printing warning
                if wrong == 1:
                    self.print.warning("please select option")           
                    wrong = 0

                #Format
                self.print.question_box(info_list,information,title)
                option = input(self.print.question("Enter Choice here"))

                #change answer for next print
                info_list[key] = option

                #Choices
                if option == 'c':
                    return
                elif option == 'f' and info_list["license_type"] != "empty" :
                        
                    self.logic.new_customer(info_list['ID'],info_list['customer_name'],info_list['ssn'],info_list['email'],info_list['phone'],info_list['address'],info_list['license_type'])
                    self.new_contract(info_list['ID'])
                    return
                else:
                    wrong = 1 
                    continue



#------------Creating a new contract------------
    def new_contract(self, customer_id):
        #info
        title = 'New Contract'
        customer = self.logic.get_customer(customer_id)
        #remember to rework this function, adding the fancy new functions
        #Logic_API.check_license(customer_id, vehicle_id)
        #Logic_API.check_reservations(vehicle_ID, start_date, end_date)
        print(customer)

        gbp = customer.gbp
        amount = 'good boy points: {}'.format(gbp)

        #Format
        self.liner()
        self.print.short_box(amount,title)

        use_gbp = input(self.print.question('\t\tUse Good Boy Points ( y / n )'))


        if use_gbp == 'y':
            #þarf að implementa gbp notkun
            pass



        #info for next part
        information = ("( c ) Cancel, ( f ) Finish")
        questions = {'start date (dd/mm/yy)':"empty",'end date (dd/mm/yy)':"empty",'vehicle_id':"empty",'destination_id':"empty",}
        vehicle_fail = 0
        #Contract making part
        while True:

            for key,value in questions.items():
                self.liner()
                if vehicle_fail == 1:
                    self.print.warning("customer not qualified for vehicle!")
                    vehicle_fail = 0

                #Format
                self.print.question_box(questions,information,title)
                option = input(self.print.question("\tEnter Choice here"))

                #Chaning info for next print
                questions[key] = option


                #check if customer can rent car
                if questions["vehicle_id"] != "empty":
                    can_rent = self.logic.check_license(customer_id,questions["vehicle_id"])
                    if can_rent == True:
                        pass
                    else:
                        vehicle_fail = 1
                        questions["vehicle_id"] = "empty"



                #repeats til user is happy and chooses either choice
                if option == 'c':
                    return

                elif option == 'f' and questions["destination_id"] != "empty" and  questions["vehicle_id"] != "empty" :
                    questions["start_date"],questions["end_date"] = questions['start date (dd/mm/yy)'],questions['end date (dd/mm/yy)']
                    self.logic.make_new_contract()





        # for spinning dates----------------------------------------------------------------------
        # date_list =  end_date.split("/")
        # date_list[1],date_list[3] = date_list[3],date_list[1]
        # fixed_date = "/".join(date_list)
                  


#-----------View contrarct-------------
    def view_contract(self):

        #Info
        title = "Contract Search"
        information = ("( c ) Cancel,,Insert ID below")
        options = '( c ) Change,( r ) Return'
        while True:

            #Format
            self.liner()
            self.print.short_box(information,title)
            conID = input(self.print.question("Contract ID"))  

            if conID == 'c':
                return

            contract = self.logic.get_contract(conID)

            while True:
                #Info
                title = "Contract: " + contract.id
                info = "ident,employee_id,customer_id,vehicle_id,destination_id,start_date,end_date,paid"
                second_str = str(contract)


                #Format
                self.liner()
                self.print.list_box(title,options,info,second_str)
                option = input(self.print.question('Type here: ')).lower()

                #Choices
                if option == 'c':
                    self.change_contract(contract)
                elif option == 'r':
                    return
                else:
                    print('Not a valid option')



#--------------Changing contract---------
    def change_contract(self,contract):
        #Info
        title = "Changing contract"
        information = ("( c ) Cancel, ( f ) Finish,( s ) skip")
        questions = {"start_date":contract.start_date,"end_date":contract.end_date,"vehicle_id":contract.vehicle_id}

        while True:
            for key,value in questions.items():

                #Format
                self.liner()
                self.print.question_box()
                option = input(self.print.question("\tEnter Choice here"))

                #Choices
                if option == 's':
                    continue
                if option == 'c':
                    return
                if option == "f":
                    self.logic.change_contract(contract.id,questions)
                    return
                #changing for next print
                questions[key] = option



#------------------View all contracts----------------
    def all_contracts(self):
        title = "Search vehicles"
        options = "( r ) return"
        info = "ID,employee_id,customer_id,vehicle_id,destination_id,start_date,end_date,paid?"

        contracts = self.logic.all_contracts()
        title = "Contract list"

        #Format
        self.liner()
        self.print.large_list_box(options,title,info,contracts)
        go_back = input(self.print.question("\tReturn"))
        return


#------------Delete employee--------------
    def delete_employee():
        #Info
        title = "contract search"
        information = ("( c ) Cancel,,Insert ID below")

        #Format
        self.liner()
        self.print.short_box(information,title)
        contract_id = input(self.print.question("Contract ID"))

        while True:
            #info
            title = "Deleting contract"
            information = ("( c ) Cancel,( d ) Delete")

            #Format
            self.liner()
            self.print.short_box(information,title)
            confirm = input(self.print.question("Confirm"))

            if confirm == "c":
                return
            elif confirm == "d":
                self.logic.delet(employee_id)
                return
            else:
                self.print.warning("Wrong input")
 



# Report---------------------- NOT FINISHED
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

            

#----------------Adding new employee---------------
    def add_new_employee(self):
        #Info
        title = 'New Employee'
        questions = {"name":"empty","ssn":"empty","address":"empty","location_id":"empty","email":"empty","phone":"empty","password":"empty","confirm password":"empty"}
        information = ("( c ) Cancel, ( f ) Finish")        

        while True:
            for key,value in questions.items():

                #Format
                self.liner()
                self.print.question_box(questions,information,title)
                option = input(self.print.question('Type here: '))

                #change for next print
                questions[key] = option

                #Choices
                if questions["password"] != questions["confirm password"]:
                    self.print.warning("passwords don't match")
                if option == 'c':
                    return
                elif option == 'f' and questions["confirm password"] != "empty" :
                    questions["emp_name"] = questions["name"]
                    self.logic.hire_employee(questions["emp_name"],questions["ssn"],questions["address"],questions["phone"],questions["email"],questions["password"],)



#----------------Changing employee information------------
    def change_employee(self):

        title = 'New Employee'
        while True:
            title = "employee search"
            information = ("( c ) Cancel,,Insert ID below")

            #Format
            self.liner()
            self.print.short_box(information,title)
            employee_id = input(self.print.question("employee ID"))  

            if employee_id == 'c':
                return

            #Info for next part
            employee = self.logic.get_employee(employee_id)
            information = ("( c ) Cancel, ( f ) Finish, ( s ) skip")
            questions = {"address":employee.address,"phone":employee.phone,"email":employee.email,"location":employee.location,"password":employee.password,"confirm password":employee.password} # address,phone,email,location,password

            while True:
                for key,value in questions.items():


                    #Format
                    self.liner()
                    self.print.question_box(questions,information,title)
                    option = input(self.print.question("\tEnter Choice here"))


                    #Choices
                    if option == 'c':
                        return
                    if option == 's':
                        continue
                    if questions["password"] != questions["confirm password"]:
                        self.print.warning("passwords don't match")
                    elif option == "f":
                        del questions["confirm password"]
                        self.logic.change_employee(employee_id,questions)
                        return

                    #rewrite for next print
                    questions[key] = option



#---------------Deleting/firing employee---------
    def delete_employee(self):
        #Info
        title = "employee search"
        information = ("( c ) Cancel,,Insert ID below")

        #Format
        self.liner()
        self.print.short_box(information,title)
        employee_id = input(self.print.question("employee ID"))

        while True:
            #info
            title = "Deleting employee"
            information = ("( c ) Cancel,( d ) Delete")

            #Format
            self.liner()
            self.print.short_box(information,title)
            confirm = input(self.print.question("Confirm"))

            if confirm == "c":
                return
            elif confirm == "d":
                self.logic.fire_employee(employee_id)
                return
            else:
                self.print.warning("Wrong input")



#------------search vehicles in certein location--------
    def search_vehicles(self):
        title = "Search vehicles"
        information = "( c ) Cancel,,write ID below!"
        options = "( r ) return"
        info = "ID,vehicle_name,Type,Manufacturer,Model,Color,age,tax,available,location_id,license_type"

        self.liner()
        self.print.short_box(information,title)
        location_id = input(self.print.question("location ID"))

        if location_id == "c":
            return

        vehicles = self.logic.locate_vehicles(location_id)
        title = "vehicle list"
        self.liner()
        self.print.large_list_box(options,title,info,vehicles)
        go_back = input(self.print.question("\tReturn"))
        return