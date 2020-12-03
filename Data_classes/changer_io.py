import csv
from Data_classes.get_io import Getter
from Data_classes.deleter_io import Dell

class Changer(object):
    def __init__(self) -> None:
        pass
    
    def change(filename,id,changes):
        item = Getter.get_certein(id,filename)
        new_item = item
        list_dict = Getter.get_csv(filename)

        counter = 0
        for thing in list_dict:

            if thing == item:

                for key,value in changes.items():
                    new_item[key] = value
                    
                list_dict[counter] = new_item

            else:
                counter += 1

        Dell.rewrite_file(list_dict,list_dict,filename)
        