from Data_classes.DataAPI import DataAPI
api = DataAPI
contract = api.get_contract("123")
print(contract)
print(api.get_contracts())