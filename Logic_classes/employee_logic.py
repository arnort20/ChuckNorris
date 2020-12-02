from Data_classes.DataAPI import DataAPI as dAPI


class Employee:
    def __init__(self):
        self.dAPI = dAPI()
    def hire(self,Employee_name,ssn,Address,Phone,Email,Location):
        employeeID = dAPI.get_employeeID()
        dAPI.add_employee(employeeID,Employee_name,ssn,Address,Phone,Email,Location)
    def fire(self,emp_ID):
        #removes employee form database
        pass
    def change_name(self,emp_ID):
        #makes changes
        pass
    def change_address(self,emp_ID):
        #makes changes
        pass
    def change_SSN(self,emp_ID):
        #makes changes
        pass
    def change_phone(self,emp_ID):
        #makes changes
        pass
    def change_email(self,emp_ID):
        #makes changes
        pass
    def change_location(self,emp_ID):
        #makes changes
        pass
    