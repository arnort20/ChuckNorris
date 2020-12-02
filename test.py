from Logic_classes.logic_wrapper import LogicAPI as lAPI
api = lAPI()
contract = api.get_contract("123")
print(contract)
print(api.get_contracts())
