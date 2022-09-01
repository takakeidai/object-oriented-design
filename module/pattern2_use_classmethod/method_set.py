




# pattern2_use_classmethod
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
    
    
class Bicycle():
    @property
    def lead_days(self):
        return datetime.timedelta(days=1)
    
    def is_schedulable(self, start_date, end_date):
        MethodSet.is_schedulable(self, self.lead_days, start_date, end_date)
        
        
if __name__ == '__main__':
    start_date = datetime.date(2015, 9, 4)
    end_date = datetime.date(2015, 9, 10)
    
    b = Bicycle()
    b.is_schedulable(start_date, end_date)

# end of line break