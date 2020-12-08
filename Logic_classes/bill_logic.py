from Data_classes.DataAPI import DataAPI as dAPI
import datetime
class Bill_logic:
    def __init__(self, bill_obj):
        self.dAPI = dAPI()
        self.contract = self.dAPI.get_contract(bill_obj.contract_ID)
        self.vehicle = self.dAPI.get_vehicle(self.contract.vehicle_id)
        self.the_bill = self.dAPI.get_bill(bill_obj.contract_ID)
        self.employee = self.dAPI.get_employee(self.contract.employee_id)
        self.customer = self.dAPI.get_customer(self.contract.customer_id)
        
    def new_bill(self, contract_ID, fetch_date, return_date, gbp_used):
        self.dAPI.add_bill(contract_ID, fetch_date, return_date, gbp_used)

    def calculate_price(self, bill_dictionary):
        car_tax = int(bill_dictionary["tax"])
        gbp = bill_dictionary["gbp_discount"]
        if bill_dictionary["late_tax"]:
            basecost = bill_dictionary["true_period"]*10000
            tardy_tax = 20
        else:
            basecost = bill_dictionary["contract_period"]*10000
            tardy_tax = 0
        modified_cost = basecost*(1+(car_tax+tardy_tax)/100)-gbp
        return modified_cost
        

    def get_bill_info(self, contract_ID):
        fined = bool(False)
        #decompresses all the information contained within the contract
        #returns a dictionary containing ALL information regarding a contract
        contract = self.dAPI.get_contract(contract_ID)
        vehicle = self.dAPI.get_vehicle(contract.vehicle_id)
        the_bill = self.dAPI.get_bill(contract_ID)
        employee = self.dAPI.get_employee(contract.employee_id)
        customer = self.dAPI.get_customer(contract.customer_id)
        bill_dictionary = {}

        #contract information
        start_date = self.convert_date(contract.start_date)
        bill_dictionary["start_date"] = str(start_date)
        end_date = self.convert_date(contract.end_date)
        bill_dictionary["end_date"] = str(end_date)

        #bill information
        bill_dictionary["gbp_used"] = the_bill["gbp_used"]
        bill_dictionary["gbp_discount"] = int(the_bill["gbp_used"])*1000
        fetch_date = self.convert_date(the_bill["fetch_date"])
        bill_dictionary["fetch_date"] = str(fetch_date)
        ret_date = self.convert_date(the_bill["return_date"])
        bill_dictionary["return_date"] = str(ret_date)
        contract_period = end_date - start_date
        bill_dictionary["contract_period"] = contract_period.days
        true_period = ret_date - start_date
        bill_dictionary["true_period"] = true_period.days
        if true_period > contract_period:
            fined = bool(True)
        bill_dictionary["late_tax"] = fined


        #vehicle information
        bill_dictionary["vehicle_id"] = vehicle.id
        bill_dictionary["vehicle_name"] = vehicle.vehicle_name
        bill_dictionary["vehicle_type"] = vehicle.type
        bill_dictionary["vehicle_manufacturer"] = vehicle.manufacturer
        bill_dictionary["vehicle_model"] = vehicle.model
        bill_dictionary["vehicle_color"] = vehicle.color
        bill_dictionary["vehicle_age"] = vehicle.age
        bill_dictionary["tax"] = vehicle.tax


        #employee information
        bill_dictionary["employee_id"] = employee.id
        bill_dictionary["employee_name"] = employee.employee_name
        bill_dictionary["employee_ssn"] = employee.ssn
        bill_dictionary["employee_address"] = employee.address
        bill_dictionary["employee_phone"] = employee.phone
        bill_dictionary["employee_email"] = employee.email


        #customer information
        bill_dictionary["customer_id"] = customer.id
        bill_dictionary["customer_name"] = customer.customer_name
        bill_dictionary["customer_license"] = customer.License_type
        bill_dictionary["customer_email"] = customer.email
        bill_dictionary["customer_phone"] = customer.phone
        bill_dictionary["customer_address"] = customer.address

        return bill_dictionary


    def convert_date(self, date_string):
        year, month, day = str(date_string).split('.')
        date_format = datetime.date(int(year), int(month), int(day))
        return date_format

