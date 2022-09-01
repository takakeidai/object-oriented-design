




# inherface 2
# bad_2.py

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
        
    def prepare_bicycle(self, bike):
        self.clean_bicycle(bike)
        self.pump_tire(bike)
        self.lube_chain(bike)
        self.check_brakes(bike)
        

class Trip():
    def __init__(self, bike, mechanic):
        self.bike = bike
        self.mechanic = mechanic
    
    def bicycles(self):
        print("start trip with bicycles")
        
    def prepare_bicycle(self):
        self.mechanic.prepare_bicycle(self.bike)
        

if __name__ == '__main__':
    mechanic = Mechanic()
    bike = 'my bike'
    trip = Trip(bike, mechanic)
    trip.prepare_bicycle()

# end of line break