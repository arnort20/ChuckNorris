import csv

def get_destination(ident):
    ident = "123"
    counter = 0
    obj = get_destinations("Data_classes\Customer_io.py")

    for line in obj:
        if line[0] == ident:
            print(line)
            return line

def get_destinations(filename):
    obj = open(filename)
    opener = csv.reader(obj)
    obj_list = []
    for line in opener:

        fixed_line = line[0].replace(";",", " )
        fixed_line = fixed_line.split(",")
        obj_list.append(fixed_line)
        print(obj_list)s

    return obj_list
