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
        in the timeframe given, returns an int
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
            if self.check_date_clash(money_day, money_day, date_from, date_to):
                filtered_bills.append(bill)
        laundered_money = 0
        for bill in filtered_bills:
            laundered_money += float(bill.price)
        return int(laundered_money)

    def handoff_vehicle(self, contract_ID, fetch_date):
        """
        the whole proccess from when the vehicle is handed over
        """
        contract = self.dAPI.get_contract(contract_ID)
        vehicle = self.dAPI.get_vehicle(contract.vehicle_id)
        #the car becomes unavailable
        self.dAPI.change_vehicle(vehicle.id,{"available":"no"})
        #the date picked up gets registered in the database
        #and an unfilled bill gets made
        self.dAPI.add_bill(contract_ID, fetch_date, "not returned", contract.destination_id, 0)

    def recieve_vehicle(self, contract_ID, return_date, gbp_used):
        """
        the whole proccess from when the vehicle gets returned
        """
        contract = self.dAPI.get_contract(contract_ID)
        vehicle = self.dAPI.get_vehicle(contract.vehicle_id)
        customer = self.dAPI.get_customer(contract.customer_id)
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
            #20% increase to price and the amount of days rented becomes the 
            #time the customer had the vehicle
            late_tax = 20
            days = true_period
        else:
            late_tax = 0
            days = contract_period

        #KA-CHING!
        price = self.calculate_price(tax, gbp, days, late_tax)
        self.dAPI.change_Bill(contract_ID, {"return_date":return_date,"price":price})

        #mark the car as returned
        self.dAPI.change_vehicle(contract.vehicle_id,{"available":"yes"}) 

        #add BBP to the customer if they returned late
        if late_tax > 0:
            new_BBP = customer.bbp + 1
            self.dAPI.change_Customer(customer.id,{"bbp":str(new_BBP)})
        


    def calculate_price(self, tax, gbp_discount, days, late_tax):
        #takes the amount of days as a timedelta object
        car_tax = int(tax)
        gbp = int(gbp_discount)*1000
        basecost = days.days*10000
        #car tax is a percentage increase in the base price
        modified_cost = basecost*(1+(car_tax+late_tax)/100)-gbp
        #returns a float
        return modified_cost
        
    
    def convert_date(self, date_string):
        year, month, day = str(date_string).split('.')
        date_format = datetime.date(int(year), int(month), int(day))
        return date_format

    def check_date_clash(self, date1_start, date1_end, date2_start, date2_end):
        """
        takes four datetime objects and checks if there's any overlap
        to check if one day is in a span of time, insert date1_start = date1_end
        returns true if there is a clash
        """
        if ((date2_start > date1_start and date2_start < date1_end)or(date2_end > date1_start and date2_end < date1_end)):
            return True
        elif ((date1_start > date2_start and date1_start < date2_end)or(date1_end > date2_start and date1_end < date2_end)):
            return True
        else:
            return False

    def get_vehicle_tax(self, vehicle_id):
        pass




