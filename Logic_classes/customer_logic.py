from Data_classes.DataAPI import DataAPI as dAPI

class Customer_logic:
    def __init__(self):
        self.dAPI = dAPI()
        
    def get_customer(self,customerID):
        #returns a customer object containing all info 
        return self.dAPI.get_customer(customerID)

    def new_customer(self,customerID,name,email,phone,address,license_type):
        #registers a new customer, their ID will be their driver's license number
        #
        self.dAPI.add_customer(customerID,name,email,phone,address,license_type,0,0)

    def add_GBP(self,customerID,added_points):
        self.dAPI.add_points(customerID,added_points)

    def add_BBP(self,customerID,added_points):
        self.dAPI.add_points(customerID,added_points)

    def change_name(self,customerID,new_name):
        self.dAPI.change_Customer(customerID, new_name)

        #make changes
    def change_license_type(self,customerID,new_license):
        self.dAPI.add_license(customerID, new_license)
        #make changes

    def kill_customer(self,customerID):
        try:
            self.dAPI.delete_customer(customerID)
        except ValueError:
            return False
        #removes the customer from the database