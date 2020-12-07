from Data_classes.DataAPI import DataAPI as dAPI


class Employee:
    def __init__(self):
        self.dAPI = dAPI()
    def hire(self,Employee_name,ssn,Address,Phone,Email,Location, password):
        employeeID = self.dAPI.employee_makeID()
        self.dAPI.add_employee(employeeID,Employee_name,ssn,Address,Phone,Email,Location,password)
    def fire(self,emp_ID):
        self.dAPI.delete_employee(emp_ID)
        #removes employee form database
        
    def change_employee(self, emp_ID, change_dict):
        self.dAPI.change_Employee(emp_ID, change_dict)
        
    def get_employee(self,emp_ID):
        return self.dAPI.get_employee(emp_ID)
