from Data_classes.DataAPI import DataAPI as dAPI

class Customer:
    def __init__(self):
        self.api = dAPI()
    def get_customer(self,customerID):
        return self.dAPI.bring_customer(customerID)
    def new_customer(self,customerID,name,license_type):
        dAPI.make_customer(customerID,name,license_type,0,0)
    def add_GBP(self,customerID,added_points):
        return self.dAPI.add_points(customerID,added_points)
    def add_BBP(self,customerID,added_points):
        return self.dAPI.add_points(customerID,added_points)
    def change_name(self,customerID,new_name):
        return self.dAPI.add_new_name(customerID, new_name)
        #make changes
    def change_license_type(self,customerID,new_license):
        return self.dAPI.add_new_license(customerID, new_license)
        #make changes
    def kill_customer(self,customerID):
        try:
            self.dAPI.delete_customer(customerID)
        except ValueError:
            return False
        #removes the customer from the database

    