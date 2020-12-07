from Data_classes.DataAPI import DataAPI as dAPI
import datetime
class Bill:
    def __init__(self):
        self.dAPI = dAPI()

    def new_bill(self, contract_ID, return_date, gbp_used):
        self.dAPI.add_bill(contract_ID, return_date, gbp_used)

    def calculate_price(self, bill_dictionary):
        pass
        

    def get_bill_info(self, contract_ID):
        fined = "o"
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
        ret_date = self.convert_date(the_bill["return_date"])
        bill_dictionary["return_date"] = str(ret_date)
        contract_period = end_date - start_date
        bill_dictionary["contract_period"] = str(contract_period)
        true_period = ret_date - start_date
        bill_dictionary["true_period"] = str(true_period)
        # if true_period > contract_period:
        #     fined = "x"
        # bill_dictionary["penalty":fined]


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

