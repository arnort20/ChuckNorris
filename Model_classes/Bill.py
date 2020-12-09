class Bill:
    def __init__(self, contract_ID, fetch_date, return_date, gbp_used,location_id,price):
        self.contract_ID = contract_ID
        self.fetch_date = fetch_date
        self.return_date = return_date
        self.gbp = gbp_used
        self.location_id = location_id
        self.price = price

    def __str__(self) -> str:
        return (self.contract_ID, self.fetch_date,self.return_date, self.gbp)