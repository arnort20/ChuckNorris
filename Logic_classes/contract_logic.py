try:
#    from Data_classes.DataAPI import *
    import Data_classes.DataAPI
except:
    print("bad")
api = Data_classes.DataAPI
contract = api.get_contract(123)
print(contract)