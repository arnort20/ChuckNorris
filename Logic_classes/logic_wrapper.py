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

    #vehicle stuff
    def get_vehicle(self, vehicleID):
        self.vehicle_wrapper()
        return self.contract.get_vehicle(vehicleID)
    def make_new_vehicle(self,vehicle_name,Type,Model,Color,age,tax):
        self.vehicle_wrapper()
        self.vehicle.create_new_vehicle(vehicle_name,Type,Model,Color,age,tax)
    def return_vehicle(self,vehicleID):
        self.vehicle_wrapper()
        self.vehicle.return_vehicle(vehicleID)
        #returns True if it succeeds, otherwise false
    def reserve_vehicle(self, vehicleID):
        self.vehicle_wrapper()
        self.vehicle.reserve_vehicle(vehicleID)
        #returns True if it succeeds, otherwise false
    def change_information(self, vehicleID):
        pass

    #customer stuff

    #employee stuff

    #destination stuff