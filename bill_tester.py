from Logic_classes.logic_API import Logic_API as lAPI

api = lAPI("1","1")
price = api.finish_contract("2","2021.1.10","2021.1.26",True)
print(price)