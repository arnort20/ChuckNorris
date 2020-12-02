class Vehicle(object):
    def __init__(self,ID,vehicle_name,Type,Manufacturer,Model,Color,mileage,age,tax,available) -> None:
        self.id = ID
        self.vehicle_name = vehicle_name
        self.type = Type
        self.manufacturer = Manufacturer
        self.model = Model
        self.color = Color
        self.mileage = mileage
        self.age = age
        self.tax = tax
        self.available = available

    def __str__(self) -> str:
        pass
