import csv
class Customer(object):
    def __init__(self,ID,Customer_name,License_type,GBP,BBP) -> None:
        self.id = ID
        self.costumer_name = Customer_name
        self.License_type = License_type
        self.GBP = GBP
        self.BBP = BBP

def get_Customer(ident):
    ident = "123"
    counter = 0
    obj = get_costumers("Data_classes\Customer_io.py")

    for line in obj:
        if line[0] == ident:
            print(line)
            return line

def get_costumers(filename):
    obj = open(filename)
    opener = csv.reader(obj)
    obj_list = []
    for line in opener:

        fixed_line = line[0].replace(";",", " )
        fixed_line = fixed_line.split(",")
        obj_list.append(fixed_line)
        print(obj_list)s

    return obj_list

