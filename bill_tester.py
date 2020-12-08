from Logic_classes.logic_wrapper import LogicAPI as lAPI

api = lAPI("1","1")
bill_dict = api.get_bill_info("2")
print(bill_dict)
print(bill_dict["start_date"])
print(bill_dict["end_date"])
print(bill_dict["contract_period"])
total_cost = api.calculate_bill(bill_dict)
print(total_cost)