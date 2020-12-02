from typing import Dict
import csv

class Adder(object):
    def __init__(self) -> None:
        pass

    def add(dicter,filename):
        filed = open(filename,"at", newline='')
        fields = dicter.keys()
        writing = csv.DictWriter(filed,fieldnames=fields)
        writing.writerow(dicter)
        filed.close()