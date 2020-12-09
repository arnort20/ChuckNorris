from Logic_classes.logic_API import Logic_API as lAPI

api = lAPI("1","1")
bills = api.get_bills()
for bill in bills:
    print(bill)