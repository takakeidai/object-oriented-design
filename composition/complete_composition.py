




# compositon 3
# complete_composition.py

class Bicycle():
    def __init__(self, **kwargs):
        self.size = kwargs['size'] if 'size' in kwargs.keys() else None
        self.parts = kwargs['parts']
    
    @property
    def spares(self):
        result = self.parts.spares()
        return result

class Part():
    def __init__(self, need_spapre = True, **kwargs):
        self.name = kwargs['name']
        self.description  = kwargs['description']
        self.needs_spare = need_spapre


class Parts():
    def __init__(self, parts):
        self.parts = parts
    
    def spares(self):  
        result = [k.__dict__ for k in self.parts if k.needs_spare]
        return result
    
    
class PartsFactory():
    @classmethod
    def build(cls, config, parts_class=Parts):
        index = 0
        len_num = len(config)
        parts_list = []
        def create_part(config_list):
            part_class = Part(
                name = config_list[0],
                description = config_list[1]
                #needs_spare = config_list[2] if config_list[2] in config_list else True
            )
            return part_class
        
        while index < len_num:
            parts_list.append(create_part(config[index]))
            index += 1
        return parts_class(parts_list)
    

if __name__ == '__main__':
    
    road_config = [
        ['chain', '10-speed'],
        ['tire_size', '23'],
        ['tape_color', 'red']
    ]
    
    mountain_config = [
        ['chain', '10-speed'],
        ['tire_size', '2.1'],
        ['front_shock', 'Manitou', False],
        ['rear_shock', 'Fox']
    ]
    road_bike = Bicycle(
        size = 'L',
        parts = PartsFactory.build(road_config)        
    )
    
    print(road_bike.spares)
    
    mountain_bike = Bicycle(
        size = 'L',
        parts = PartsFactory.build(mountain_config)
    )
    
    print(mountain_bike.spares)
    
    recumbent_config = [
        ['chain', '9-speed'],
        ['tire_size', '28'],
        ['flag', 'tall and orange']
    ]
    
    recumbent_bike = Bicycle(
        size = 'L',
        parts = PartsFactory.build(recumbent_config)
    )
    
    print(recumbent_bike.spares)
    
# end of line break