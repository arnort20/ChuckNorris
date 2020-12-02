
import csv
from Data_classes.get_io import Getter
from Model_classes import *

# skila objectum til logic
# skila listum af objectum til logic
# taka a moti objectum fra io closum

class DataAPI(object):
    # get single
    def __init__(self):
        self.get = Getter

    def get_vehicle(self,ident):
        vehicle = self.get.get_certein(ident,"Data files\Vehicles.csv")
        return vehicle

    def get_customer(self,ident):
        customer = self.get.get_certein(ident,"Data files\Customers.csv")
        return customer

    def get_destination(self,ident):
        Destination = self.get.get_certein(ident,"Data files\Destinations.csv")
        return Destination

    def get_contract(self,ident):
        contract = self.get.get_certein(ident,"Data_files\Contracts.csv")
        return contract

    def get_employee(self,ident):
        Employee = self.get.get_certein(ident,"Data files\Employees.csv")
        return Employee


    # get multiple
    def get_vehicles(self):
        vehicles = self.get.get_csv("Data files\Vehicles.csv")
        return vehicles
    def get_customers(self):
        customers = self.get.get_csv("Data files\Customers.csv")
        return customers
    def get_destinations(self):
        destinations = self.get.get_csv("Data files\Destinations.csv")
        return destinations
    def get_contracts(self):
        contracts = self.get.get_csv("Data_files\Contracts.csv")
        return contracts

    def get_employees(self):
        employees = self.get.get_csv("Data files\Employees.csv")
        return employees

    #make,ident
    def vehicles_makeID():
        pass
    def get_customer_makeID():
        pass
    def get_destination_makeID():
        pass
    def get_contract_makeID():
        pass
    def get_employee_makeID():
        pass


    # change single
    def change_vehicle():
        pass
    def change_Customer():
        pass
    def change_Destination():
        pass
    def change_Contract():
        pass
    def change_Employee():
        pass


    #delete single
    def delete_vehicle():
        pass
    def delete_customer():
        pass
    def delete_destination():
        pass
    def delete_contract():
        pass
    def delete_employee():
        pass


    #add single
    def add_vehicle(ID,vehicle_name,Type,Manufacturer,Model,Color,mileage,age,tax,available):
        pass
    def add_customer(ID,Customer_name,License_type,GBP,BBP):
        pass
    def add_destination(ID,Destination_name,Phone,opening_hours,reportfilename):
        pass
    def add_contract(ID,employee_id,costumer_id,vehicle_id,start_date,end_date,paid):
        pass
    def add_employee(ID,Employee_name,SSN,Address,Phone,Email,Location):
        pass