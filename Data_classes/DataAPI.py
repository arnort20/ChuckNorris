
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

# skila objectum til logic
# skila listum af objectum til logic
# taka a moti objectum fra io closum

class DataAPI(object):
    def __init__(self):
        self.get = Getter
        self.add = Adder
        self.dell = Dell
        self.chang = Changer



    #make stuff-------------done
    def make_vehicle(ride):

        return Vehicle(ride["ID"],ride["Vehicle name"],ride["Type"],ride["Manufacturer"],ride["Model"],ride["Color"],ride["age"],ride["tax"],ride["available"],ride["location id"],ride["license type"])

    def make_customer(info):
        
        return Customer(info["ID"],info["Customer name"],info["email"],info["phone"],info["address"],info["License type"],info["GBP"],info["BBP"])

    def make_destination(info):
        
        return Destination(info["ID"],info["Destination name"],info["Phone"],info["opening hours"],info["report filename"])

    def make_contract(info):
     
        return Contract(info["contract ID"],info["employee ID"],info["customer ID"],info["vehicle ID"],info["start date"],info["end date"],info["paid?"])

    def make_employee(info):

        return Employee(info["ID"],info["Employee name"],info["SSN"],info["Address"],info["Phone"],info["Email"],info["Location"],info["Location"])



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
            return DataAPI.make_Destination(destination)
        except:
            return None

    def get_contract(self,ident):
        try:
            contract = self.get.get_certein(ident,"Data_files\Contracts.csv")
            #outputs list of dictionaries
            print(contract)
            return DataAPI.make_contract(contract)
        except:
            return None

    def get_employee(self,ident):
        try:
            employee = self.get.get_certein(ident,"Data_files\Employees.csv")
            return DataAPI.make_employee(employee)
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



    #add single-------------done
    def add_vehicle(self,ident,vehicle_name,Type,Manufacturer,Model,Color,age,tax,available,location_id,license_type):
        vehicle_dict = {"ID":ident,"Vehicle name":vehicle_name,"Type":Type,"Manufacturer":Manufacturer,"Model":Model,"Color":Color,"age":age,"tax":tax,"available":available,"location id":location_id,"license_type":license_type}
        self.add.add(vehicle_dict,"Data_files\Vehicles.csv")

    def add_customer(self,ident,Customer_name,email,phone,address,License_type,gbp,bbp):
        dicter = {"ID":ident,"Customer name":Customer_name,"email":email,"phone":phone,"address":address,"License_type":License_type,"GBP":gbp,"BBP":bbp}
        self.add.add(dicter,"Data_files\Customers.csv")

    def add_destination(self,ident,Destination_name,phone,opening_hours,report_filename):
        dicter = {"ID":ident,"Destination name":Destination_name,"Phone":phone,"opening hours":opening_hours,"report filename":report_filename}
        self.add.add(dicter,"Data_files\Destinations.csv")

    def add_contract(self,ident,employee_id,costumer_id,vehicle_id,start_date,end_date,paid):
        dicter = {"ID":ident,"employee_id":employee_id,"costumer_id":costumer_id,"vehicle_id":vehicle_id,"start_date":start_date,"end_date":end_date,"paid":paid}
        self.add.add(dicter,"Data_files\Contracts.csv")

    def add_employee(self,ident,Employee_name,ssn,Address,Phone,Email,Location):
        dicter = {"ID":ident,"Employee_name":Employee_name,"SSN":ssn,"Address":Address,"Phone":Phone,"Email":Email,"Location":Location}
        self.add.add(dicter,"Model_classes\Employee.py")



    # change single
    def change_vehicle(self,ident):
        pass

    def change_Customer(self,ident):
        pass

    def change_Destination(self,ident):
        pass

    def change_Contract(self,obj):
        pass

    def change_Employee(self,ident):
        pass



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

