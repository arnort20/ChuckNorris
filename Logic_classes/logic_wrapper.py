#from vehicle_logic import *
#from contract_logic import Conrtact as contLogic
#from Data_classes.Logic_classes.contract_logic import Contract as contLogic
from .contract_logic import Contract as contLogic
#import customer_logic
#import destination_logic
#import employee_logic

class LogicAPI:
    def __init__(self):
        self.contract = contLogic()
    def getContract(self, contractID):
        return self.contract.getContract(contractID)
