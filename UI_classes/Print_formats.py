
# Hér eru öll print format commands geymd.

class Print_format():

    def liner(self):
        print("\n"*12)

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
        splitt_info = information
        if type(information) == str: 
            splitt_info = information.split(",")

        print("{:>20}".format("|"),end = "")
        basic =  int(width/len(splitt_info))
        fixer = width -(basic*len(splitt_info))
        for info in splitt_info:

            print(info.center(basic), end="")


        print(fixer*" "+"|")



    def print_space(self,width=200):
        print("{:>20} ".format("|"),end= "")
        print("{:>{size}} ".format("|",size = width))




    def question(self,question,width = 200):
        print("{:>{size}} ".format("",size = int(width/2-25)),end="")
        formatted = "{:>46}: ".format(question)
        return formatted


    def warning(self,text,width = 200):
        print(" {:>{size}}|  ".format("",size = int(width/2)),end="")
        print(text+ "  |")


    def short_box(self,information,title):
        self.print_title(title)
        self.print_space()
        self.print_out_format(information)
        self.print_space()
        self.print_line(len(title)*"_")

    def question_box(self,questions,information,title):
        self.print_title(title)
        self.print_space()

        self.print_out_format(information)
        self.print_space()
        self.print_line(len(title)*"_")


        self.print_space()    
        self.print_questions(questions)
        self.print_line(len(title)*"_")

    def list_box(self,title,options,info,second_str):
        self.print_title(title)
        self.print_space()
        self.print_out_format(options)
        self.print_space()
        self.print_line(len(title)*"_")
        #efri
        self.print_space()
        self.print_out_format(info)
        self.print_space()
        self.print_out_format(second_str)
        self.print_space()
        self.print_line(len(title)*"_")

    def large_list_box(self,options,title,list1,list2):
        self.short_box(options,title)
        self.print_space()
        self.print_out_format(list1)
        self.print_space()
        for item in list2:
            self.print_out_format(str(item))
        self.print_space()
        self.print_line(len(title)*"_")
