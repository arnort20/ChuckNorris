from Logic_classes.logic_API import Logic_API as lAPI

api = lAPI("1","1")
bills = api.filter_earings("6","2020.10.1","2020.11.30")
print(bills)