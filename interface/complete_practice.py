




# interface 5
# complete_parctice.py

class Customer():
    def __init__(self, on_date, of_difficulty, need_bike, trip_finder):
        self.on_date = on_date
        self.of_difficulty = of_difficulty
        self.need_bike = need_bike
        self.trip_finder = trip_finder
        
    def suitable_trips(self):
        self.trip_finder.suitable_trips(self.on_date, self.of_difficulty, self.need_bike)


class TripFinder():
    def __init__(self, trip, bicycle, route_types):
        self.trip = trip
        self.bicycle = bicycle
        self.route_types = route_types
        
    def suitable_trips(self, on_date, of_difficulty, need_bike):
        found_trip = self.trip.suitable_trips(on_date, of_difficulty)
        if not need_bike:
            return found_trip
        
        route_type = self.route_types[of_difficulty]
        found_bicycle = self.bicycle.suitable_bicycle(on_date, route_type)
        return {**found_trip, **found_bicycle}
        
        
class Trip():
    def __init__(self, bike, mechanic, spots):
        self.bike = bike
        self.mechanic = mechanic
        self.spots = spots
        
    def suitable_tirps(self, on_date, of_difficulty):
        spot = self.spots[of_difficulty]
        trip_suggestion = {"spot":spot, "date":on_date, "difficulty":of_difficulty }
        return trip_suggestion
            
    def prepare_trip(self, trip):
        self.mechanic.prepare_trip(trip)
        
    def bicycles(self):
        self.mechanic.prepare_bicycle(self.bike)


class Bicycle():
    def __init__(self, bicycles_list):
        self.bicycles_list = bicycles_list
        #{"date_1":[bicycle_a, bicycle_b], "date_2":[bicycle_b, bicycle_c]}
    
    def data_structure(self, trip_date):
        if len(self.bicycles_list[trip_date]) == 0:
            return None
        
        return self.bicycles_list[trip_date][0]

    def suitable_bicycle(self, trip_date, route_type):
        if not self.data_structure(trip_date):
            return None
        return {"bicycle":self.data_structure(trip_date), "route_type":route_type}
            
            
class Mechanic():
            
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

        
if __name__ == '__main__':
    spot = 'karuizawa'
    mechanic = 'mechanic'
    trip = 'trip'
    route_type = 'difficult'
    bike_list = ['bike_a', 'bike_b']
    bike  = Bicycle(bike_list)
    trip = Trip(bike, mechanic, spot)
    trip_finder = TripFinder(trip, spot, route_type)
    customer = Customer("5/2", 1, True, trip_finder)
    
# end of line break