from .vehicle_logic import 
from .contract_logic import Contract as contLogic


class LogicAPI:
    def __init__(self):
        self.contract = contLogic()
    def getContract(self, contractID):
        return self.contract.getContract(contractID)
