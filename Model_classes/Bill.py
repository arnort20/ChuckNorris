class Bill:
    def __init__(self, contract_ID, fetch_date, return_date, location_id,price):
        self.contract_ID = contract_ID
        self.fetch_date = fetch_date
        self.return_date = return_date
        self.location_id = location_id
        price_float = float(price)
        self.price = round(price_float)

    def __str__(self) -> str:
        return (self.contract_ID+','+self.fetch_date+','+self.return_date+','+self.location_id+','+str(self.price))