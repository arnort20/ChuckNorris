from Logic_classes.logic_wrapper import LogicAPI as lAPI
api = lAPI("1","1")


sasasoola = api.get_vehicle("7")
sas_age = sasasoola.age
#reservations = api.check_reservations("6")
#print(reservations)