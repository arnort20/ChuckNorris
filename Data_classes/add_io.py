from typing import Dict
import csv

class Adder(object):
    def __init__(self) -> None:
        pass

    def add(self,dict,filename):
        writing = csv.DictWriter()
        writing.writerow()