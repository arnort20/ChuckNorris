from Data_classes.DataAPI import *
api = DataAPI()
contract = api.get_contract("123")
print(contract)
print(api.get_contracts())