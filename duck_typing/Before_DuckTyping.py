




# duck_typing 1
# Before_DuckTyping.py

class Trip():
    def __init__(self, bicycles, customer, vehicle):
        self.bicycles = bicycles
        self.customer = customer
        self.vehicle = vehicle
    
    def prepare(self, mechanic):
        mechanic.prepare_bicycles(self.bicycles)

class Mechnic():
    
    def prepare_bicycles(self, bicycles):
        # bicycles and self.prepare_bicycle are used inside.
        pass
    
    def prepare_bicycle(self):
        pass

# end of line break