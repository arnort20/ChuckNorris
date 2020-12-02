from Data_classes.DataAPI import DataAPI as dAPI

class Customer:
    def __init__(self):
        self.api = dAPI()
    def get_customer(self,customerID):
        pass
    def get_customer_txt(self,customerID):
        pass
    def new_customer(self,customerID,name,license_type):
        dAPI.make_customer(customerID,name,license_type,0,0)
    def add_GBP(self,customerID,added_points):
        #make changes
        pass
    def add_BBP(self,customerID,added_points):
        #make changes
        pass
    def change_name(self,customerID,new_name):
        #make changes
        pass
    def change_license_type(self,customerID,new_license):
        #make changes
        pass
    def kill_customer(self,customerID):
        #removes the customer from the database
        pass
    