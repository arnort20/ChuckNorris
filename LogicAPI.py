from DataAPI import *

#make logic for the following:
#Contract
"""
contract ID
employee ID
customer ID
vehicle ID(comma seperated)
start date
end date
paid?
"""

class Contract:
    
def getContract(contractID):
    contract = DataAPI.getContract(contractID)
    return contract
def changeContract(contractID):
    pass



#Customer(contract)
"""
ID
name
license type
GBP
BBP
"""
class Customer:
    pass
def makeNewCustomer(name, licenseType):
    pass
def addGBP(customerID):
    pass



#Employee
"""
ID
name
SSN
Address
phone
Email
location
"""
class Employee:
    def __init__(self, empID):
        self.name,self.ssn,self.address,self.phone,self.email,self.location = DataAPI.getEmpoyee(empID)
        if self.location == 1:
            self.cn = True
        elif self.location == 2:
            self.rvk = True
    def changeInfo(self, data, newInfo):
        pass
    

def makeNewEmpoyee(name, ssn, address, phone, email, location):
    empID = getEmpID()



#Destination
"""
ID 
name
phone
opening hours
report filename
"""



#Vehicle(destination)
"""
ID
name
type
manufacturer
model
color
mileage
age
tax
avaiable
"""
def makeNewVehicle(name='N/A', vtype, manufacturer='N/A', model='N/A', color='N/A', age=0, tax):
    pass
class Vehicle:
    def __init__(self, name='N/A', vtype, manufacturer='N/A', model='N/A', color='N/A', age=0, tax):
        self.name = name
        self.type = vtype
        self.manufacturer = manufacturer
        self.model = model
        self.color = color
        self.age = age
        self.tax = tax



