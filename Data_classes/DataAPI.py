


import csv
from get_io import *

# skila objectum til logic
# skila listum af objectum til logic
# taka a moti objectum fra io closum


# get single
def get_vehicle(ID):
    vehicle = get_certein(ID,"Data files\Vehicles.csv")
    return vehicle
def get_customer(ID):
    customer = get_certein(ID,"Data files\Customers.csv")
    return customer
def get_destination(ID):
    Destination = get_certein(ID,"Data files\Destinations.csv")
    return Destination
def get_contract(ID):
    contract = get_certein(ID,"Data files\Contracts.csv")
    return contract
def get_employee(ID):
    Employee = get_certein(ID,"Data files\Employees.csv")
    return Employee



# get multiple

def get_vehicles():
    vehicles = get_csv("Data files\Vehicles.csv")

def get_customers():
    Customers = get_csv("Data files\Customers.csv")

def get_destinations():
    Destinations = get_csv("Data files\Destinations.csv")

def get_contracts():
    Contracts = get_csv("Data files\Contracts.csv")
    return contracts

def get_employees():
    Employees = get_csv("Data files\Employees.csv")




#make id
def vehicles_makeID():
    pass
def get_CustomerID():
    pass
def get_DestinationID():
    pass
def get_ContractID():
    pass
def get_EmployeeID():
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
def add_vehicle():
    pass
def add_customer():
    pass
def add_destination():
    pass
def add_contract():
    pass
def add_employee():
    pass

