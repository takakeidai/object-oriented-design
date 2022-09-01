




# module
# first_example.py

import datetime

class Schedule():
    def is_scheduled(self, scheduleable, start_date, end_date):
        print(f"This {scheduleable.__class__.__name__} is not scheduled between {start_date} and {end_date}")
        return True
    
class Bicycle():
    def __init__(self, **kwargs):
        self.schedule = kwargs['schedule'] if 'schedule' in kwargs.keys() else Schedule()
        # and so on...
        
    def is_schedulable(self, start_date, end_date):
        self.is_scheduled(start_date - self.lead_days, end_date)
    
    def is_scheduled(self, start_date, end_date):
        self.schedule.is_scheduled(self,start_date, end_date)        
    
    @property
    def lead_days(self):
        return datetime.timedelta(days=1)
    
if __name__ == '__main__':
    start_date = datetime.date(2015, 9, 4)
    end_date = datetime.date(2015, 9, 10)
    
    b = Bicycle()
    b.is_schedulable(start_date, end_date)

# end of line break