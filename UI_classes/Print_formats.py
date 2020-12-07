
# Hér eru öll print format commands geymd.

class Print_format():

# Þessi þarf að geta prentað út Title á flottan hátt.
    def print_title(self,title,width=135):# Langar að breyta þannig að Title centerist við info úr main menu!
    # Title = Nafn á Völdum kosti
        print("")
        name_title = ('{:-^{size}}'.format(title,size = width)).center(width+40)
        print(name_title)
        #Þurfum ekki að hafa center með þessu formati
        print("")

    # þessi þarf að geta prentað út þægilegt og flott main menu 
    def print_main_menu(self,option,width=0):
        # Prentar út Main menu textan í ákveðnu formati
        splitt_info = option.split(",")
        for info in splitt_info:
            title = ("|\t{:<40}|".format(info)).center(width+40)
            print(title)
            #Þurfum ekki að hafa center með þessu formati
            #print("{0: >40}".format(info))

    # Þessi þarf að geta prentað út textan sem er sóttur úr skjölum á þokkalegan hátt
    def print_out_format(self,information,width=0):
        # Information = Efsta línan sem er upplysingar um hvað er hvað.


        splitt_info = information.split(",")
        streng = ""
        print((" "*int(width)), end="")
        for info in splitt_info:
            print(info.center(20), end="")
        print("")


    def question(self,question,width = 0):
        formatted = ((" "*int(width/2-2))+"|\t{:<40}: ".format(question))
        return formatted