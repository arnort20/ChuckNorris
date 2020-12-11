from Model_classes.Destination import Destination
from os import read
from Model_classes.Customer import Customer
from Logic_classes.Logic_API import Logic_API
from UI_classes.Print_formats import Print_format


class Rvk_ui:

    def liner(self):
        print("\n"*12)

    def __init__(self, username, pword):
        self.employee_num = username
        self.pword = pword
        self.logic = Logic_API(username, pword)
        self.print = Print_format()
        self.employee_id = username


#-------------START MENU FOR RVK EMPLOYEE---------------
    def main_menu(self):
        wrong =0
        while True:
            self.liner()

            if wrong != 0:
                self.print.warning('Not a valid option')
                wrong =0
            title = "Welcome, Employee {}".format(self.employee_num)
            self.print.print_title(title)
            self.print.print_space()

            option = "( 1 ) Contract menu,( 2 ) Employee menu,( 3 ) Destination menu,( 4 ) Vehicle menu,,( q ) Quit"
            self.print.print_main_menu(option)
            self.print.print_line(len(title)*"")
            print()
            option = input(self.print.question('Type here'))

            if option == '1':
                self.contract_menu()
            elif option == '2':
                self.employee_menu()
            elif option == '3':
                self.destination_menu()
            elif option == "4":
                self.vehicle_menu()
            elif option == '5':
                self.branch_review()
            elif option.lower() == 'q':
                break
            else:
                wrong = 1
                continue
                
    

#---------------CONTRACT MENU FOR RVK EMPLOYEE-------------
    def contract_menu(self):
        while True:
            self.liner()
            title = "Contract Menu"
            self.print.print_title(title)
            self.print.print_space()
            information = ("( 1 ) Create contract,( 2 ) View contract,( 3 ) Delete contract ,( 4 ) Print all contracts ,( 5 ) Print contract report,( 6 ) Print bill,,( r ) Return")
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

            elif option == "6":
                self.print_bill()

            elif option.lower() == 'r':
                return

            else:
                print('Invalid option')



#-----------Vehicle menu------------------------
    def vehicle_menu(self):
        while True:

            self.liner()
            title = "Vehicle Menu"

            self.print.print_title(title)
            self.print.print_space()
            information = ("( 1 ) Search vehicle by location,( 2 ) Add type,( 3 ) Change type,( 4 ) See vehicle type taxes ,,( r ) Return")
            self.print.print_main_menu(information)
            self.print.print_line(len(title)*"_")

            print()
            option = input(self.print.question('Type here'))
            if option == '1':
                self.search_vehicles()

            elif option == '2':
                self.add_type()
            elif option == '3':
                self.change_type()
            elif option == '4':
                self.vehicle_taxes()

            elif option.lower() == 'r':
                return

            else:
                print('Invalid option')



#------------Employee menu----------------------
    def employee_menu(self):
        while True:
            self.liner()
            title = "Employee Menu"
            self.print.print_title(title)
            self.print.print_space()
            information = ("( 1 ) Add employee,( 2 ) View employee,( 3 ) Delete employee,,( r ) Return")
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



#--------------Destination Menu----------
    def destination_menu(self):
        while True:
            self.liner()
            title = "Destination Menu"
            self.print.print_title(title)
            self.print.print_space()
            information = ("( 1 ) Add destination,( 2 ) Change destination,( 3 ) Delete destination,( 4 ) Look up destination,( 5 ) Destination earning reviews,,( r ) Return")
            self.print.print_main_menu(information)
            self.print.print_line(len(title)*"_")
            print()
            option = input(self.print.question('Type here'))
            if option == '1':
                self.new_destination()

            elif option == '2':
                self.change_destination()

            elif option == '3':
                self.delete_destination()

            elif option == '4':
                self.find_destination()

            elif option == "5":
                self.branch_review()

            elif option.lower() == 'r':
                return

            elif option == '':
                print('Please input an option')

            else:
                print('Invalid option')



#----------------------Branch review---------------------
    def branch_review(self):
        title = "Earnings Report"
        information = ("Date Format = (yy.mm.dd),( c ) Cancel")
        wrong = 0

        while True:
            questions = {"Input Location ID":"empty","Input Date From":"empty","Input Date To":"empty"}

            employee = self.logic.get_employee(self.employee_num)


            for key,value in questions.items():

                self.liner()
                if wrong != 0:
                    self.print.warning("invalid date input")
                    wrong = 0
                self.print.question_box(questions,information,title)
                option = input(self.print.question("Enter Input here"))

                print("")
                questions[key] = option


                if option == "c":
                    return
            try:
                money = self.logic.filter_earnings(questions["Input Location ID"],questions["Input Date From"],questions["Input Date To"])
            except:
                wrong = 1
                continue

            self.liner()
            self.print.question_box(questions,information,title)
            self.print.print_space()
            self.print.print_out_format("Money Made: " + str(money))
            self.print.print_space()
            self.print.print_line(len("Earning Report")*"_")
            go_back = input(self.print.question("return: "))
            return



#---------------------New destination--------------------
    def new_destination(self):

            info_list = {"destination_name":"empty","country_name":"empty",'airport code':"empty",'phone':"empty",'opening_hours':"empty"}
            title = 'New Destination'
            information = ("( c ) Cancel,time format: hh:mm - hh:mm, ( f ) Finish")
            option = 0
            wrong = 0

            while True:
                for key,value in info_list.items():
                    self.liner()

                    # printing warning

                    #Format
                    self.print.question_box(info_list,information,title)
                    option = input(self.print.question("Enter Choice here"))

                    #change answer for next print



                    #Choices
                    if option == 'c':
                        return
                    elif option == 'f' :
                        self.logic.new_destination(info_list['destination_name'],info_list['country_name'],info_list['airport'],info_list['phone'],info_list['opening_hours'])
                        return
                    else:
                        info_list[key] = option
                        continue



#---------------------Change Destination-----------------
    def change_destination(self):
                #Info
        title = "Destination Search"
        information = ("( r ) Return,,| Insert ID below |")
        wrong = 0
        while True:

            #Format
            self.liner()

            if wrong != 0:
                self.print.warning("Wrong Destination ID")
                wrong =0         

            self.print.short_box(information,title)
            destination_id = input(self.print.question("Destination ID")) 

            if destination_id == 'r':
                return

            try:
                destination = self.logic.get_destination(destination_id)
                destination.id
                break

            except:
                wrong = 1
                continue

        #Info
        title = "Changing Destination"
        information = ("( c ) Cancel, ( f ) Finish,( s ) skip")
        questions = {"phone":destination.phone,"opening_hours":destination.opening_hours}

        while True:
            for key,value in questions.items():

                #Format
                self.liner()
                self.print.question_box(questions,information,title)
                option = input(self.print.question("Enter input here"))

                #Choices
                if option == 's':
                    continue
                if option == 'c':
                    return
                if option == "f":
                    self.logic.change_destination(destination.id,questions)
                    return
                #changing for next print
                questions[key] = option



#---------------------Delete Destination-----------------
    def delete_destination(self):
        #Info
        wrong = 0
        title = "Destination search"
        information = ("( c ) Cancel,,Insert ID below")

        #Format
        while True:
            self.liner()
            if wrong == 1:
                self.print.warning("wrong Destination ID")
                wrong = 0
            self.print.short_box(information,title)
            destination_id = input(self.print.question("Destination ID"))
            destination = self.logic.get_destination(destination_id)

            if destination != None:
                while True:
                    #info
                    title = "Deleting Destination"
                    information = ("( c ) Cancel,Are you sure you want to delete "+destination.name+",( d ) Delete")

                    #Format
                    self.liner()
                    self.print.short_box(information,title)
                    confirm = input(self.print.question("Confirm")) 

                    if confirm == "c":
                        return
                    elif confirm == "d":
                        self.logic.delete_destination(destination_id)
                        return
                    else:
                        self.print.warning("Wrong input")
            else:
                wrong =1 
                continue



#---------------------find Destination-----------------
    def find_destination(self):
   
        #Info
        title = "Destination Search"
        information = ("( c ) Cancel,Insert ID below,")
        options = '( r ) Return'
        while True:

            #Format
            self.liner()
            self.print.short_box(information,title)
            dest_ID = input(self.print.question("Destination ID"))  

            if dest_ID == 'c':
                return

            destination = self.logic.get_destination(dest_ID)
            if destination != None:
                while True:
                    #Info
                    title = "Destination: " + destination.name
                    info = "ID,Destination_name,airport_code,Phone,opening_hours,country"
                    second_str = str(destination)


                    #Format
                    self.liner()
                    self.print.list_box(title,options,info,second_str)
                    go_back = input(self.print.question('return: ')).lower()

                    return



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
        customer_name = "customer has not been entered"
        
        ready =0

        while True:
            information = ("( c ) Cancel,"+customer_name+", ( f ) Finish")
            for key,value in questions.items():
                
                self.liner()


                # printing warning
                if wrong != 0:
                    self.print.warning("wrong id")
                    wrong = 0

                #Format
                self.print.question_box(questions,information,title)
                option = input(self.print.question("Enter input here"))

                customer = self.logic.get_customer(option)
                test = self.logic.get_customer(questions["customer ID"])
                if customer != None:
                    customer_name = customer.customer_name

                #change answer

                if option == 'f' and test != None:
                    self.new_contract(questions["customer ID"])
                    return
                elif option == 'c':
                    return
                elif option =="f" and ready == 0:
                    wrong =1

                questions[key] = option


                #Choices



                questions[key] = option



#------------Creating New customer---------
    def new_customer(self):

        #start info

        title = 'New Customer'
        information = ("( c ) Cancel, ( f ) Finish")
        info_list = {'ID':"empty","customer_name":"empty","ssn":"empty",'email':"empty",'phone':"empty",'address':"empty", "license_type":"empty"}
        option = 0
        wrong = 0

        while True:
            if wrong != 0:
                info_list = {'ID':"empty","customer_name":"empty","ssn":"empty",'email':"empty",'phone':"empty",'address':"empty", "license_type":"empty"}
            for key,value in info_list.items():
                self.liner()

                if wrong == 1:
                    self.print.warning("customer info not filled in yet")
                    print("")
                    wrong = 0


                #Format
                self.print.question_box(info_list,information,title)
                option = input(self.print.question("Enter input here"))

                #change answer for next print
                

                #Choices

                if option == 'c':
                    return
                elif option == 'f' and info_list["license_type"] != "empty" :
                    self.logic.new_customer(info_list['ID'],info_list['customer_name'],info_list['ssn'],info_list['email'],info_list['phone'],info_list['address'],info_list['license_type'])
                    self.liner()
                    item = self.logic.get_customers()
                    popped = item.pop()
                    information = popped.id + " is the new customer ID"
                    title = "new customer id"
                    self.print.short_box(information,title)
                    go_back = input(self.print.question("return"))
                    self.new_contract(info_list['ID'])
                    return


                elif option == 'f' and info_list["license_type"] == "empty" :
                    wrong =1
                    break                  
                else:
                    info_list[key] = option
                    continue

#------------Creating a new contract------------
    def new_contract(self, customer_id):
        #info
        title = 'New Contract'
        customer = self.logic.get_customer(customer_id)
        information = ("( c ) Cancel, ( f ) Finish")
        questions = {'start date (YYYY.MM.DD)':"empty",'end date (YYYY.MM.DD)':"empty",'destination_id':"empty",'vehicle_id':"empty"}
        wrong = 0
        done = 0
        vehicle_fail = 0

        #Contract making part
        while True:
            if wrong != 0:
                questions = {'start date (YYYY.MM.DD)':"empty",'end date (YYYY.MM.DD)':"empty",'destination_id':"empty",'vehicle_id':"empty"}

            for key,value in questions.items():
                self.liner()
                if vehicle_fail == 1:
                    self.print.warning("customer not qualified for vehicle!")
                    vehicle_fail = 0
                if wrong == 1:
                    self.print.warning("not all info has been filled in")

                if wrong == 2:
                    self.print.warning("Date entered wrong")
                    print("")
                    wrong = 0

                #Format
                self.print.question_box(questions,information,title)
                option = input(self.print.question("Enter Choice here"))

                #check if customer can rent car

                if questions["vehicle_id"] != "empty" and len(questions["start date (YYYY.MM.DD)"].split(".")) == 3 and questions['end date (YYYY.MM.DD)'] != "empty" :
                    try:
                        can_rent = self.logic.check_license(customer_id,questions["vehicle_id"])
                        not_taken = self.logic.check_reservations(questions["vehicle_id"],questions['start date (YYYY.MM.DD)'],questions['end date (YYYY.MM.DD)'])
                    except:
                        wrong = 2
                        break
                    if can_rent == True and not_taken == True:
                        pass
                    else:
                        vehicle_fail = 1
                        questions["vehicle_id"] = "empty"
                        break
                elif questions["vehicle_id"] != "empty" and len(questions["start date (YYYY.MM.DD)"].split(".")) != 3:
                    wrong = 2
                    break
                    
                if key == "destination_id":
                    questions[key] = option
                if option == 'c':
                    return
                elif questions["destination_id"] != "empty" and done != 1:
                    self.search_vehicles()
                    done =1
                    continue
                elif option == 'f' and questions["destination_id"] != "empty":
                    questions["start_date"],questions["end_date"] = questions['start date (YYYY.MM.DD)'],questions['end date (YYYY.MM.DD)']
                    self.logic.new_contract(customer.id,questions["vehicle_id"],questions["destination_id"],questions["start_date"],questions["end_date"])


                    self.liner()
                    item = self.logic.all_contracts()
                    popped = item.pop()
                    information = popped.id + " is the new contracts ID"
                    title = "new contract id"
                    self.print.short_box(information,title)
                    go_back = input(self.print.question("return"))


                    return
                elif option == 'f' and questions["destination_id"] == "empty" :
                    wrong =1
                    break     
                else:
                    questions[key] = option



#-----------View contrarct-------------
    def view_contract(self):

        #Info
        title = "Contract Search"
        information = ("( c ) Cancel,,Insert ID below")
        options = '( c ) Change,( r ) Return'
        wrong = 0
        while True:
            #Format
            self.liner()

            if wrong != 0:
                self.print.warning("Wrong ID")
                wrong = 0

            self.print.short_box(information,title)
            conID = input(self.print.question("Contract ID"))  

            if conID == 'c':
                return

            contract = self.logic.get_contract(conID)
            if contract != None:
                while True:
                    #Info
                    title = "Contract: " + conID
                    info = "ident,customer_id,employee_id,vehicle_id,destination_id,start_date,end_date,paid,day_made"
                    customer = self.logic.get_customer(contract.customer_id)
                    cust_name = customer.customer_name
                    employee = self.logic.get_employee(contract.employee_id)
                    emp_name = employee.employee_name
                    vehicle = self.logic.get_vehicle(contract.vehicle_id)
                    vehi_name = vehicle.vehicle_name
                    destination = self.logic.get_destination(contract.destination_id)
                    dest_name = destination.name
                    second_str = str(contract.id)+','+cust_name+','+emp_name+','+vehi_name+','+dest_name+','+str(contract.start_date)+','+str(contract.end_date)+','+str(contract.paid)+','+str(contract.day_made)
                    


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
            else:
                wrong = 1
                continue
                


#--------------Changing contract---------
    def change_contract(self,contract):
        #Info
        title = "Changing contract"
        information = ("( c ) Cancel, ( f ) Finish,( s ) skip")
        questions = {"start_date":contract.start_date,"end_date":contract.end_date,"vehicle_id":contract.vehicle_id,"paid?":contract.paid}

        while True:
            for key,value in questions.items():

                #Format
                self.liner()
                self.print.question_box(questions,information,title)
                option = input(self.print.question("Enter input here"))

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
        # Hérna kallar hann í að sjá lista yfir alla contracts sem hafa gengið í geggnum fyrirtækið.(Finished)
        # Option,info input into a format for sexy print. 
        options = "( r ) return"
        info = "ID,Signed employee,Customer,Vehicle,Destination,Start date,End date,Paid,Day made"

        contracts = self.logic.all_contracts()
        title = "Contract list"
        contract_str_list = []
        for contract in contracts:
            customer = self.logic.get_customer(contract.customer_id)
            cust_name = customer.customer_name
            employee = self.logic.get_employee(contract.employee_id)
            emp_name = employee.employee_name
            vehicle = self.logic.get_vehicle(contract.vehicle_id)
            vehi_name = vehicle.vehicle_name
            destination = self.logic.get_destination(contract.destination_id)
            dest_name = destination.name
            modified_str = str(contract.id)+','+cust_name+','+emp_name+','+vehi_name+','+dest_name+','+str(contract.start_date)+','+str(contract.end_date)+','+str(contract.paid)+','+str(contract.day_made)
            contract_str_list.append(modified_str)
        #Format
        self.liner()
        self.print.large_list_box(options,title,info,contract_str_list)
        go_back = input(self.print.question("Return"))
        return



#------------Delete contract--------------
    def delete_contract(self):
        #Info
        title = "contract search"
        information = ("( c ) Cancel,,Insert ID below")
        wrong =0 
        while True:
            #Format
            self.liner()

            if wrong != 0:
                self.print.warning("wrong contract ID!")
                wrong =0

            self.print.short_box(information,title)
            contract_id = input(self.print.question("Contract ID"))
            contract = self.logic.get_contract(contract_id)
            
            if contract != None:
                while True:
                    #info
                    title = "Deleting contract " + contract_id
                    information = ("( c ) Cancel,Are you sure you want to delete contract "+contract.id+",( d ) Delete")

                    #Format
                    self.liner()
                    self.print.short_box(information,title)
                    confirm = input(self.print.question("Confirm")) 

                    if confirm == "c":
                        return
                    elif confirm == "d":
                        self.logic.delete_contract(contract_id)
                        return
                    else:
                        self.print.warning("Wrong input")
            elif contract_id == "c":
                return
            else:
                wrong =1
                continue


#----------------View extensive contract report-------------
    def print_report(self):

        #Info
        title = "Contract Search"
        information = ("( c ) Cancel,,Insert ID below")
        options = "( r ) Return"
        wrong = 0
        while True:
            #Format
            self.liner()

            if wrong != 0:
                self.print.warning("Wrong ID")
                wrong = 0

            self.print.short_box(information,title)
            conID = input(self.print.question("Contract ID"))  

            if conID == 'c':
                return

            contract = self.logic.get_contract(conID)
            if contract != None:
                employee = self.logic.get_employee(contract.employee_id)
                customer = self.logic.get_customer(contract.customer_id)
                vehicle = self.logic.get_vehicle(contract.vehicle_id)
                
                while True:
                    

                    #Info
                    title = "Contract: " + conID 
                    info = "ident,employee_id,customer_id,vehicle_id,destination_id,start_date,end_date,paid,day_made"
                    contract_str = str(contract)
                    vehicle_str = str(vehicle)
                    customer_str = str(customer)
                    employee_str = str(employee)

                    #Format
                    self.liner()

                    self.print.print_title(title)
                    self.print.print_space()
                    self.print.print_out_format(options)
                    self.print.print_space()
                    self.print.print_line(len(title)*"_")
                    #efri
                    self.print.print_space()
                    self.print.print_out_format("contract")
                    self.print.print_space()
                    self.print.print_out_format(info)
                    self.print.print_space()
                    self.print.print_out_format(contract_str)
                    self.print.print_space()
                    self.print.print_line(len(title)*"_")
                    self.print.print_space()
                    self.print.print_out_format("employee")
                    self.print.print_space()
                    self.print.print_out_format("ID,Employee_name,ssn,Address,Phone,Email,Location")
                    self.print.print_space()
                    self.print.print_out_format(employee_str)
                    self.print.print_space()
                    self.print.print_line(len(title)*"_")
                    self.print.print_space()
                    self.print.print_out_format("customer")
                    self.print.print_space()
                    self.print.print_out_format("ID,customer_name,License_type,gbp,bbp,email,phone,address,Social_security_number")
                    self.print.print_space()
                    self.print.print_out_format(customer_str)
                    self.print.print_space()
                    self.print.print_line(len(title)*"_")
                    self.print.print_space()
                    self.print.print_out_format("vehicle")
                    self.print.print_space()
                    self.print.print_out_format("ID,vehicle_name,Type,Manufacturer,Model,Color,age,available,location_id,license_type")
                    self.print.print_space()
                    self.print.print_out_format(vehicle_str)
                    self.print.print_space()
                    self.print.print_line(len(title)*"_")
                    option = input(self.print.question('return '))
                    return
            else:
                wrong = 1
                continue

    def print_bill(self):
        
        #Info
        title = "Bill Search"
        information = ("( c ) Cancel,,Insert contract ID below")
        options = '( r ) Return'
        wrong = 0
        while True:
            #Format
            self.liner()

            if wrong == 1:
                self.print.warning("Wrong ID")
                wrong = 0
            if wrong == 2:
                self.print.warning("Bill does not exist")
                wrong = 0

            self.print.short_box(information,title)
            conID = input(self.print.question("Contract ID"))  
            contract = self.logic.get_contract(conID)


            if conID == 'c':
                return
            if contract != None:
                bill = self.logic.get_bill(conID)
                vehi = self.logic.get_vehicle(contract.vehicle_id)
                dest = self.logic.get_destination(contract.destination_id)
                cust = self.logic.get_customer(contract.customer_id)
                cust_name = cust.customer_name
                dest_name = dest.name
                vehicle_type = vehi.type
                if bill != None and contract != None:
                    while True:

                        #Info
                        title = "Bill of contract #" + conID
                        #info = "ident,employee_id,customer_id,vehicle_id,destination_id,start_date,end_date,paid"
                        info = "Contract ID,Start date,End date,Pickup date,Return date,Destination,Customer,Vehicle type,Paid,Final price"
                        second_str = (str(contract.id)+','+str(contract.start_date)+','+str(contract.end_date)+','+
                        str(bill.fetch_date)+','+str(bill.return_date)+','+str(dest_name)+','+str(cust_name)+','+
                        str(vehicle_type)+','+str(contract.paid)+','+str(bill.price))


                        #Format
                        self.liner()
                        self.print.list_box(title,options,info,second_str)
                        option = input(self.print.question('Type here: ')).lower()

                        return
                else:
                    wrong = 2
                    continue
            else:
                wrong = 1
                continue

#----------------Adding new employee---------------
    def add_new_employee(self):
        #Info
        title = 'New Employee'
        information = ("( c ) Cancel, ( f ) Finish")        
        wrong =0
        questions = {"name":"empty","ssn":"empty","address":"empty","location_id":"empty","email":"empty","phone":"empty","password":"empty","confirm password":"empty"}
        while True:
            if wrong != 0:
                questions = {"name":"empty","ssn":"empty","address":"empty","location_id":"empty","email":"empty","phone":"empty","password":"empty","confirm password":"empty"}
            for key,value in questions.items():

                #Format
                self.liner()
                if wrong == 1:
                    self.print.warning("passwords don't match")
                    wrong = 0
                elif wrong == 2:
                    self.print.warning("not all info filled in yet")
                    wrong = 0          


                self.print.question_box(questions,information,title)
                option = input(self.print.question('Type here: '))

                #change for next print
            
                #Choices
                if option == "f" and questions["password"] != questions["confirm password"]:
                    wrong = 1
                    break
                elif option == 'c':
                    return
                elif option == 'f' and questions["confirm password"] != "empty" :
                    questions["emp_name"] = questions["name"]
                    self.logic.hire_employee(questions["emp_name"],questions["ssn"],questions["address"],questions["phone"],questions["email"],questions["location_id"],questions["password"])

                    self.liner()
                    item = self.logic.get_employees()
                    popped = item.pop()
                    information = popped.id + " is the new Employee ID"
                    title = "new Employee id"
                    self.print.short_box(information,title)
                    go_back = input(self.print.question("return"))
                    return
                elif option == 'f' and questions["confirm password"] == "empty" :
                    wrong =2
                    break
                else:
                    questions[key] = option



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
                    option = input(self.print.question("Enter input here"))


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
        wrong =0
        title = "employee search"
        information = ("( c ) Cancel,,Insert ID below")
        while True:
            #Format
            self.liner()
            if wrong != 0:
                self.print.warning("Wrong employee ID")
                wrong =0
            self.print.short_box(information,title)
            employee_id = input(self.print.question("employee ID"))
            employee = self.logic.get_employee(employee_id)
            if employee != None:
                while True:
                    #info
                    title = "Deleting employee"
                    information = ("( c ) Cancel,Are you sure you want to delete "+employee.employee_name+",( d ) Delete")

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
            else:
                wrong = 1
                continue



#------------search vehicles in certein location--------

    def search_vehicles(self):
        title = "Search vehicles by location"
        information = "( c ) Cancel,,write ID below!"
        options = "( r ) return"
        info = "ID,vehicle_name,Type,Manufacturer,Model,Color,age,available,location_id,license_type"
        wrong = 0
        while True:
            self.liner()

            #for errors
            if wrong != 0:
                self.print.warning("No vehicles at location " + location_id)
                wrong = 0

            self.print.short_box(information,title)
            location_id = input(self.print.question("Destination ID"))
            vehicles = self.logic.locate_vehicles(location_id)


            if location_id == "c":
                return
            #check if any vehicles are returned for location
            if vehicles != []:
                title = "vehicle list"
                self.liner()
                self.print.large_list_box(options,title,info,vehicles)
                go_back = input(self.print.question("Return"))
                return

            else:
                wrong =1
                continue



#-----------See all vehicle type taxes-----------------

    def vehicle_taxes(self):
        self.liner()
        options = "( r ) Return"
        title = "Vehicle type taxes"
        vehicle_types = self.logic.get_vehicle_types()
        information = "Type_name,Destination,Rate"
        type_list = []
        
        for vtype in vehicle_types:
            if vtype["destination_id"] == '0':
                destination_name = 'All'
            else:
                destination = self.logic.get_destination(vtype["destination_id"])
                destination_name = destination.name

            the_type = [str(vtype["name"]),str(destination_name),str(vtype["rate"])]
            str_the_type = ','.join(the_type)
            type_list.append(str_the_type)
        self.print.large_list_box(options,title,information,type_list)
        go_back = input(self.print.question("return"))



#----------------Add vehicle type-----------------------
    def add_type(self):
        
            questions = {"name":"empty","destination_id":"empty","rate":"empty"}
            title = 'New Type'
            information = ("( c ) Cancel, ( f ) Finish")
            option = 0
            wrong = 0

            while True:
                for key,value in questions.items():
                    self.liner()

                    # printing warning

                    #Format
                    self.print.question_box(questions,information,title)
                    option = input(self.print.question("Enter input here"))

                    #change answer for next print


                    #Choices
                    if option == 'c':
                        return
                    elif option == 'f' :
                        self.logic.make_new_type(questions['name'],questions['destination_id'],questions['rate'])
                        return
                    else:
                        questions[key] = option
                        continue



#------------------Change vehicle type-------------------
    def change_type(self):
        title = "type Search"
        information = ("( c ) Cancel,,| Insert ID below |")
        wrong = 0
        while True:

            #Format


            questions = {"type_name":"empty","destination_id":"empty"}
            for key,value in questions.items():
                self.liner()
                if wrong != 0:
                    self.print.warning("Wrong Destination ID")
                    wrong =0         
                self.print.question_box(questions,information,title)
                option = input(self.print.question("Enter input here"))
                questions[key] = option
            
                if option == 'c':
                    return

            destination_id = questions["destination_id"]
            name = questions["type_name"]
            try:
                
                rate = self.logic.get_vehicle_tax(name,destination_id)
                destination = self.logic.get_destination(destination_id)
                print(rate)
                break

            except:
                wrong = 1
                continue

        #Info
        title = "Changing type " + name +" in "+ destination.name
        information = ("( c ) Cancel, ( f ) Finish,( s ) skip")
        questions = {"rate":rate}

        while True:
            for key,value in questions.items():

                #Format
                self.liner()
                self.print.question_box(questions,information,title)
                option = input(self.print.question("Enter input here"))

                #Choices
                if option == 's':
                    continue
                if option == 'c':
                    return
                if option == "f":
                    self.logic.change_type(name,destination_id,questions)
                    return
                #changing for next print
                questions[key] = option