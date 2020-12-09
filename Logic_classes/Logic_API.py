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
    def make_new_contract(self, customer_ID, vehicle_ID, start_date, end_date):

        Vehicle = self.get_vehicle(vehicle_ID)
        #check if the customer has the appropriate licensing
        if not self.check_license(customer_ID, Vehicle.id):
            return "license_error"
        #customer has the appropriate license for the vehicle, check reservations
        reservations = self.check_reservations(vehicle_ID)

        self.new_contract(self.user, customer_ID, vehicle_ID, start_date, end_date)
        return "success"

    def get_contract(self, contractID):
        self.contract_wrapper()
        return self.contract.get_contract(contractID)

    def delete_contract(self,contractID):
        self.contract_wrapper()
        self.contract.delete_current_contract(contractID)
        #returns false if failed, remember to implement

    def new_contract(self,customerID,vehicleID,location,start_date,end_date):
        self.contract_wrapper()
        employeeID = self.user
        self.contract.make_contract(employeeID,customerID,vehicleID,location,start_date,end_date)
    
    def change_contract(self,contractID,change_value):
        self.contract_wrapper()
        self.contract.change_contract(contractID, change_value)

    def all_contracts(self):
        self.contract_wrapper()
        return self.contract.all_contracts()
    #So chuck can get a list of all current contracts





    #vehicle stuff
    def get_vehicle(self, vehicleID):
        self.vehicle_wrapper()
        return self.vehicle.get_vehicle(vehicleID)

    def make_new_vehicle(self,vehicle_name,Type,manufacturer,Model,Color,age,tax,available,location,license_type):
        self.vehicle_wrapper()
        self.vehicle.create_new_vehicle(vehicle_name,Type,manufacturer,Model,Color,age,tax,available,location,license_type)

    def check_reservations(self, vehicle_ID, start_date, end_date):
        """
        checks all contracts to see which dates the vehicle is reserved, if any
        returns a list of tuples as (start_date, end_date)
        then checks if there are any dates that clash with the inputted dates
        returns a bool
        """
        self.contract_wrapper()
        reserved_dates = self.contract.check_vehicle_reservations(vehicle_ID)
        

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
        




    #customer stuff
    def new_customer(self,customerID,name,ssn,email,phone,address,license_type):
        self.customer_wrapper()
        self.customer.new_customer(customerID,name,ssn,email,phone,address,license_type)

    def get_customer(self,customerID):
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
        self.employee_wrapper()
        return self.employee.get_employee(emp_ID)


    #destination stuff
    def new_destination(self, destination_name, airport, phone, opening_hours):
        self.destination_wrapper()
        self.destination.new_destination(destination_name, airport, phone, opening_hours)

    def get_destination(self, dest_ID):
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
        self.bill_wrapper()
        self.bill.new_bill(contractID, fetch_date, return_date, gbp_used)

    def get_bill_info(self, contractID):
        self.bill_wrapper()
        return self.bill.get_bill_info(contractID)

    def calculate_bill(self, bill_dict):
        self.bill_wrapper()
        return self.bill.calculate_price(bill_dict)

    def get_bills(self):
        self.bill_wrapper()
        return self.bill.get_all_bills()

    def get_bill(self, contract_ID):
        self.bill_wrapper()
        return self.bill.get_bill(contract_ID)
    
    #when the customer returns the vehicle, magic happens
    
    def filter_earings(self, location_ID, date_from, date_to):
        self.bill_wrapper()
        return self.bill.filter_earnings(location_ID,date_from,date_to)
    
        
