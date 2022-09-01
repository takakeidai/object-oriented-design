




# composition 1
# basic_composition.py

class Bicycle():
    def __init__(self, **kwargs):
        self.size = kwargs['size'] if 'size' in kwargs.keys() else None
        self.parts = kwargs['parts'] if 'parts' in kwargs.keys() else Parts()

    def spares(self):
        result_dict = self.parts.spares()
        return result_dict

class Parts():
    def __init__(self, **kwargs):
        self.chain = kwargs['chain'] if 'chain' in kwargs.keys() else self.default_chain
        self.tire_size = kwargs['tire_size'] if 'tire_size' in kwargs.keys() else self.default_tire_size
    
    def spares(self):
        spares_dict = dict(tire_size = self.tire_size, chain = self.chain)
        return spares_dict
        
    @property
    def default_tire_size(self):
        if 'default_tire_size' in dir(self):
            print(f"This {self.__class__} connot respond to default_tire_size")
            raise NotImplementedError
        
        return self.default_tire_size    
    
    @property
    def default_chain(self):
        return '10-speed'        
    
    @property
    def local_spares(self):
        return {}
    
    
class RoadBikeParts(Parts):
    def __init__(self, **kwargs):
        self.tape_color = kwargs['tape_color']
        super().__init__(**kwargs)
    
    @property
    def default_tire_size(self):
        return '23'


class MountainBikeParts(Parts):
    def __init__(self, **kwargs):
        self.front_shock = kwargs['front_shock'] 
        self.rear_shock = kwargs['rear_shock']
        super().__init__(**kwargs)
        
    @property
    def default_tire_size(self):
        return '2.1'
    

if __name__ == "__main__":
    road_bike = Bicycle(
        size = 'M', 
        parts = RoadBikeParts(tape_color = 'red')
        )
    
    print(road_bike.size)
    print(road_bike.spares())
    
    mountain_bike = Bicycle(
        size = 'L',
        parts = MountainBikeParts(front_shock = 'Manitou',rear_shock = 'Fox')
    )
    print(mountain_bike.size)
    print(mountain_bike.spares())
    
# end of line break