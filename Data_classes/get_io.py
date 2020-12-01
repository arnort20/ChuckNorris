import csv

class getter(object):
    def __init__(self) -> None:
        pass


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

        return obj_list

    def get_certein(ident,filename):
        ident = "123"
        counter = 0
        obj = getter.get_csv(filename)

        for line in obj:
            if line[0] == ident:
                return line

