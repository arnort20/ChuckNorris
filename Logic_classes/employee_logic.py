from Data_classes.DataAPI import DataAPI as dAPI


class Employee:
    def __init__(self):
        self.dAPI = dAPI()
    def hire(self,Employee_name,ssn,Address,Phone,Email,Location):
        employeeID = dAPI.get_employeeID()
        dAPI.add_employee(employeeID,Employee_name,ssn,Address,Phone,Email,Location,password)
    def fire(self,emp_ID):
        #removes employee form database
        pass
    def change_name(self,emp_ID,new_name):
        #makes changes
        pass
    def change_address(self,emp_ID,new_address):
        #makes changes
        pass
    def change_SSN(self,emp_ID,new_ssn):
        #makes changes
        pass
    def change_phone(self,emp_ID,new_phone):
        #makes changes
        pass
    def change_email(self,emp_ID,new_email):
        #makes changes
        pass
    def change_location(self,emp_ID,new_location):
        #makes changes
        pass
    def get_employee(self,emp_ID):
        return self.dAPI.get_employee(emp_ID)
