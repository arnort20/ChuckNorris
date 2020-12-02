from Data_classes.DataAPI import DataAPI as dAPI

class Contract:
    def __init__(self):
        self.dAPI = dAPI()
    def get_contract(self, contractID):
        return self.dAPI.get_contract(contractID)