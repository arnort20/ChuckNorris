from Data_classes.get_io import Getter
import csv


class Dell(object):
    def __init__(self) -> None:
        self.get = Getter

    def dell(self,filename,ident):
        got_whole = self.get.get_csv(filename)
        got_single = self.get.get_certein(ident,filename)
        new_file = got_whole-got_single
        Dell.rewrite_file(new_file,filename)


    def rewrite_file(new_file,filename):
        filed = open(filename,"w", newline="")
        fields = new_file[0].keys()
        writing = csv.DictWriter(filed,fieldnames=fields)
        writing.writerows(new_file)

