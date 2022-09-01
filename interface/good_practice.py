




# interface 3
# good_practice.py

class Mechanic():
    def __init__(self):
        #何も特にいらない
        pass
            
    def clean_bicycle(self, bike):
        print(f"clean bicycle for {bike}")
        
    def pump_tire(self, bike):
        print(f"pump tires of {bike}")
        
    def lube_chain(self, bike):
        print(f"lube chain of {bike}")
        
    def check_brakes(self, bike):
        print(f"check brakes of {bike}")

    def prepare_trip(self, trip):
        trip.bicycles()
        
    def prepare_bicycle(self, bike):
        self.clean_bicycle(bike)
        self.pump_tire(bike)
        self.lube_chain(bike)
        self.check_brakes(bike)

class Trip():
    def __init__(self, bike, mechanic):
        self.bike = bike
        self.mechanic = mechanic
        
    def prepare_trip(self, trip):
        self.mechanic.prepare_trip(trip)
        
    def bicycles(self):
        self.mechanic.prepare_bicycle(self.bike)
        


if __name__ == '__main__':
    bike = "my bike"
    mechanic = Mechanic()
    trip = Trip(bike, mechanic)
    
    # 自分自身を引数で渡し、mechanicオブジェクトのメソッドに渡す。
    trip.prepare_trip(trip)
    
# end of line break