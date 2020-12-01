# This part reads and writes files



# read data from file
# change csv file to dictionary
# 


import csv
"""
def dictionary_csv(filename):
    first_line = 0
    full_dict = {}
    for line in filename:

        splitted = line.split()
        if first_line == 0:
            first_line = splitted

        else:
            counter = 0
            line_info = {}
            for value in splitted:
                line_info[first_line[counter]] = splitted[counter]

            full_dict[splitted[0]] = line_info
"""


# skila contract objecti til logic
def get_id(filename):
    pass


def get_csv(filename):
    obj = open(filename)
    opener = csv.reader(obj)
    obj_list = []
    for line in opener:
        fixed_line = line[0].replace(";",", " )
        fixed_line = fixed_line.split(",")
        obj_list.append(fixed_line)
        print(obj_list)
    return obj_list

def get_certein(ident,filename):
    ident = "123"
    counter = 0
    obj = get_csv(filename)
    for line in obj:
        if line[0] == ident:
            print(line)
            return line







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

def main():
    filename = 'excel files\Contracts.csv'
    get_csv(filename)
   # get_certein("123",filename)

main()