class Customer(object):
    def __init__(self,ident,Customer_name,email,phone,address,License_type,gbp,bbp) -> None:
        self.id = ident
        self.costumer_name = Customer_name
        self.License_type = License_type
        self.gbp = gbp
        self.gbp = bbp
        self.email = email
        self.phone = phone
        self.address = address

    def __str__(self) -> str:
        pass
