from .vehicle_logic import Vehicle as vehi_logic
from .contract_logic import Contract as cont_logic
from .employee_logic import Employee as emp_logic
from .destination_logic import Destination as dest_logic
from .customer_logic import Customer as cust_logic

class LogicAPI:
    def __init__(self, userID, pword):
        self.user = userID
        priv_location = self.login_user(userID, pword)
        if priv_location:
            return priv_location
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


    #login stuff
    def login_user(self, user_ID, user_pwrd):
        #if username and password are correct:
        #   returns a value for what privileges the user has
        #else:
        #   returns none
        user = self.get_employee(user_ID)
        correct_pword = user.password
        if correct_pword == user_pwrd:
            return user.location
        else:
            return None
    

    #make the contract:
    #vehicles_ID must be a list of IDs (if multiple) comma seperated with no whitespace
    def make_new_contract(self, customer_ID, vehicles_ID, start_date, end_date):
        employee = self.get_employee(self.user)
        customer = self.get_customer(customer_ID)
        vehicles = vehicles_ID.split(',')
        #get all the vehicles and put em in a list of objects
        signed_vehicles = []
        for vehicleID in vehicles:
            Vehicle = self.get_vehicle(vehicleID)
            signed_vehicles.append(vehi)
        #check if the customer has the appropriate licensing
        for vehicle in signed_vehicles:
            if not self.check_license(customer_ID, vehicle.id):
                return "license_error"
        #customer has the appropriate license for all vehicles, reserve them all
        #for vehicle in signed_vehicles:
            #self.reserve_vehicle(vehicle.id, start_date, end_date)
            #remember to create reservation function
        self.new_contract(self.user, customer_ID, vehicles_ID, start_date, end_date)
        return "success"

    #when the customer picks up the vehicles:
    #for all the cars:
    #   available = False

    #when returning the vehicle/s
    def return_vehicles(self, contractID, date_returned):
        Contract = self.get_contract(contractID)
        end_date = Contract.end_date
        # (function that checks if the date returned is later 
        # than the contract's end date goes here)
        #apply BBP to customer if True
        vehicles = Contract.vehicle_ID
        for vehicle in vehicles:
            self.return_vehicle(vehicle.id)

    def return_vehicle(self,vehicleID):
        pass
        #returns True if it succeeds, otherwise false
        
    def use_GBP(self, customer_ID):
        Customer = self.get_customer(customer_ID)
        gbp = Customer.gbp
        discount = int(gbp)*100
        
        

    #contract stuff
    def get_contract(self, contractID):
        self.contract_wrapper()
        return self.contract.getContract(contractID)

    def delete_contract(self,contractID):
        self.contract_wrapper()
        self.contract.delete_current_contract(contractID)
        #returns false if failed, remember to implement

    def new_contract(self,employeeID,customerID,vehicleID,start_date,end_date):
        self.contract_wrapper()
        self.contract.make_contract(employeeID,customerID,vehicleID,start_date,end_date)
    #remember to add a function for calculating penalties and price
    def change_contract(self,contractID,change_value):
        self.contract_wrapper()
        self.contract.change_contract(contractID, change_value)

    def all_contracts(self):
        self.contract_wrapper()
        self.contract.all_contracts()
    #So chuck can get a list of all current contracts





    #vehicle stuff
    def get_vehicle(self, vehicleID):
        self.vehicle_wrapper()
        return self.vehicle.get_vehicle(vehicleID)

    def make_new_vehicle(self,vehicle_name,Type,manufacturer,Model,Color,age,tax,location):
        self.vehicle_wrapper()
        self.vehicle.create_new_vehicle(vehicle_name,Type,manufacturer,Model,Color,age,tax,location)



    def reserve_vehicle(self, vehicleID):
        self.vehicle_wrapper()
        self.vehicle.reserve_vehicle(vehicleID)
        #returns True if it succeeds, otherwise false

    def change_information(self, vehicleID, change_dict):
        self.vehicle_wrapper()
        self.vehicle.change_details(vehicleID, change_dict)

    def kill_vehicle(self, vehicle_ID):
        self.vehicle_wrapper()
        self.vehicle.kill_vehicle(vehicle_ID)

    def check_license(self, customerID, vehicleID):
        self.vehicle_wrapper()
        return self.vehicle.check_license(customerID,vehicleID)
        




    #customer stuff
    def new_customer(self,customerID,name,email,phone,address,license_type):
        self.customer_wrapper()
        self.customer.new_customer(customerID,name,email,phone,address,license_type)

    def get_customer(self,customerID):
        self.customer_wrapper()
        return self.customer.get_customer(customerID)

    # def end_of_contract_update_customer(self,customerID,gbp,bbp):
    #     #part of return_vehicle
    #     self.customer_wrapper()
    #     self.customer.add_GBP(customerID,gbp)
    #     self.customer.add_BBP(customerID,bbp)

    # def change_name(self,customerID,new_name):
    #     self.customer_wrapper()
    #     self.customer.change_name(customerID,new_name)

    # def change_license_type(self,customerID,new_license):
    #     self.customer_wrapper()
    #     self.customer.change_license_type(customerID,new_license)

    def change_customer(self, customer_ID, changes_dict):
        self.customer_wrapper()
        self.customer.change_customer(customer_ID, changes_dict)


    def kill_customer(self,customerID):
        self.customer_wrapper()
        self.customer.kill_customer(customerID)





    #employee stuff
    def hire_employee(self,emp_name,ssn,address,phone,email,location):
        self.employee_wrapper()
        self.employee.hire(emp_name,ssn,address,phone,email,location)

    def fire_employee(self,emp_ID):
        self.employee_wrapper()
        self.employee.fire(emp_ID)

    def change_employee(self, emp_ID, change_dict):
        self.employee_wrapper()
        self.employee.change_employee(emp_ID, change_dict)

    def get_employee(self,emp_ID):
        self.employee_wrapper()
        self.employee.get_employee(emp_ID)

    #destination stuff

