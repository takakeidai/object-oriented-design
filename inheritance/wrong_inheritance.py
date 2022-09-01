




# inheritance 3
# wrong_inheritance.py


# 問題ありのコード
# 単にBicycleクラスの性質をMountainBikeクラスが継承しても、余計なものがついてくる。
# 間違ったtire_sizeや、MountainBikeクラスに必要とされていないtape_colorまで継承してしまうことになる。
# これはつまり、マウンテンバイクのインスタンスがロードバイクとマウンテンバイクの振る舞いをごっちゃまぜに含んでしまっていることになる。
# 問題の原因は、Bicycleクラスにそもそもロードバイクの性質を持たせてしまっていて、他のクラスに正しく継承される形になっていないこと。
# つまり、現時点でのBicycleクラスは、一般の自転車という概念と、ロードバイクの概念を混ぜ合わせたものになってしまっている。

class Bicycle():
    def __init__(self, **kwargs):
        self.size = kwargs["size"] if "size" in kwargs.keys() else None
        self.tape_color = kwargs["tape_color"] if "tape_color" in kwargs.keys() else None
    
    @property
    def spares(self):
        spares_detail = {
            "chain": "10-speed",
            "tire_size":23,
            "tape_color":self.tape_color
        }
        return spares_detail
    
class MounatainBike(Bicycle):
    def __init__(self, **kwargs):
        self.front_shock = kwargs['front_shock'] if "front_shock" in kwargs.keys() else None
        self.rear_shock = kwargs['rear_shock'] if "rear_shock" in kwargs.keys() else None
        super().__init__(**kwargs)
        
        
    @property
    def spares(self):
        parerent_dict = super().spares
        child_dict = {"front_shock": self.front_shock,"rear_shock": self.rear_shock}
        spares_detail = {**parerent_dict, **child_dict}
        return spares_detail
    
    


if __name__ == '__main__':
    mountain_bike = MounatainBike(
        size = "S",
        front_shock = "Manitou",
        rear_shock = "FOX"
    )
    
    print(mountain_bike.size)
    print(mountain_bike.spares)
    
# end of line break