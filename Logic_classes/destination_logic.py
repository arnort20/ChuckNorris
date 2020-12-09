from Data_classes.DataAPI import DataAPI as dAPI

class Destination_logic:
    def __init__(self):
        self.dAPI = dAPI()

    def new_destination(self,name, airport, phone, report_filename):
        #make the new destination, the ID is automatically generated
        new_dest_ID = self.dAPI.destination_makeID()
        self.dAPI.add_destination(new_dest_ID, name, airport, phone, report_filename)

    def get_destination(self, destID):
        #returns a destination object containing all information about the destination
        return self.dAPI.get_destination(destID)
        
    def get_all_destinations(self):
        #get a list of all destination objects in the database
        return self.dAPI.get_destinations()

    def change_destination(self, dest_ID, change_dict):
        #change the destination based on what keys to change and the new values for each key
        self.dAPI.change_Destination(dest_ID, change_dict)