




# inheritance 4
# correct_inheritance.py

class Bicycle():
    def __init__(self, **kwargs):
        self.size = kwargs['size'] if 'size' in kwargs.keys() else None
        self.chain = kwargs['chain'] if 'chain' in kwargs.keys() else self.default_chain
        self.tire_size = kwargs['tire_size'] if 'tire_size' in kwargs.keys() else self.default_tire_size
    
    # hard cording in chain and tire_size should be changed
    @property
    def default_chain(self):
        return '10-speed'
    
    # これは、自分的には完璧な実装方法。
    # 内部でself.default_tire_sizeが呼び出されているが、
    # このselfはRoadBikeやMountainBikeのインスタンスのことで、それぞれのクラスでdefault_tire_sizeを実装すれば、うまく動く。
    # これにより、それぞれのクラスのデフォルト値が実装できる。
    @property
    def default_tire_size(self):
        if 'default_tire_size' in dir(self):
            print(f"This {self.__class__} connot respond to default_tire_size")
            raise NotImplementedError
        
        return self.default_tire_size
    
    
    # sparsesメソッドの2つの実装方法。
    # 1つ目は簡単だが、結合度が高く、2つ目は複雑だが、強固。
    @property
    def spares(self):
        spares_dict = dict(tire_size = self.tire_size, chain = self.chain)
        return spares_dict
        

class RoadBike(Bicycle):
    def __init__(self, **kwargs):
        self.tape_color = kwargs['tape_color']
        super().__init__(**kwargs)
    
    @property
    def default_tire_size(self):
        return '23'
    
    @property
    def spares(self):
        parerent_dict = super().spares
        child_dict = {"tape_color": self.tape_color}
        spares_detail = {**parerent_dict, **child_dict}
        return spares_detail



class MountainBike(Bicycle):
    def __init__(self, **kwargs):
        self.front_shock = kwargs['front_shock']
        self.rear_shock = kwargs['rear_shock']
        super().__init__(**kwargs)
        
    @property
    def default_tire_size(self):
        return '2.1'
    
    @property
    def spares(self):
        parerent_dict = super().spares
        child_dict = {"front_shock": self.front_shock,"rear_shock": self.rear_shock}
        spares_detail = {**parerent_dict, **child_dict}
        return spares_detail


class RecumbentBike(Bicycle):
    def __init__(self, **kwargs):
        self.flag = kwargs['flag']
        super().__init__(**kwargs)

    @property
    def spares(self):
        parerent_dict = super().spares
        child_dict = {"flag":self.flag}
        spares_detail = {**parerent_dict, **child_dict}
        return spares_detail
        
    
    @property
    def default_chain(self):
        return '9-speed'
    
    @property
    def default_tire_size(self):
        return '28'


if __name__ == '__main__':
    road_bike = RoadBike(
        size = 'M',
        tape_color = 'red'
    )
    print(road_bike.tire_size)
    print(road_bike.chain)
    print(road_bike.spares)
    
    mountain_bike = MountainBike(
        size = 'S',
        front_shock = 'Manitou',
        rear_shock = 'FOX'
    )
    print(mountain_bike.tire_size)
    print(mountain_bike.chain)
    print(mountain_bike.spares)
    
    bent = RecumbentBike(flag = 'tall and orange')
    print(bent.spares)
    
    print(dir(road_bike))
    print(road_bike.__dict__)
    print(road_bike)

# end of line break