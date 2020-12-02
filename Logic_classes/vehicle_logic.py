from Data_classes.DataAPI import DataAPI as dAPI

class Vehicle:
    def __init__(self):
        self.dAPI = dAPI()
    def get_vehicle_txt(self,vehicleID):
        pass
    def get_vehicle(self,vehicleID):
        pass
    def reserve_vehicle(self,vehicleID):
        pass
    def create_new_vehicle(self,vehicle_name,Type,Manufacturer,Model,Color,mileage,age,tax,available):
        vehicleID = self.dAPI.vehicle_makeID()
        