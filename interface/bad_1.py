




# interface 1
# bad_1.py

class Mechanic():
    def __init__(self):
        pass
            
    def clean_bicycle(self, bike):
        print(f"clean bicycle for {bike}")
        
    def pump_tire(self, bike):
        print(f"pump tires of {bike}")
        
    def lube_chain(self, bike):
        print(f"lube chain of {bike}")
        
    def check_brakes(self, bike):
        print(f"check brakes of {bike}")
        

class Trip():
    def __init__(self, bike):
        self.bike = bike
    
    def bicycles(self):
        print("start trip with bicycles")
        
    def clean_bicycle(self):
        mechanic = Mechanic()
        mechanic.clean_bicycle(self.bike)
        
    def pump_tire(self):
        mechanic = Mechanic()
        mechanic.pump_tire(self.bike)
        
    def lube_chain(self):
        mechanic = Mechanic()
        mechanic.lube_chain(self.bike)
        
    def check_brakes(self):
        mechanic = Mechanic()
        mechanic.check_brakes(self.bike)
        
# end of line break
