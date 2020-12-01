import csv
class Contract(object):
    def __init__(self,ID,employee_id,costumer_id,vehicle_id,start_date,end_date,paid) -> None:
        self.id = ID
        self.employee_id = employee_id
        self.costumer_id = costumer_id
        self.vehicle_id = vehicle_id
        self.start_date = start_date
        self.end_date = end_date
        self.paid = paid

def get_contract(ident):
    ident = "123"
    counter = 0
    obj = get_contracts("Data_classes\Customer_io.py")

    for line in obj:
        if line[0] == ident:
            print(line)
            return line

def get_contracts(filename):
    obj = open(filename)
    opener = csv.reader(obj)
    obj_list = []
    for line in opener:

        fixed_line = line[0].replace(";",", " )
        fixed_line = fixed_line.split(",")
        obj_list.append(fixed_line)
        print(obj_list)s

    return obj_list
