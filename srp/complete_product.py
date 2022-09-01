




# srp 4
# complete_product.py

import math

class Gear():
    
    def __init__(self, chainring, cog, wheel):
        self.chainring = chainring
        self.cog = cog
        self.wheel = wheel
    
    def ratio(self):
        ratio = self.chainring / self.cog
        return ratio
    
    def gear_inches(self):
        inche = self.ratio() * self.wheel.diamater
        return inche
    

class Wheel():

    def __init__(self, rim, tire):
        self.rim = rim
        self.tire = tire
        
    @property
    def diamater(self):
        diamater = self.rim + (self.tire * 2)
        return diamater
    
    # もしもdiamatersメソッドを加えるならば、Dataクラスを定義してデータ構造を隠蔽して実装するべき。
    # def diamaters(self):
    #         pass
        
    def circumference(self):
        circumference = self.diamater * math.pi
        return circumference
    

if __name__ == '__main__':
    
    wheel = Wheel(26, 1.5)
    print(wheel.circumference())
    
    gear = Gear(52, 11, wheel)
    print(gear.ratio())
    print(gear.gear_inches())

# end of line break