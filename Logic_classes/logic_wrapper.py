from vehicle_logic import *
from contract_logic import *
import customer_logic
import destination_logic
import employee_logic

class LogicAPI:
    def __init__(self):
        contract = contract_logic.Contract()
    def getContract(contractID):
        return contract_logic.getContract(contractID)



