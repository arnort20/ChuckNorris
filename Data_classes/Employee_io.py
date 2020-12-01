import csv
class Employee(object):
    def __init__(self,ID,Employee_name,SSN,Address,Phone,Email,Location) -> None:
        self.id = ID
        self.employee_name = Employee_name
        self.SSN = SSN
        self.Address = Address
        self.Phone = Phone
        self.Email = Email
        self.Location = Location

def get_employee(ident):
    ident = "123"
    counter = 0
    obj = get_employees("Data_classes\Customer_io.py")

    for line in obj:
        if line[0] == ident:
            print(line)
            return line

def get_employees(filename):
    obj = open(filename)
    opener = csv.reader(obj)
    obj_list = []
    for line in opener:

        fixed_line = line[0].replace(";",", " )
        fixed_line = fixed_line.split(",")
        obj_list.append(fixed_line)
        print(obj_list)s

    return obj_list
