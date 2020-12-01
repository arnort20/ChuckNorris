from Data_classes.DataAPI import *


class Employee:
    def hire(self,Employee_name,ssn,Address,Phone,Email,Location):
        employeeID = DataAPI.get_employeeID()
        DataAPI.add_employee(employeeID,Employee_name,ssn,Address,Phone,Email,Location)
        