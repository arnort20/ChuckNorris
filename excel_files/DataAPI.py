# This part reads and writes files



# read data from file
# change csv file to dictionary
# 


import csv
"""
def dictionary_csv(filename):
    first_line = 0
    full_dict = {}
    for line in filename:

        splitted = line.split()
        if first_line == 0:
            first_line = splitted

        else:
            counter = 0
            line_info = {}
            for value in splitted:
                line_info[first_line[counter]] = splitted[counter]

            full_dict[splitted[0]] = line_info
"""


# skila contract objecti til logic
   

class Contract(object):
    def __init__(self,employee_id,costumer_id,vehicle_id,start_date,end_date,paid) -> None:
        self.id = last_id + 1
        self.employee_id = employee_id
        self.costumer_id = costumer_id
        self.vehicle_id = vehicle_id
        self.start_date = start_date
        self.end_date = end_date
        self.paid = paid

    def get_contracts():
        contracts = open("Contracts.csv")
        
            

class Employee(object):
    def __init__(self) -> None:
        pass

class Destination(object):
    def __init__(self) -> None:
        pass

class Costumer(object):
    def __init__(self) -> None:
        pass

class Vehicle(object):
    def __init__(self) -> None:
        pass

def main():
    print(get_contracts)