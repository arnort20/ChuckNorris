import csv

class Getter(object):
    def __init__(self) -> None:
        pass


    def get_id(filename):
        pass


    def get_csv(filename):
        obj = open(filename)
        opener = csv.DictReader(obj)
        obj_list = []
        for line in opener:
            

            #fixed_line = line[0].replace(";",", " )
            #fixed_line = fixed_line.split(",")
            obj_list.append(line)

        return obj_list

    def get_certein(ident,filename):
        ident = "123"
        counter = 0
        obj = Getter.get_csv(filename)

        for line in obj:
            if line[0] == ident:
                return line

