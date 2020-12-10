from Data_classes.DataAPI import DataAPI as dAPI

class Vehicle_logic:
    def __init__(self):
        self.dAPI = dAPI()
    
    def get_vehicle(self,vehicleID):
        #returns an object containing information about the vehicle
        return self.dAPI.get_vehicle(vehicleID)

    def get_vehicles(self):
        #returns a list of all vehicles in the database as objects
        return self.dAPI.get_vehicles()

    def create_new_vehicle(self,vehicle_name,Type,Manufacturer,Model,Color,age,tax,available,location,license_type):
        #adds a new car to the database, the ID is automatically generated
        vehicleID = self.dAPI.vehicles_makeID()
        self.dAPI.add_vehicle(vehicleID,vehicle_name,Type,Manufacturer,Model,Color,age,tax,available,location,license_type)

    def change_details(self, vehicleID, change_dict):
        #change the vehicle with a dictionary containing the keys 
        #you want to change and what values to replace them with
        self.dAPI.change_vehicle(vehicleID, change_dict)

    def kill_vehicle(self,vehicleID):
        #roundhouses the vehicle out of the database
        dAPI.delete_vehicle(vehicleID)

    def check_license(self, customerID, vehicleID):
        #check if the customer has the necessary licensing for the vehicle
        #OK = no license required
        vehicle = self.dAPI.get_vehicle(vehicleID)
        customer = self.dAPI.get_customer(customerID)
        requirements = vehicle.license_type
        cust_license = customer.License_type.split('.')
        if requirements in cust_license:
            return True
        elif requirements == "OK":
            return True
        else:
            return False

    def vehicle_taxes(self):
        type_dict = {}
        vehicles = self.dAPI.get_vehicles()
        for vehicle in vehicles:
            type_dict[vehicle.type] = str(vehicle.tax)+"%"
        return type_dict
