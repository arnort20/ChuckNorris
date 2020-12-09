from Data_classes.DataAPI import DataAPI as dAPI
import datetime
class Bill_logic:
    def __init__(self):
        self.dAPI = dAPI()

    def get_bill(self, contract_ID):
        #calls on data to fetch a bill
        bill = self.dAPI.get_bill(contract_ID)
        return bill
    
    def get_all_bills(self):
        #calls on data to fetch all the bills
        return self.dAPI.get_bills()

    def filter_earnings(self, location_id, min_date, max_date):
        """
        finds all bills that fit the input parameters
        returns the total money earned by the location
        in the
        """
        bills = self.dAPI.get_bills()
        date_from = self.convert_date(min_date)
        date_to = self.convert_date(max_date)
        locations_bills = []
        filtered_bills = []
        for bill in bills:
            if bill.location_id == location_id:
                locations_bills.append(bill)
        for bill in locations_bills:
            money_day = self.convert_date(bill.return_date)
            if money_day > date_from and date_to > money_day:
                filtered_bills.append(bill)
        laundered_money = 0
        for bill in filtered_bills:
            laundered_money += float(bill.price)
        return int(laundered_money)


    def new_bill(self, contract_ID, fetch_date, return_date, gbp_used):
        contract = self.dAPI.get_contract(contract_ID)
        vehicle = self.dAPI.get_vehicle(contract.vehicle_id)
        customer = self.dAPI.get_customer(contract.customer_id)
        location_id = contract.destination_id
        tax = vehicle.tax

        #would you like to use your loyalty points?
        gbp_available = customer.gbp
        if gbp_used == True:
            gbp = gbp_available
        else:
            gbp = 0

        #date calculations part
        start_date = self.convert_date(contract.start_date)      
        end_date = self.convert_date(contract.end_date)
        date_retuned = self.convert_date(return_date)
        contract_period = end_date - start_date
        true_period = date_retuned - start_date
        if true_period > contract_period:
            late_tax = 20
            days = true_period
        else:
            late_tax = 0
            days = contract_period

        #KA-CHING!
        price = self.calculate_price(tax, gbp, days, late_tax)
        self.dAPI.add_bill(contract_ID, fetch_date, return_date, location_id, price)

        #mark the car as returned
        self.dAPI.change_vehicle(contract.vehicle_id,{"available":"yes"}) 

        #add BBP to the customer if they returned late
        if late_tax > 0:
            new_BBP = customer.bbp + 1
            self.dAPI.change_Customer(customer.id,{"bbp":str(new_BBP)})
        


    def calculate_price(self, tax, gbp_discount, days, late_tax):
        car_tax = int(tax)
        gbp = int(gbp_discount)*1000
        basecost = days.days*10000
        modified_cost = basecost*(1+(car_tax+late_tax)/100)-gbp
        return modified_cost
        
    
    def convert_date(self, date_string):
        year, month, day = str(date_string).split('.')
        date_format = datetime.date(int(year), int(month), int(day))
        return date_format


    


#RIP
    # def get_bill_info(self, contract_ID):
    #     fined = bool(False)
    #     #decompresses all the information contained within the contract
    #     #returns a dictionary containing ALL information regarding a contract
    #     contract = self.dAPI.get_contract(contract_ID)
    #     vehicle = self.dAPI.get_vehicle(contract.vehicle_id)
    #     the_bill = self.dAPI.get_bill(contract_ID)
    #     employee = self.dAPI.get_employee(contract.employee_id)
    #     customer = self.dAPI.get_customer(contract.customer_id)
    #     bill_dictionary = {}

    #     #contract information
    #     start_date = self.convert_date(contract.start_date)
    #     bill_dictionary["start_date"] = str(start_date)
    #     end_date = self.convert_date(contract.end_date)
    #     bill_dictionary["end_date"] = str(end_date)

    #     #bill information
    #     bill_dictionary["gbp_used"] = the_bill["gbp_used"]
    #     bill_dictionary["gbp_discount"] = int(the_bill["gbp_used"])*1000
    #     fetch_date = self.convert_date(the_bill["fetch_date"])
    #     bill_dictionary["fetch_date"] = str(fetch_date)
    #     ret_date = self.convert_date(the_bill["return_date"])
    #     bill_dictionary["return_date"] = str(ret_date)
    #     contract_period = end_date - start_date
    #     bill_dictionary["contract_period"] = contract_period.days
    #     true_period = ret_date - start_date
    #     bill_dictionary["true_period"] = true_period.days
    #     if true_period > contract_period:
    #         fined = bool(True)
    #     bill_dictionary["late_tax"] = fined


    #     #vehicle information
    #     bill_dictionary["vehicle_id"] = vehicle.id
    #     bill_dictionary["vehicle_name"] = vehicle.vehicle_name
    #     bill_dictionary["vehicle_type"] = vehicle.type
    #     bill_dictionary["vehicle_manufacturer"] = vehicle.manufacturer
    #     bill_dictionary["vehicle_model"] = vehicle.model
    #     bill_dictionary["vehicle_color"] = vehicle.color
    #     bill_dictionary["vehicle_age"] = vehicle.age
    #     bill_dictionary["tax"] = vehicle.tax


    #     #employee information
    #     bill_dictionary["employee_id"] = employee.id
    #     bill_dictionary["employee_name"] = employee.employee_name
    #     bill_dictionary["employee_ssn"] = employee.ssn
    #     bill_dictionary["employee_address"] = employee.address
    #     bill_dictionary["employee_phone"] = employee.phone
    #     bill_dictionary["employee_email"] = employee.email


    #     #customer information
    #     bill_dictionary["customer_id"] = customer.id
    #     bill_dictionary["customer_name"] = customer.customer_name
    #     bill_dictionary["customer_license"] = customer.License_type
    #     bill_dictionary["customer_email"] = customer.email
    #     bill_dictionary["customer_phone"] = customer.phone
    #     bill_dictionary["customer_address"] = customer.address

    #     return bill_dictionary



