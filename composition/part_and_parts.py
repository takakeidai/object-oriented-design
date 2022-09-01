




# composition 2
# part_and_parts.py

class Bicycle():
    def __init__(self, **kwargs):
        self.size = kwargs['size'] if 'size' in kwargs.keys() else None
        self.parts = kwargs['parts']

    def spares(self):
        result_dict = self.parts.spares()
        return result_dict
      
class Parts():
    def __init__(self, parts):
        self.parts = parts
    
    def spares(self):  
        # result = []
        # for k in self.parts:
        #     if k.needs_spare:
        #         result.append(k.__dict__)
        #     else:
        #         pass
        # return result
        
        result = [k.__dict__ for k in self.parts if k.needs_spare]
        return result

class Part():
    def __init__(self, needs_spare = True, **kwargs):
        self.name = kwargs['name']
        self.description = kwargs['description']
        self.needs_spare = needs_spare
        

if __name__ == '__main__':
    chain = Part(
        name = 'chain',
        description = '10-speed'
    )
    
    road_tire = Part(
        name = 'tire_size',
        description = '23'
    )
    
    tape = Part(
        name = 'tape_color',
        description = 'red'
    )
    
    mountain_tire = Part(
        name = 'rear_shock',
        description = '2.1'
    )
    
    rear_shock = Part(
        name = 'rear_shock',
        description = 'Fox'
    )
    
    front_shock = Part(
        name = 'front_shock',
        description = 'Manitou',
        needs_spare=False
    )
    
    road_bike_parts = Parts(
        [chain, road_tire, tape]
    )
    
    road_bike = Bicycle(
        size = 'L',
        # 委譲：Bicycleクラスは、Partsクラスを明示的に知っていて、引数として受け取らなければならない。
        parts = Parts(
            [chain,
             road_tire,
             tape]
        ))
    
    print(road_bike.size)
    print(road_bike.spares())
    
    mountain_bike = Bicycle(
        size = 'L',
        # 委譲：Bicycleクラスは、Partsクラスを明示的に知っていて、引数として受け取らなければならない。
        parts = Parts(
            [chain,
             mountain_tire,
             front_shock,
             rear_shock]
        )
    )
    print(mountain_bike.size)
    print(mountain_bike.spares())
    
# end of line break