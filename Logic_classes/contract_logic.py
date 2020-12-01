try:
    from Data_classesrt.DataAPI import *
except:
    print("bad")

contract = DataAPI.get_contract(123)
print(contract)