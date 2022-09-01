




# pattern1_divide_module
# schedulable.py

import datetime
from schedule import Schedule

class Schedulable():
    def __init__(self, target_obj):
        self.schedule = Schedule()
        self.target_obj = target_obj
             
    def is_schedulable(self, start_date, end_date):
        self.is_scheduled(start_date - self.lead_days, end_date)
    
    def is_scheduled(self, start_date, end_date):
        self.schedule.is_scheduled(self.target_obj,start_date, end_date)        
    
    @property
    def lead_days(self):
        if self.target_obj.lead_days is None:
            return datetime.timedelta(days=0)
        return self.target_obj.lead_days

# end of line break