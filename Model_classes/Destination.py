class Destination(object):
    def __init__(self,ID,Destination_name,airport_code,Phone,opening_hours,reportfilename) -> None:
        self.id = ID
        self.Destination = Destination_name
        self.airport_code = airport_code
        self.Phone = Phone
        self.opening_hours = opening_hours
        self.report_filename = reportfilename

    def __str__(self) -> str:
        pass
