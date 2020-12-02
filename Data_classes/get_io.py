import csv

class Getter(object):
    def __init__(self) -> None:
        pass


    def get_id(filename):
        obj = open(filename)
        opener = csv.DictReader(obj)
        item_id = Getter.get_type(filename)
        last_id = 0

        for line in opener:
            last_id = line[item_id]
        obj.close()
        return str(int(last_id) + 1)


    def get_csv(filename):
        obj = open(filename)
        opener = csv.DictReader(obj)
        obj_list = []

        for line in opener:
            #test dict here
            obj_list.append(line)

        obj.close()
        return obj_list

    def get_type(filename):
        obj = open(filename)
        opener = csv.reader(obj)

        for line in opener:
            obj.close()
            return line[0]

    def get_certein(ident,filename):
        counter = 0
        obj = Getter.get_csv(filename)
        item_id = Getter.get_type(filename)

        for item in obj:
            
            if item[item_id] == ident:
                return item
            else:
                counter += 1

