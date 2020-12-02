from Data_classes.DataAPI import DataAPI

class Contract:
    def __init__(self):
        self.dAPI = DataAPI.DataAPI()
    def getContract(self, contractID):
        return self.dAPI.get_contract(contractID)