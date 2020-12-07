from Data_classes.DataAPI import DataAPI as dAPI
import datetime
class Bill:
    def __init__(self):
        self.dAPI = dAPI()

    def new_bill(self, contract_ID, return_date, gbp_used):
        self.dAPI.add_bill(contract_ID, return_date, gbp)

    def calculate_price(self, contract_obj):
        
        if true_period > contract_period:
            rented_period = true_period
            fined = True
        else: 
            rented_period = contract_period
        baseprice = rented_period.days * 1000
        if fined:
            punishment = 20
        else:
            punishment = 1
        with_tax = baseprice*(vehi_tax/100)+baseprice*(punishment/100)

    def get_bill_info(self, contract_ID):
        fined = False
        #decompresses all the information contained within the contract
        contract = self.dAPI.get_contract(contract_ID)
        vehicle = self.dAPI.get_vehicle(contract.vehicle_id)
        the_bill = self.dAPI.get_bill(contract_ID)
        employee = self.dAPI.get_employee(contract.employee_id)
        customer = self.dAPI.get_customer(contract.customer_id)

        return_date = the_bill["return_date"]

        vehi_tax = vehicle.tax
        start_date = self.convert_date(contract.start_date)
        end_date = self.convert_date(contract.end_date)
        ret_date = self.convert_date(return_date)
        gbp_discount = the_bill["gbp"]
        contract_period = end_date - start_date
        true_period = ret_date - start_date
        if true_period > contract_period:
            fined = True
        bill_dict = {"vehicle":vehicle, "tax":}
        
        



    def convert_date(self, date_string):
        year, month, day = str(date_string).split('.')
        date_format = datetime.date(year, month, day)
        return date_format

