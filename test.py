from Data_classes.DataAPI import DataAPI
api = DataAPI()
# apid = api.vehicles_makeID() 
# contracts = api.add_vehicle(apid,"jojo","jingle","jambajuice","akakaka","blue","25","20","yes")


print(api.get_contracts())
print(api.get_contract("1"))

# det = api.get_customer("12")
# print(det)