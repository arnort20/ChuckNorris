import csv
class Vehicle(object):
    def __init__(self,ID,vehicle_name,Type,Manufacturer,Model,Color,mileage,age,tax,available) -> None:
        self.id = ID
        self.vehicle_name = vehicle_name
        self.type = Type
        self.manufacturer = Manufacturer
        self.model = Model
        self.color = Color
        self.mileage = mileage
        self.age = age
        self.tax = tax
        self.available = available


def get_vehicle(ident):
    ident = "123"
    counter = 0
    obj = get_vehicles("Data_classes\Customer_io.py")

    for line in obj:
        if line[0] == ident:
            print(line)
            return line

def get_vehicles(filename):
    obj = open(filename)
    opener = csv.reader(obj)
    obj_list = []
    for line in opener:

        fixed_line = line[0].replace(";",", " )
        fixed_line = fixed_line.split(",")
        obj_list.append(fixed_line)
        print(obj_list)s

    return obj_list
