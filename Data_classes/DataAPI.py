


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
    contract = get_certein(ID,"Data_files\Contracts.csv")
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
    contracts = get_csv("Data_files\Contracts.csv")
    return contracts

def get_employees():
    Employees = get_csv("Data files\Employees.csv")




#make id
def vehicles_makeID():
    pass
def get_customerID():
    pass
def get_destinationID():
    pass
def get_contractID():
    pass
def get_employeeID():
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

print(get_contracts())
print()
print(get_contract("123"))

