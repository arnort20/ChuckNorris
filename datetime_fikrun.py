import datetime
from Logic_classes.logic_wrapper import LogicAPI as lAPI
api = lAPI("1","1")


cont = api.get_contract("2")


# sasasoola = api.get_vehicle("7")
# year,month,day = sasasoola.age.split(',')
# sas_age = datetime.datetime(int(year),int(month),int(day))
# print(sas_age)
# first = datetime.datetime(2021,11,10)
# print(first - sas_age)

# curr = datetime.datetime.now()
# req_format = datetime.date(2020,11,10)
# #(curr, "%Y/%m/%d %H/%M/%S")
# print(req_format)