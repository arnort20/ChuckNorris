class Employee(object):
    def __init__(self,ID,Employee_name,SSN,Address,Phone,Email,Location) -> None:
        self.id = ID
        self.employee_name = Employee_name
        self.SSN = SSN
        self.Address = Address
        self.Phone = Phone
        self.Email = Email
        self.Location = Location

    def __str__(self) -> str:
        pass
