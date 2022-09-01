




# pattern2_use_classmethod
# schedule.py

class Schedule():
    def is_scheduled(self, scheduleable, start_date, end_date):
        print(f"This {scheduleable.__class__.__name__} is not scheduled between {start_date} and {end_date}")
        return True
    
# end of line break