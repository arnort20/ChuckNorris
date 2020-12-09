class Destination(object):
    def __init__(self,ident,Destination_name,airport_code,Phone,country,opening_hours) -> None:
        self.id = ident
        self.Destination = Destination_name
        self.airport_code = airport_code
        self.Phone = Phone
        self.opening_hours = opening_hours
        self.country =country

    def __str__(self) -> str:
        return ("lets get poopin")
