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
            print
            obj_list.append(line)

        return obj_list

    def get_type(filename):
        obj = open(filename)
        opener = csv.reader(obj)
        for line in opener:
            return line

    def get_certein(ident,filename):
        ident = "1"
        counter = 0
        obj = Getter.get_csv(filename)
        listed_first_line = Getter.get_type(filename)
        item_id = listed_first_line[0]
        for item in obj:
            if item[item_id] == ident:
                return item
            else:
                counter += 1

