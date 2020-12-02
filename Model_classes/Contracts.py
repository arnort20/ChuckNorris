class Contract(object):
    def __init__(self,ID,employee_id,costumer_id,vehicle_id,start_date,end_date,paid) -> None:
        self.id = ID
        self.employee_id = employee_id
        self.costumer_id = costumer_id
        self.vehicle_id = vehicle_id
        self.start_date = start_date
        self.end_date = end_date
        self.paid = paid

    def __str__(self) -> str:
        pass
