from Data_classes.DataAPI import DataAPI as dAPI


class Employee:
    def __init__(self):
        self.dAPI = dAPI()
    def hire(self,Employee_name,ssn,Address,Phone,Email,Location):
        employeeID = DataAPI.get_employeeID()
        DataAPI.add_employee(employeeID,Employee_name,ssn,Address,Phone,Email,Location)
        