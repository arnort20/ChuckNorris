from Data_classes.DataAPI import DataAPI as dAPI

class Destination_logic:
    def __init__(self):
        self.dAPI = dAPI()
    def new_destination(self,name, airport, phone, report_filename):
        new_dest_ID = self.dAPI.destination_makeID()
        self.dAPI.add_destination(new_dest_ID, name, airport, phone, report_filename)
    def get_destination(self, destID):
        return self.dAPI.get_destination(destID)
    def get_all_destinations(self):
        return self.dAPI.get_destinations()
    def change_destination(self, dest_ID, change_dict):
        self.dAPI.change_Destination(dest_ID, change_dict)


