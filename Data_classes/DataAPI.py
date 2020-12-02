
import csv
from Data_classes.get_io import Getter
from Model_classes.Contract import Contract
from Model_classes.Customer import Customer
from Model_classes.Destination import Destination
from Model_classes.Employee import Employee
from Model_classes.Vehicle import Vehicle

# skila objectum til logic
# skila listum af objectum til logic
# taka a moti objectum fra io closum

class DataAPI(object):
    def __init__(self):
        self.get = Getter

    #make stuff
    def make_vehicle(ride):

        return Vehicle(ride["ID"],ride["Vehicle name"],ride["Type"],ride["Manufacturer"],ride["Model"],ride["Color"],ride["age"],ride["tax"],ride["available"])

    def make_customer(info):
  
        return Customer(info["ID"],info["Customer name"],info["License type"],info["GBP"],info["BBP"])

    def make_destination(info):
        
        return Destination(info["ID"],info["Destination name"],info["Phone"],info["opening hours"],info["report filename"])

    def make_contract(info):
     
        return Contract(info["contract ID"],info["employee ID"],info["customer ID"],info["vehicle ID"],info["start date"],info["end date"],info["paid?"])

    def make_employee(info):

        return Employee(info["ID"],info["Employee name"],info["SSN"],info["Address"],info["Phone"],info["Email"],info["Location"])




    # get single

    def get_vehicle(self,ident):
        vehicle = self.get.get_certein(ident,"Data_files\Vehicles.csv")
        return DataAPI.make_vehicle(vehicle)

    def get_customer(self,ident):
        customer = self.get.get_certein(ident,"Data files\Customers.csv")
        return DataAPI.make_customer(customer)

    def get_destination(self,ident):
        destination = self.get.get_certein(ident,"Data files\Destinations.csv")
        return DataAPI.make_Destination(destination)

    def get_contract(self,ident):
        contract = self.get.get_certein(ident,"Data_files\Contracts.csv")
        return DataAPI.make_contract(contract)

    def get_employee(self,ident):
        employee = self.get.get_certein(ident,"Data files\Employees.csv")
        return DataAPI.make_employee(employee)


    # get multiple
    def get_vehicles(self):
        vehicle_list = []
        vehicles = self.get.get_csv("Data_files\Vehicles.csv")
        for obj in vehicles:
            vehicle = DataAPI.make_vehicle(obj)
            vehicle_list.append(vehicle)
        return vehicle_list

    def get_customers(self):
        customer_list = []
        customers = self.get.get_csv("Data files\Customers.csv")
        for obj in customers:
            customer = DataAPI.make_customer(obj)
            customer_list.append(customer)
        return customer_list

    def get_destinations(self):
        destinations = self.get.get_csv("Data files\Destinations.csv")
        destination_list = []
        for obj in destinations:
            destination = DataAPI.make_destination(obj)
            destination_list.append(destination)
        return destination_list

    def get_contracts(self):
        contract_list = []
        contracts = self.get.get_csv("Data_files\Contracts.csv")
        for obj in contracts:
            contract = DataAPI.make_contract(obj)
            contract_list.append(contract)
        return contract_list

    def get_employees(self):
        employees = self.get.get_csv("Data files\Employees.csv")
        employee_list = []
        for obj in employees:
            employee = DataAPI.make_employee(obj)
            employee_list.append(employee)
        return employee_list

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
        #available ætti að byrja sem True
        pass
    def add_customer(ID,Customer_name,License_type,GBP,BBP):
        pass
    def add_destination(ID,Destination_name,Phone,opening_hours,reportfilename):
        pass
    def add_contract(ID,employee_id,costumer_id,vehicle_id,start_date,end_date,paid):
        pass
    def add_employee(ID,Employee_name,SSN,Address,Phone,Email,Location):
        pass