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
    def change_employee(self, emp_ID, change_dict):
        dAPI.change_Employee(emp_ID, change_dict)
        
    def get_employee(self,emp_ID):
        return self.dAPI.get_employee(emp_ID)
