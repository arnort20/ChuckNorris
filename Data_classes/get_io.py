import csv


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

