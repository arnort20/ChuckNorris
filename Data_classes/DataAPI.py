


import csv
from Contracts_io import Contract
from Customer_io import Customer
from Destination_io import Destination
from Employee_io import Employee
from Vehicle_io import Vehicle

# skila objectum til logic
# skila listum af objectum til logic
# taka a moti objectum fra io closum


class Contract(object):
    def __init__(self,ID,employee_id,costumer_id,vehicle_id,start_date,end_date,paid) -> None:
        self.id = ID
        self.employee_id = employee_id
        self.costumer_id = costumer_id
        self.vehicle_id = vehicle_id
        self.start_date = start_date
        self.end_date = end_date
        self.paid = paid

    def get_contract():

class Employee(object):
    def __init__(self,ID,Employee_name,SSN,Address,Phone,Email,Location) -> None:
        self.id = ID
        self.employee_name = Employee_name
        self.SSN = SSN
        self.Address = Address
        self.Phone = Phone
        self.Email = Email
        self.Location = Location

class Vehicle(object):
    def __init__(self,ID,vehicle_name,Type,Manufacturer,Model,Color,mileage,age,tax,available) -> None:
        self.id = ID
        self.vehicle_name = vehicle_name
        self.type = Type
        self.manufacturer = Manufacturer
        self.model = Model
        self.color = Color
        self.mileage = mileage
        self.age = age
        self.tax = tax
        self.available = available

class Destination(object):
    def __init__(self,ID,Destination_name,Phone,opening_hours,reportfilename) -> None:
        self.id = ID
        self.Destination = Destination_name
        self.Phone = Phone
        self.opening_hours = opening_hours
        self.report_filename = reportfilename





def get_id(filename):
    pass


def get_csv(filename):
    obj = open(filename)
    opener = csv.reader(obj)
    obj_list = []
    for line in opener:

        fixed_line = line[0].replace(";",", " )
        fixed_line = fixed_line.split(",")
        obj_list.append(fixed_line)
        print(obj_list)

    return obj_list

def get_certein(ident,filename):
    ident = "123"
    counter = 0
    obj = get_csv(filename)

    for line in obj:
        if line[0] == ident:
            print(line)
            return line



def main():
    filename = 'excel files\Contracts.csv'
    get_csv(filename)
   # get_certein("123",filename)

main()