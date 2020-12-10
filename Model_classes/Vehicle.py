class Vehicle(object):
    def __init__(self,ident,vehicle_name,Type,Manufacturer,Model,Color,age,available,location_id,license_type) -> None:
        self.id = ident
        self.vehicle_name = vehicle_name
        self.type = Type
        self.manufacturer = Manufacturer
        self.model = Model
        self.color = Color
        self.age = age
        #self.tax = tax
        self.available = available
        self.location = location_id
        self.license_type = license_type

    def __str__(self) -> str:
        #return(self.id +","+ self.vehicle_name+","+self.type+","+self.manufacturer+","+self.model+","+self.color+","+self.age+","+self.tax+","+self.available+","+self.location+","+self.license_type)
        return(self.id +","+ self.vehicle_name+","+self.type+","+self.manufacturer+","+self.model+","+self.color+","+self.age+","+self.available+","+self.location+","+self.license_type)
