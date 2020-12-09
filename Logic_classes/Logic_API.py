from Logic_classes.vehicle_logic import Vehicle_logic as vehi_logic
from Logic_classes.contract_logic import Contract_logic as cont_logic
from Logic_classes.employee_logic import Employee_logic as emp_logic
from Logic_classes.destination_logic import Destination_logic as dest_logic
from Logic_classes.customer_logic import Customer_logic as cust_logic
from Logic_classes.bill_logic import Bill_logic as bill_logic
import datetime

class Logic_API:
    def __init__(self, userID, pword):
        self.user = userID
        self.priv_location = self.login_user(userID, pword)

    def login_user(self, user_ID, user_pwrd):
        """
        if username and password are correct:
           returns a value for what privileges the user has
        else:
           returns none
        """
        user = self.get_employee(user_ID)
        correct_pword = user.password
        if correct_pword == user_pwrd:
            return user.location
        else:
            return None

    def contract_wrapper(self):
        self.contract = cont_logic()

    def vehicle_wrapper(self):
        self.vehicle = vehi_logic()

    def customer_wrapper(self):
        self.customer = cust_logic()

    def employee_wrapper(self):
        self.employee = emp_logic()

    def destination_wrapper(self):
        self.destination = dest_logic()  

    def bill_wrapper(self):
        self.bill = bill_logic()


    #contract stuff
    def get_contract(self, contractID):
        #returns an object containing information about the contract
        self.contract_wrapper()
        return self.contract.get_contract(contractID)

    def delete_contract(self,contractID):
        self.contract_wrapper()
        self.contract.delete_current_contract(contractID)

    def new_contract(self,customerID,vehicleID,location,start_date,end_date):
        #registers the user and the employee signed on the contract
        #registers the contract to the database
        self.contract_wrapper()
        employeeID = self.user
        self.contract.make_contract(employeeID,customerID,vehicleID,location,start_date,end_date)
    
    def change_contract(self,contractID,change_dict):
        #change the contract with a dictionary containing the keys 
        #you want to change and what values to replace them with
        self.contract_wrapper()
        self.contract.change_contract(contractID, change_dict)

    def all_contracts(self):
        # get a list of all contracts
        self.contract_wrapper()
        return self.contract.all_contracts()
    





    #vehicle stuff
    def get_vehicle(self, vehicleID):
        #returns an object containing information about the vehicle
        self.vehicle_wrapper()
        return self.vehicle.get_vehicle(vehicleID)

    def make_new_vehicle(self,vehicle_name,Type,manufacturer,Model,Color,age,tax,available,location,license_type):
        self.vehicle_wrapper()
        self.vehicle.create_new_vehicle(vehicle_name,Type,manufacturer,Model,Color,age,tax,available,location,license_type)

    def check_reservations(self, vehicle_ID, start_date, end_date):
        """
        checks all contracts to see which dates the vehicle is reserved, if any
        then checks if there are any dates that clash with the inputted dates
        returns True if the vehicle is not reserved for that particular span
        of dates, returns false is it's reserved
        """
        self.contract_wrapper()
        min_date = self.convert_date(start_date)
        max_date = self.convert_date(end_date)
        reserved_dates = self.contract.check_vehicle_reservations(vehicle_ID)
        for dates in reserved_dates:
            starts_at = self.convert_date(dates[0])
            ends_at = self.convert_date(dates[1])
            if self.check_date_clash(min_date, max_date, starts_at, ends_at):
                return False
        return True

    def change_vehicle_info(self, vehicleID, change_dict):
        self.vehicle_wrapper()
        self.vehicle.change_details(vehicleID, change_dict)

    def kill_vehicle(self, vehicle_ID):
        self.vehicle_wrapper()
        self.vehicle.kill_vehicle(vehicle_ID)

    def check_license(self, customerID, vehicleID):
        self.vehicle_wrapper()
        return self.vehicle.check_license(customerID,vehicleID)

    def get_vehicle_reports(self):
        self.vehicle_wrapper()
        return self.vehicle.get_vehicles()

    def popular_vehicle_types(self):
        pass





    #customer stuff
    def new_customer(self,customerID,name,ssn,email,phone,address,license_type):
        self.customer_wrapper()
        self.customer.new_customer(customerID,name,ssn,email,phone,address,license_type)

    def get_customer(self,customerID):
        #returns an object containing information about the customer
        self.customer_wrapper()
        return self.customer.get_customer(customerID)

    def change_customer(self, customer_ID, changes_dict):
        self.customer_wrapper()
        self.customer.change_customer(customer_ID, changes_dict)

    def kill_customer(self,customerID):
        self.customer_wrapper()
        self.customer.kill_customer(customerID)





    #employee stuff
    def hire_employee(self,emp_name,ssn,address,phone,email,location, password):
        self.employee_wrapper()
        self.employee.hire(emp_name,ssn,address,phone,email,location, password)

    def fire_employee(self,emp_ID):
        self.employee_wrapper()
        self.employee.fire(emp_ID)

    def change_employee(self, emp_ID, change_dict):
        self.employee_wrapper()
        self.employee.change_employee(emp_ID, change_dict)

    def get_employee(self,emp_ID):
        #returns an object containing information about the employee
        self.employee_wrapper()
        return self.employee.get_employee(emp_ID)


    #destination stuff
    def new_destination(self, destination_name, airport, phone, opening_hours):
        self.destination_wrapper()
        self.destination.new_destination(destination_name, airport, phone, opening_hours)

    def get_destination(self, dest_ID):
        #returns an object containing information about the destination
        self.destination_wrapper()
        return self.destination.get_destination(dest_ID)

    def get_all_destinations(self):
        self.destination_wrapper()
        return self.destination.get_all_destinations

    def change_destination(self, dest_ID, change_dict):
        self.destination_wrapper()
        self.destination.change_destination(dest_ID, change_dict)


    #billing stuff
    
    def finish_contract(self, contractID, fetch_date, return_date, gbp_used):
        #when the customer returns the vehicle, magic happens
        #input the contract, date when car was picked up,
        #date when car was returned, and whether the customer wants to use
        #their loyalty points(Good Boy Points)
        self.bill_wrapper()
        self.bill.new_bill(contractID, fetch_date, return_date, gbp_used)

    def calculate_bill(self, tax, gbp_discount, days, late_tax):
        #a handy dandy calculator, used automatically within the bill logic file
        self.bill_wrapper()
        return self.bill.calculate_price(tax, gbp_discount, days, late_tax)

    def get_bills(self):
        #get all the bill objects in the database
        self.bill_wrapper()
        return self.bill.get_all_bills()

    def get_bill(self, contract_ID):
        #get one bill object, bill IDs are always the same as 
        #the bill they're associated with
        self.bill_wrapper()
        return self.bill.get_bill(contract_ID)
    
    def filter_earnings(self, location_ID, date_from, date_to):
        #how much money did this place make me last month?
        #                      -Chuck Norris, probably
        self.bill_wrapper()
        return self.bill.filter_earnings(location_ID,date_from,date_to)



    #extra functions

    def convert_date(self, date_string):
        #for datetime module calculations
        year, month, day = str(date_string).split('.')
        date_format = datetime.date(int(year), int(month), int(day))
        return date_format

    def check_date_clash(self, date1_start, date1_end, date2_start, date2_end):
        """
        takes four datetime objects and checks if there's any overlap
        to check if one day is in a span of time, insert date1_start = date1_end
        returns true if there is a clash
        """
        if ((date2_start > date1_start and date2_start < date1_end)or(date2_end > date1_start and date2_end < date1_end)):
            return True
        elif ((date1_start > date2_start and date1_start < date2_end)or(date1_end > date2_start and date1_end < date2_end)):
            return True
        else:
            return False
    
    def check_privilege(self):
        """
        0: no privileges, access denied
        1: master access of Chuck Norris
        2: A Reykjavík employee, has contract making privileges
        3: Destination employee, has car management privileges
        """
        if not self.priv_location:
            return 0
        elif self.priv_location >= "3":
            return 3
        else:
            return self.priv_location
