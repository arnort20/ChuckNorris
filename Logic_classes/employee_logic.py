from Data_classes.DataAPI import DataAPI as dAPI


class Employee_logic:
    def __init__(self):
        self.dAPI = dAPI()

    def hire(self,Employee_name,ssn,Address,Phone,Email,Location, password):
        #hires a new employee, the employee ID is automatically generated
        employeeID = self.dAPI.employee_makeID()
        self.dAPI.add_employee(employeeID,Employee_name,ssn,Address,Phone,Email,Location,password)

    def fire(self,emp_ID):
        #removes the employee from the database
        self.dAPI.delete_employee(emp_ID)
        
    def change_employee(self, emp_ID, change_dict):
        #change the employee based on what keys to change and the new values for each key
        #please don't change their name or SSN
        self.dAPI.change_Employee(emp_ID, change_dict)
        
    def get_employee(self,emp_ID):
        #returns an employee object containing all information about them
        return self.dAPI.get_employee(emp_ID)

    def get_all_employees(self):
        return self.dAPI.get_employees()
        