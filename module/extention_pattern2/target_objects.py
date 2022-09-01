




# extension_pattern2
# target_objects.py

import datetime
from method_set import MethodSet

class Bicycle():
    @property
    def lead_days(self):
        return datetime.timedelta(days=1)
    
    def is_schedulable(self, start_date, end_date):
        MethodSet.is_schedulable(self, self.lead_days, start_date, end_date)

class Vehicle():
    @property
    def lead_days(self):
        return datetime.timedelta(days=3)
    
    def is_schedulable(self, start_date, end_date):
        MethodSet.is_schedulable(self, self.lead_days, start_date, end_date)
        
class Mechanic():
    @property
    def lead_days(self):
        return datetime.timedelta(days=4)
    
    def is_schedulable(self, start_date, end_date):
        MethodSet.is_schedulable(self, self.lead_days, start_date, end_date)
    
if __name__ == '__main__':
    start_date = datetime.date(2015, 9, 4)
    end_date = datetime.date(2015, 9, 10)
    
    b = Bicycle()
    b.is_schedulable(start_date, end_date)
    
    v = Vehicle()
    v.is_schedulable(start_date, end_date)
    
    m = Mechanic()
    m.is_schedulable(start_date, end_date)

# end of line break