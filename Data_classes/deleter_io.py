from Data_classes.get_io import Getter
import csv


class Dell(object):
    def __init__(self) -> None:
        pass

    def dell(filename,ident):
        new_list = []
        got_whole = Getter.get_csv(filename)
        got_single = Getter.get_certein(ident,filename)

        # go through all items in the file and add all to new one
        # except the one that is supposed to be deleted
        for obj in got_whole:
            if obj != got_single:
                new_list.append(obj)

        Dell.rewrite_file(got_whole,new_list,filename)


    def rewrite_file(old_list,new_list,filename):
        filed = open(filename,"w", newline="",encoding="utf-8")
        fields = old_list[0].keys()

        writing = csv.DictWriter(filed,fieldnames=fields)
        writing.writeheader()
        writing.writerows(new_list)

