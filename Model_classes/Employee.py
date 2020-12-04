class Employee(object):
    def __init__(self,ident,Employee_name,ssn,Address,Phone,Email,Location,password):
        self.id = ident
        self.employee_name = Employee_name
        self.ssn = ssn
        self.address = Address
        self.phone = Phone
        self.email = Email
        self.location = Location
        self.password = password
    def __str__(self) -> str:
        pass
