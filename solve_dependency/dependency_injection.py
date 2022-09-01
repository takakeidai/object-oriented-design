




# solve_dependency 3
# dependency_injection.py

#外部のクラスへの参照の分離・隔離
# GearとWheelの依存関係を解決する。
# wheelと結合する代わりに初期化の際にdiameterに応答できるオブジェクトを要求する

class Wheel():
    def __init__(self, rim, tire):
        self.rim = rim
        self.tire = tire
    
    @property
    def diamater(self):
        diamater = self.rim + (self.tire *2)
        return diamater


class Gear_Bad():
    def __init__(self, chainring, cog, rim, tire):
        self.chainring = chainring
        self.cog = cog
        self.rim = rim
        self.tire = tire
    
    def ratio(self):
        ratio = self.chainring / self.cog
        return ratio
    
    # gear_inchesメソッドないで、他のクラスが固定的に使われてしまっている。
    # Gearクラスは、Wheelクラスの名前や引数、その順番まで知っていなければ動かない。
    def gear_inches(self):
        inche = self.ratio() * Wheel(self.rim, self.tire).diamater
        return inche


# Best Practice : 依存の分離
class Gear():
    def __init__(self, chainring, cog, wheel):
        self.chainring = chainring
        self.cog = cog
        self.wheel = wheel
    
    @property
    def ratio(self):
        ratio = self.chainring / self.cog
        return ratio
    
    # このように最低、クラスを使わずに、gearインスタンス生成時にオブジェクトを渡すようなコードを書く
    # 以前のGearはWheelクラスに対して明示的に依存しており、初期化に使う引数の型や順番にも依存していた。  
    def gear_inches(self):
        inche = self.ratio * self.wheel.diamater
        return inche


# 依存の隔離
class Gear_2():
    def __init__(self, chainring, cog, rim, tire):
        self.chainring = chainring
        self.cog = cog
        self.rim = rim
        self.tire = tire
 
    #どうしてもWheelクラスを内部で使わなければいけない場合は、
    # Wheelクラスのインスタンス生成を分離する。
    # これにより、Wheelクラスへの変更が発生してもここだけ変更すれば良いことになる。
    @property
    def wheel(self):
        wheel = Wheel(self.rim, self.tire)
        return wheel
    
    def ratio(self):
        ratio = self.chainring / self.cog
        return ratio
    
    # このように最低、クラスを使わずに、gearインスタンス生成時にオブジェクトを渡すようなコードを書く
    # 以前のGearはWheelクラスに対して明示的に依存しており、初期化に使う引数の型や順番にも依存していた。  
    def gear_inches(self):
        inche = self.ratio() * self.wheel.diamater
        return inche
    
    
if __name__ == '__main__':
    
    gear = Gear(52, 11, Wheel(26, 1.5))
    print(gear.gear_inches())

# end of line break