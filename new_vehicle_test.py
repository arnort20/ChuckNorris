from Logic_classes.logic_wrapper import LogicAPI as lAPI

api = lAPI()
#api.make_new_vehicle("gr 425","minijeep","toyota","Jimny","green","2020","1.24","3")
#api.new_customer("0371188555","Nóri2","afgva@ggew.com","9549564","cewafdwea 10","A,C")
if api.check_license("0371188555","1"):
    print("success!")
else:
    print("fail")

