




# interface 4
# experiment.py

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

    def prepare_trip(self, trip_instance, mechanic):
        trip_instance.bicycles(mechanic)
        
    def prepare_bicycle(self, bike):
        self.clean_bicycle(bike)
        self.pump_tire(bike)
        self.lube_chain(bike)
        self.check_brakes(bike)

class Trip():
    def __init__(self, bike):
        self.bike = bike
        
    def prepare_trip(self, trip, mechanic_instance):
        mechanic_instance.prepare_trip(trip, mechanic_instance)
        
    def bicycles(self, mechanic_instance):
        mechanic_instance.prepare_bicycle(self.bike)
        


if __name__ == '__main__':
    bike = "my bike"
    mechanic = Mechanic()
    trip = Trip(bike)
    
    # 自分自身とmechanicインスタンスを渡す。
    trip.prepare_trip(trip, mechanic)

# end of line break