#from Data_classes.DataAPI import DataAPI
from Data_classes.DataAPI import DataAPI as dAPI

class Contract_logic:
    def __init__(self):
        self.dAPI = dAPI()

    def get_contract(self, contractID):
        #get a contract object, containing all information regarding a contract
        contract = self.dAPI.get_contract(contractID)
        return contract
        
    def change_contract(self, contractID, change_value):
        #sends contractID and dict with value for change to the data layer
        self.dAPI.change_Contract(contractID, change_value)
        
    def delete_current_contract(self, contractID):
        #for when a contract gets invalidated
        self.dAPI.delete_contract(contractID)

    def make_contract(self, employeeID,customerID,vehicleID,location,start_date,end_date):
        #makes the contract, all contracts are unpaid by deafault
        #all contract IDs are automatically generated to make sure there's no contracts that share the same ID
        contractID = self.dAPI.contract_makeID()
        paid = "no"
        self.dAPI.add_contract(contractID, employeeID, customerID, vehicleID, location, start_date, end_date,paid)

    def all_contracts(self):
        #get all the contracts as objects
        return self.dAPI.get_contracts()

    def check_vehicle_reservations(self, vehicle_ID):
        """
        #a function to see at what times the vehicle is reserved
        #returns a list of tuples containing two strings
        #returns None if there's no reservations for that car
        #used by the logic wrapper in check_reservations
        """
        all_contracts = self.all_contracts()
        vehicle_contracts = []
        for cont in all_contracts:
            if vehicle_ID == cont.vehicle_id:
                vehicle_contracts.append(cont)
        if vehicle_contracts:
            dates_reserved = []
            for reservation in vehicle_contracts:
                dates = (reservation.start_date, reservation.end_date)
                dates_reserved.append(dates)
            return dates_reserved
        else:
            return None