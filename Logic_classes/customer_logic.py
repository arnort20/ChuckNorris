from Data_classes.DataAPI import DataAPI as dAPI

class Customer_logic:
    def __init__(self):
        self.dAPI = dAPI()
        
    def get_customer(self,customerID):
        #returns a customer object containing all info 
        return self.dAPI.get_customer(customerID)

    def new_customer(self,customerID,name,email,ssn,phone,address,license_type):
        #registers a new customer, their ID will be their driver's license number
        #if the customer is a company, the employee is expected to have checked what the highest ID for a company is
        #might add a function to automate this
        self.dAPI.add_customer(customerID,name,email,ssn,phone,address,license_type,0,0)

    def change_customer(self, customer_ID, change_dict):
        #change the customer based on what keys to change and the new values for each key
        self.dAPI.change_Customer(customer_ID, change_dict)

    def kill_customer(self,customerID):
        #removes the customer from the database
        self.dAPI.delete_customer(customerID)
        
    def get_all_customers(self):
        return self.dAPI.get_customers()
        