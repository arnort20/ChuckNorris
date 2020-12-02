from .vehicle_logic import 
from .contract_logic import Contract as contLogic


class LogicAPI:
    def __init__(self):
        self.contract = contLogic()
    def get_contract(self, contractID):
        return self.contract.getContract(contractID)
