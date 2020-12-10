class Contract(object):
    def __init__(self,ident,employee_id,customer_id,vehicle_id,destination_id,start_date,end_date,paid,day_made) -> None:
        self.id = ident
        self.employee_id = employee_id
        self.customer_id = customer_id
        self.vehicle_id = vehicle_id
        self.start_date = start_date
        self.destination_id = destination_id
        self.end_date = end_date
        self.paid = paid
        self.day_made = day_made
    def __str__(self) -> str:
        return (self.id +","+ self.employee_id+","+self.customer_id+","+self.vehicle_id+","+self.destination_id+","+self.start_date+","+self.end_date+","+self.paid+","+self.day_made)
