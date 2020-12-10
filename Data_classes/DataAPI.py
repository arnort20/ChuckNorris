
import csv
from Data_classes.add_io import Adder
from Data_classes.get_io import Getter
from Data_classes.deleter_io import Dell
from Data_classes.changer_io import Changer
from Model_classes.Contract import Contract
from Model_classes.Customer import Customer
from Model_classes.Destination import Destination
from Model_classes.Employee import Employee
from Model_classes.Vehicle import Vehicle
from Model_classes.Bill import Bill

# skila objectum til logic
# skila listum af objectum til logic
# taka a moti objectum fra io closum

class DataAPI(object):
    
    def __init__(self):
        self.get = Getter
        self.add = Adder
        self.dell = Dell
        self.chang = Changer
# laga i utf encoding


    #make stuff-------------done
    def make_vehicle(ride):

        return Vehicle(ride["id"],ride["vehicle_name"],ride["type"],ride["manufacturer"],ride["model"],ride["color"],ride["age"],ride["tax"],ride["available"],ride["location_id"],ride["license_type"])

    def make_customer(info):
        
        return Customer(info["id"],info["customer_name"],info["ssn"],info["email"],info["phone"],info["address"],info["license_type"],info["gbp"],info["bbp"])

    def make_destination(info):
        
        return Destination(info["id"],info["destination_name"],info["airport"],info["phone"],info["country_name"],info["opening_hours"])

    def make_contract(info):
     
        return Contract(info["contract_id"],info["employee_id"],info["customer_id"],info["vehicle_id"],info["destination_id"],info["start_date"],info["end_date"],info["paid?"])

    def make_employee(info):

        return Employee(info["id"],info["employee_name"],info["ssn"],info["address"],info["phone"],info["email"],info["location"],info["password"])

    def make_bill(info):

        return Bill(info["id"],info["fetch_date"],info["return_date"],info["location_id"],info["price"])




    # get single-------------done
    def get_vehicle(self,ident):
        try:
            vehicle = self.get.get_certein(ident,"Data_files\Vehicles.csv")
            return DataAPI.make_vehicle(vehicle)
        except:
            return None

    def get_customer(self,ident):
        try:
            customer = self.get.get_certein(ident,"Data_files\Customers.csv")
            return DataAPI.make_customer(customer)
        except:
            return None

    def get_destination(self,ident):
        try:
            destination = self.get.get_certein(ident,"Data_files\Destinations.csv")
            return DataAPI.make_destination(destination)
        except:
            return None

    def get_contract(self,ident):
        try:
            contract = self.get.get_certein(ident,"Data_files\Contracts.csv")
            #outputs list of dictionaries
            return DataAPI.make_contract(contract)
        except:
            return None

    def get_employee(self,ident):
        try:
            employee = self.get.get_certein(ident,"Data_files\Employees.csv")
            return DataAPI.make_employee(employee)
        except:
            return None

    def get_bill(self,ident):
        try:
            bill = self.get.get_certein(ident,"Data_files\Bills.csv")
            return DataAPI.make_bill(bill)
        except:
            return None



    # get multiple-------------done
    def get_vehicles(self):
        vehicle_list = []
        vehicles = self.get.get_csv("Data_files\Vehicles.csv")
        for obj in vehicles:
            vehicle = DataAPI.make_vehicle(obj)
            vehicle_list.append(vehicle)
        return vehicle_list

    def get_customers(self):
        customer_list = []
        customers = self.get.get_csv("Data_files\Customers.csv")
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
        #outputs single dictionary

        for obj in contracts:
            contract = DataAPI.make_contract(obj)
            contract_list.append(contract)
        return contract_list

    def get_employees(self):
        employees = self.get.get_csv("Data_files\Employees.csv")
        employee_list = []
        for obj in employees:
            employee = DataAPI.make_employee(obj)
            employee_list.append(employee)
        return employee_list

    def get_bills(self):
        bills = self.get.get_csv("Data_files\Bills.csv")
        bill_list = []
        for obj in bills:
            bill = DataAPI.make_bill(obj)
            bill_list.append(bill)
        return bill_list



    #make,ident-------------done
    def vehicles_makeID(self):
        return self.get.get_id("Data_files\Vehicles.csv")

    def customer_makeID(self):
        #not needed
        return self.get.get_id("Data_files\Customers.csv")

    def destination_makeID(self):
        return self.get.get_id("Data_files\Destinations.csv")

    def contract_makeID(self):
        return self.get.get_id("Data_files\Contracts.csv")

    def employee_makeID(self):
        return self.get.get_id("Data_files\Employees.csv")

    def bill_makeID(self):
        #not needed
        return self.get.get_id("Data_files\Bills.csv")



    #add single-------------done
    # def add_vehicle(self,ident,vehicle_name,Type,Manufacturer,Model,Color,age,tax,available,location_id,license_type):
    #     vehicle_dict = {"id":ident,"vehicle_name":vehicle_name,"type":Type,"manufacturer":Manufacturer,"model":Model,"color":Color,"age":age,"tax":tax,"available":available,"location_id":location_id,"license_type":license_type}
    #     self.add.add(vehicle_dict,"Data_files\Vehicles.csv")
    def add_vehicle(self,ident,vehicle_name,Type,Manufacturer,Model,Color,age,available,location_id,license_type):
        vehicle_dict = {"id":ident,"vehicle_name":vehicle_name,"type":Type,"manufacturer":Manufacturer,"model":Model,"color":Color,"age":age,"available":available,"location_id":location_id,"license_type":license_type}
        self.add.add(vehicle_dict,"Data_files\Vehicles.csv")

    def add_customer(self,ident,customer_name,ssn,email,phone,address,license_type,gbp,bbp):
        dicter = {"id":ident,"customer_name":customer_name,"ssn":ssn,"email":email,"phone":phone,"address":address,"license_type":license_type,"gbp":gbp,"bbp":bbp}
        self.add.add(dicter,"Data_files\Customers.csv")

    def add_destination(self,ident,destination_name,phone,opening_hours,report_filename,country_name,airport):
        dicter = {"id":ident,"destination_name":destination_name,"country_name":country_name,"airport":airport,"phone":phone,"opening_hours":opening_hours,"report_filename":report_filename}
        self.add.add(dicter,"Data_files\Destinations.csv")

    def add_contract(self,ident,employee_id,customer_id,vehicle_id,destination_id,start_date,end_date,paid):
        dicter = {"id":ident,"employee_id":employee_id,"customer_id":customer_id,"vehicle_id":vehicle_id,"destination_id":destination_id,"start_date":start_date,"end_date":end_date,"paid":paid}
        self.add.add(dicter,"Data_files\Contracts.csv")

    def add_employee(self,ident,employee_name,ssn,address,phone,email,location,password):
        dicter = {"id":ident,"employee_name":employee_name,"ssn":ssn,"address":address,"phone":phone,"email":email,"location":location,"password":password}
        self.add.add(dicter,"Data_files\Employees.csv")

    def add_bill(self,contract_id,fetch_date,return_date,location_id,price):
        dicter = {"contract_id":contract_id,"fetch_date":fetch_date,"return_date":return_date,"location_id":location_id,"price":price}
        self.add.add(dicter,"Data_files\Bills.csv")



    # change single
    def change_vehicle(self,ident,changes):
        self.chang.change("Data_files\Vehicles.csv",ident,changes)

    def change_Customer(self,ident,changes):
        self.chang.change("Data_files\Customers.csv",ident,changes)

    def change_Destination(self,ident,changes):
        self.chang.change("Data_files\Destinations.csv",ident,changes)

    def change_Contract(self,ident,changes):
        self.chang.change("Data_files\Contracts.csv",ident,changes)

    def change_Employee(self,ident,changes):
        self.chang.change("Data_files\Employees.csv",ident,changes)

    def change_Bill(self,ident,changes):
        self.chang.change("Data_files\Bills.csv",ident,changes)



    #delete single-------------done
    def delete_vehicle(self,ident):
        self.dell.dell("Data_files\Vehicles.csv",ident)

    def delete_customer(self,ident):
        self.dell.dell("Data_files\Customers.csv",ident)

    def delete_destination(self,ident):
        self.dell.dell("Data_files\Destinations.csv",ident)

    def delete_contract(self,ident):
        self.dell.dell("Data_files\Contracts.csv",ident)

    def delete_employee(self,ident):
        self.dell.dell("Data_files\Employees.csv",ident)

    def delete_bill(self,ident):
        self.dell.dell("Data_files\Bills.csv",ident)
