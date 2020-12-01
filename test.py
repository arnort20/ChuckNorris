from Data_classes.wait.Contracts_io import get_contract
from Data_classes.DataAPI import DataAPI
api = DataAPI
contract = api.get_contract("123")
print(contract)
print(get_contract())