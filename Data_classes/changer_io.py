import csv
from Data_classes.get_io import Getter
from Data_classes.deleter_io import Dell

class Changer(object):
    def __init__(self) -> None:
        pass
    
    # this one is made to find item change it and rewrite the file with it changed
    def change(filename,ident,changes):
        item = Getter.get_certein(ident,filename)
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
    

    #this one is specially made for the type file since it has to find 2 items and match them to find it
    #i would have made this easier to use for other things but there was no reason to
    def change_2(filename,ident,second_id,changes):
        list_dict = Getter.get_csv(filename)

        for thing in list_dict:
            if thing["name"] == ident and thing["destination_id"] == second_id:
                item = thing

        counter = 0
        for thing in list_dict:

            if thing == item:

                for key,value in changes.items():
                    item[key] = value
                
                list_dict[counter] = item

            else:
                counter += 1
                
                #extra list dict is just for fun 
            Dell.rewrite_file(list_dict,list_dict,filename)