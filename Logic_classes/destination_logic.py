from Data_classes.DataAPI import DataAPI as dAPI

class Destination:
    def __init__(self):
        self.dAPI = dAPI()
    def new_destination(name, airport, phone)