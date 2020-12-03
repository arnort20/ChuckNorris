#from Data_classes.DataAPI import DataAPI
from Data_classes.DataAPI import DataAPI as dAPI

class Contract:
    def __init__(self):
        self.dAPI = dAPI()
    def get_contract(self, contractID):
        return self.dAPI.bring_contract(contractID)
    def change_contract(self, contractID, change_value):
        dAPI.change_Contract(contractID, change_value)

        #sends contractID and dict with value for change to the data layer
        
    def delete_current_contract(self, contractID):
        try:
            self.dAPI.delete_contract(contractID)
        except ValueError:
            return False
            #skilar False þegar contractID er ekki til í data

    def make_contract(self, employeeID,customerID,vehicleID,start_date,end_date):
        contract_name = self.dAPI.get_name(customerID)
        contract_phone = self.dAPI.get_phone(customerID)
        contract_address = self.dAPI.get_address(customerID)
        contract_email = self.dAPI.get_email(customerID)
        contractID = self.dAPI.contract_makeID()
        self.dAPI.add_contract(contractID, contract_name, contract_phone, contract_address, contract_email, vehicleID, start_date, end_date)

    def all_contracts(self):
        return self.dAPI.get_all_contracts()


    