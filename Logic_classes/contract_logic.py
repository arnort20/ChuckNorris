#from Data_classes.DataAPI import DataAPI
from Data_classes.DataAPI import DataAPI as dAPI

class Contract:
    def __init__(self):
        self.dAPI = dAPI()
    def getContract(self, contractID):
        return self.dAPI.get_contract(contractID)