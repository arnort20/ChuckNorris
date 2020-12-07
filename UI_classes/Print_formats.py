
# Hér eru öll print format commands geymd.

class print_format():
    def __init__(self):
        pass

# Þessi þarf að geta prentað út Title á flottan hátt.
    def print_title(self,title):# Langar að breyta þannig að Title centerist við info úr main menu!
    # Title = Nafn á Völdum kosti
        print("")
        name_title = ('{:-^135}'.format(title))
        print(name_title)
        #Þurfum ekki að hafa center með þessu formati
        print("")

    # þessi þarf að geta prentað út þægilegt og flott main menu 
    def print_main_menu(self,option):
        # Prentar út Main menu textan í ákveðnu formati
        splitt_info = option.split(",")
        for info in splitt_info:
            print("|{:^40}|".format(info))
            #Þurfum ekki að hafa center með þessu formati
            #print("{0: >40}".format(info))

    # Þessi þarf að geta prentað út textan sem er sóttur úr skjölum á þokkalegan hátt
    def print_out_format(self,information):
        # Information = Efsta línan sem er upplysingar um hvað er hvað.
        splitt_info = information.split(",")
        for info in splitt_info:
            print(info.center(20), end="")

        print("")