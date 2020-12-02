from .vehicle_logic import Vehicle as vehi_logic
from .contract_logic import Contract as cont_logic
from .employee_logic import Employee as emp_logic
from .destination_logic import Destination as dest_logic
from .customer_logic import Customer as cust_logic
class LogicAPI:
    def __init__(self):
        self.contract = cont_logic()
    def get_contract(self, contractID):
        return self.contract.getContract(contractID)
