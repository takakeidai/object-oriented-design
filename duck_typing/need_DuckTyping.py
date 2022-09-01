




# duck_typing 2
# need_DuckTyping.py

class Trip():
    def __init__(self, bicycles, customer, vehicle):
        self.bicycles = bicycles
        self.customer = customer
        self.vehicle = vehicle
    
    def prepare(self, preparers):
        if isinstance(preparers, Mechanic):
            preparers.prepare_bicycles(self.bicycles)
        elif isinstance(preparers, TripCoordinator):
            preparers.buy_food(self.customer)
        elif isinstance(preparers, Driver):
            preparers.gas_up(self.vehicle)
            preparers.fill_water_tank(self.vehicle)
                

class Mechanic():
    
    def prepare_bicycles(self, bicycles):
        # bicycles and self.prepare_bicycle are used inside.
        pass
    
    def prepare_bicycle(self):
        pass
    
    
class TripCoordinator():
    def buy_food(self, customer):
        pass
    
class Driver():
    def gas_up(self, vehicle):
        pass
    
    def fill_water_tank(self, vehicle):
        pass
    
# end of line break