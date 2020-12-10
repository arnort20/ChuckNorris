class Customer(object):
    def __init__(self,ident,customer_name,Social_security_number,email,phone,address,License_type,gbp,bbp):
        self.id = ident
        self.customer_name = customer_name
        self.License_type = License_type
        self.gbp = gbp
        self.bbp = bbp
        self.email = email
        self.phone = phone
        self.address = address
        self.Social_security_number = Social_security_number

    def __str__(self) -> str:
        return(self.id +","+ self.customer_name+","+self.License_type+","+self.gbp+","+self.bbp+","+self.email+","+self.phone+","+self.address+","+self.Social_security_number)

