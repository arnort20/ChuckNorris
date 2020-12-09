from Logic_classes.logic_API import Logic_API as lAPI

api = lAPI("1","1")

contracts = api.all_contracts()
for i in range(20,25):
    for j in contracts:
        if j.id == str(i):  
            api.new_bill(j.id,j.start_date,j.end_date,False)