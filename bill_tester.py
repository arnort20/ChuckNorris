from Logic_classes.logic_wrapper import LogicAPI as lAPI

api = lAPI("1","1")
bill_dict = api.get_bill_info("2")
print(bill_dict)