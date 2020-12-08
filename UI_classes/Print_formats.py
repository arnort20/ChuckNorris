
# Hér eru öll print format commands geymd.

class Print_format():

# Þessi þarf að geta prentað út Title á flottan hátt.
    def print_title(self,title="_",width=200):# Langar að breyta þannig að Title centerist við info úr main menu!
    # Title = Nafn á Völdum kosti

        name_title = ('{:_^{size}}'.format(title,size = width)).center(width+40)
        print(name_title)
        #Þurfum ekki að hafa center með þessu formati


# Langar að breyta þannig að Title centerist við info úr main menu!
    def print_line(self,title="_",width=200):  
    # Title = Nafn á Völdum kosti
        print("{:>20} ".format("|"),end= "")
        
        name_title = ('{:_^{size}}'.format(title,size = width-1))
        print(name_title,end= "")
        print("|")

        #Þurfum ekki að hafa center með þessu formati



    # þessi þarf að geta prentað út þægilegt og flott main menu 
    def print_main_menu(self,option,width=200):

        splitt_info = option.split(",")
        for info in splitt_info:
            print("{:>20} ".format("|"),end="")
            
            print("{:>{size}} ".format("",size = width/2-20),end="")

            title = ("\t{:<40}".format(info))
            print(title,end="")

            print("{:>{size}} ".format("|",size = width-40-int(width/2.4)))

            #extra cash money bil
            Print_format().print_space()




    def print_questions(self,dicter,width=200):
        for key,value in dicter.items():
            #print((" "*int(width/2-2))+"|"+"|\t{:<40}: ".format(key.replace("_"," ")),end=" ")
            print("{:>20} ".format("|"),end="")
            print("{:>{size}} ".format("",size = int(width/2-30)),end="")
            print("\t{:<40}: ".format(key.replace("_"," ")),end="")
            print(value,end="")
            print("{:>{size}} ".format("|",size = width-17-(len(value))-int(width/2)))
      






    # Þessi þarf að geta prentað út textan sem er sóttur úr skjölum á þokkalegan hátt
    def print_out_format(self,information,width=200):
        # Information = Efsta línan sem er upplysingar um hvað er hvað.

        splitt_info = information.split(",")
        print("{:>20}".format("|"),end = " ")
        
        for info in splitt_info:
            print(info.center(int(width/len(splitt_info))), end="")

        fixer = (len(splitt_info)/width) - width 
        print(((width-((int(width/len(splitt_info)))*len(splitt_info))))*" "+ "|", end="")
        print("")



    def print_space(self,width=200):
        print("{:>20} ".format("|"),end= "")
        print("{:>{size}} ".format("|",size = width))




    def question(self,question,width = 200):
        print("{:>{size}} ".format("",size = int(width/2-20)),end="")
        formatted = "{:>46}: ".format(question)
        return formatted


    def warning(self,text,width = 200):
        print(" {:>{size}}|  ".format("",size = int(width/2)),end="")
        print(text+ "  |")