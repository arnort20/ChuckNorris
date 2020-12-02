from .vehicle_logic import Vehicle as vehi_logic
from .contract_logic import Contract as cont_logic
from .employee_logic import Employee as emp_logic
from .destination_logic import Destination as dest_logic
from .customer_logic import Customer as cust_logic
class LogicAPI:
    #def __init__(self):
        #self.contract = cont_logic()
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

    #contract stuff
    def get_contract(self, contractID):
        self.contract_wrapper()
        return self.contract.getContract(contractID)
    #remember to add a function for calculating penalties and price

    #vehicle stuff
    def get_vehicle(self, vehicleID):
        self.vehicle_wrapper()
        return self.contract.get_vehicle(vehicleID)
    def make_new_vehicle(self,vehicle_name,Type,Model,Color,age,tax):
        self.vehicle_wrapper()
        self.vehicle.create_new_vehicle(vehicle_name,Type,Model,Color,age,tax)
    def return_vehicle(self,vehicleID,gbp,bbp,customerID):
        self.vehicle_wrapper()
        self.vehicle.return_vehicle(vehicleID)
        self.end_of_contract_update_customer(customerID,gbp,bbp)
        #returns True if it succeeds, otherwise false
    def reserve_vehicle(self, vehicleID):
        self.vehicle_wrapper()
        self.vehicle.reserve_vehicle(vehicleID)
        #returns True if it succeeds, otherwise false
    def change_information(self, vehicleID):
        pass

    #customer stuff
    def new_customer(self,customerID,name,license_type):
        self.customer_wrapper()
        self.customer.new_customer(customerID,name,license_type)
    def get_customer(self,customerID):
        self.customer_wrapper()
        self.customer.get_customer(customerID)
    def end_of_contract_update_customer(self,customerID,gbp,bbp):
        #part of return_vehicle
        self.customer_wrapper()
        self.customer.add_GBP(customerID,gbp)
        self.customer.add_BBP(customerID,bbp)
    def change_name(self,customerID,new_name):
        self.customer_wrapper()
        self.customer.change_name(customerID,new_name)
    def change_license_type(self,customerID,new_license):
        self.customer_wrapper()
        self.customer.change_license_type(customerID,new_license)
    def kill_customer(self,customerID):
        self.customer_wrapper()
        self.customer.kill_customer(customerID)

    #employee stuff
    def hire_employee(self,emp_name,ssn,address,phone,email,location):
        self.employee_wrapper()
        self.employee.hire(emp_name,ssn,address,phone,email,location)
    
    #destination stuff