from Data_classes.DataAPI import DataAPI
api = DataAPI()

api.change_vehicle("7",{"vehicle_name": "ssalamander"})

# apid = api.vehicles_makeID() 
# api.add_vehicle(apid,"jojo","jingle","jambajuice","akakaka","blue","25","20","yes","12","12")

# for item in api.get_contracts():
#     print(item)



# print(api.get_vehicles())
# print(api.get_contract("1"))

# api.delete_vehicle("1")
# for item in range(1,len(api.get_vehicles())+1):
#      api.delete_vehicle(str(item))
# det = api.get_customer("1")