




# extension_pattern2
# method_set.py

import datetime
from schedule import Schedule

class MethodSet():
    schedule = Schedule()
    @classmethod
    def is_schedulable(cls, obj, lead_days, start_date, end_date):
        if lead_days is None:
            cls.is_scheduled(obj, start_date - cls.lead_days, end_date)
            
        cls.is_scheduled(obj, start_date - lead_days, end_date)
    
    @classmethod
    def is_scheduled(cls, obj,start_date, end_date):
        cls.schedule.is_scheduled(obj, start_date, end_date)        
    
    @property
    def lead_days(cls):
        return datetime.timedelta(days=0)

# end of line break
    
