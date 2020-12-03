from Data_classes.DataAPI import DataAPI as dAPI

class Destination:
    def __init__(self):
        self.dAPI = dAPI()
    def new_destination(self,name, airport, phone, report_filename):
        new_dest_ID = self.dAPI.destination_makeID()
        self.dAPI.add_destination(new_dest_ID, name, airport, phone, report_filename)
    def get_destination(self, destID):
        return self.dAPI.get_destination(destID)
    def get_all_destinations(self):
        return self.dAPI.get_destinations()
    def change_destination_name(self, dest_ID, new_name):
        pass
    def change_destination_airport(self, dest_ID, new_name):
        pass
    def change_destination_phone(self, dest_ID, new_phone):
        pass
    def change_destination_filename(self, dest_ID, new_filename):
        pass
    def change_opening_hours(self, dest_ID):
        pass


