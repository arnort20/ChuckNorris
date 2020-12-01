


import csv
from get_io import *

# skila objectum til logic
# skila listum af objectum til logic
# taka a moti objectum fra io closum


# get single
def get_vehicle(ID):
    vehicle = get_certein(ID,"Data files\Vehicles.csv")
    
def get_Customer(ID):
    customer = get_certein(ID,"Data files\Customers.csv")

def get_Destination(ID):
    Destination = get_certein(ID,"Data files\Destinations.csv")

def get_Contract(ID):
    contract = get_certein(ID,"Data files\Contracts.csv")

def get_Employee(ID):
    Employee = get_certein(ID,"Data files\Employees.csv")




# get multiple

def get_vehicles():
    vehicles = get_csv("Data files\Vehicles.csv")

def get_Customers():
    Customers = get_csv("Data files\Customers.csv")

def get_Destinations():
    Destinations = get_csv("Data files\Destinations.csv")

def get_Contracts():
    Contracts = get_csv("Data files\Contracts.csv")
    print(Contracts)

def get_Employees():
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
def delete_Customer():
    pass
def delete_Destination():
    pass
def delete_Contract():
    pass
def delete_Employee():
    pass




#add single
def add_vehicle():
    pass
def add_Customer():
    pass
def add_Destination():
    pass
def add_Contract():
    pass
def add_Employee():
    pass



def main():
    get_Contracts()
    get_Contract(123)