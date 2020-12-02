from Data_classes.DataAPI import DataAPI
api = DataAPI()
contracts = api.get_contracts()
for obj in contracts:
    print(obj)



# #from Data_classes.DataAPI import DataAPI
# from Logic_classes.logic_wrapper import LogicAPI as lAPI
# api = lAPI()
# #print(api.get_contracts())
# print(api.getContract("123"))