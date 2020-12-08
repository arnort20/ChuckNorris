from Data_classes.DataAPI import DataAPI as dAPI

class Vehicle_logic:
    def __init__(self):
        self.dAPI = dAPI()

    def get_vehicle_txt(self,vehicleID):
        #text form of vehicle object
        pass
    
    def get_vehicle(self,vehicleID):
        return self.dAPI.get_vehicle(vehicleID)

    def get_vehicles(self):
        return self.dAPI.get_vehicles()

    # def reserve_vehicle(self,vehicleID):
    #     #change available = False
    #     #if available == False:
    #         #return an error message and do nothing
    #     pass

    # def return_vehicle(self, vehicleID):
    #     #change available = True
    #     #if available == True:
    #         #return an error message and do nothing
    #     pass

    def create_new_vehicle(self,vehicle_name,Type,Manufacturer,Model,Color,age,tax,available,location,license_type):
        vehicleID = self.dAPI.vehicles_makeID()
        self.dAPI.add_vehicle(vehicleID,vehicle_name,Type,Manufacturer,Model,Color,age,tax,available,location,license_type)

    def change_details(self, vehicleID, change_dict):
        self.dAPI.change_vehicle(vehicleID, change_dict)

    def kill_vehicle(self,vehicleID):
        dAPI.delete_vehicle(vehicleID)

    def check_license(self, customerID, vehicleID):
        vehicle = self.dAPI.get_vehicle(vehicleID)
        customer = self.dAPI.get_customer(customerID)
        requirements = vehicle.license_type
        cust_license = customer.License_type.split('.')
        if requirements in cust_license:
            return True

