#from vehicle_logic import *
from contract_logic import Conrtact as contLogic
#import customer_logic
#import destination_logic
#import employee_logic

class LogicAPI:
    def __init__(self):
        self.contract = contLogic.Contract()
    def getContract(self, contractID):
        return self.contract.getContract(contractID)
