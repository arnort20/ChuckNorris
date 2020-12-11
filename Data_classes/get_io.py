import csv

class Getter(object):
    def __init__(self) -> None:
        pass

    # gets latest id input in the file nad adds one to it
    def get_id(filename):
        obj = open(filename,encoding="utf-8")
        opener = csv.DictReader(obj)
        item_id = Getter.get_type(filename)
        last_id = 0

        for line in opener:
            last_id = line[item_id]
        obj.close()
        return str(int(last_id) + 1)

    # gets all items in file and returns
    def get_csv(filename):
        obj = open(filename,encoding="utf-8")
        opener = csv.DictReader(obj)
        obj_list = []

        for line in opener:
            #test dict here
            obj_list.append(line)

        obj.close()
        return obj_list

    # gets the name of the first thing in the file which supposed to be the type of item or identifier which it outputs to get id 
    def get_type(filename):
        obj = open(filename,encoding="utf-8")
        opener = csv.reader(obj)

        for line in opener:
            obj.close()
            return line[0]
            
    #get one item with certein id from file
    def get_certein(ident,filename):
        counter = 0
        obj = Getter.get_csv(filename)
        item_id = Getter.get_type(filename)

        for item in obj:
            
            if item[item_id] == ident:
                return item
            else:
                counter += 1

