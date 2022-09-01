




# pattern1_divide_module
# bicycle.py

import datetime
from schedulable import Schedulable

class Bicycle():
    @property
    def lead_days(self):
        return datetime.timedelta(days=1)
    

if __name__ == '__main__':
    start_date = datetime.date(2015, 9, 4)
    end_date = datetime.date(2015, 9, 10)
    
    b = Bicycle()
    s = Schedulable(b)
    s.is_schedulable(start_date, end_date)

# end of line break