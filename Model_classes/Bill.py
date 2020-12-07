class Bill:
    def __init__(self, contract_ID, return_date, gbp_used):
        self.contract_ID = contract_ID
        self.return_date = return_date
        self.gbp = gbp_used
    
    def __str__(self) -> str:
        return (self.contract_ID, self.return_date, self.gbp)