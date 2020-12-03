import csv
from Data_classes.get_io import Getter
from Data_classes.deleter_io import Dell

class Changer(object):
    def __init__(self) -> None:
        pass
    
    def change(filename,id,changes):
        item = Getter.get_certein(id,filename)
        new_item = item

        for key,value in changes.items():
            new_item[key] = value

        contracts = Getter.get_csv(filename)
        contracts[int(id)-1] = new_item
        Dell.rewrite_file(contracts,contracts,filename)
        