




# solve_dependency 4
# wrapper.py

class Wheel():
    def __init__(self, rim, tire):
        self.rim = rim
        self.tire = tire
    
    @property
    def diamater(self):
        diamater = self.rim + (self.tire *2)
        return diamater

# ここで外部インターフェイスのGearOuterの引数は固定的で変えられないとする。
#　この場合ラッパークラスを作成して、任意の引数の順番を受け付ける新たなオブジェクトを作る。
class GearOuter():
    def __init__(self, chainring, cog, wheel):
        self.chainring = chainring
        self.cog = cog
        self.wheel = wheel

    @property
    def ratio(self):
        ratio = self.chainring / self.cog
        return ratio
     
    def gear_inches(self):
        inche = self.ratio * self.diamater()
        return inche

    def diamater(self):
        return self.wheel.diamater

# ラッパーを作り柔軟性の高いクラスを作る。
class GearWrapper():
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        
    def gear(self):
        return GearOuter(self.kwargs['chainring'], self.kwargs['cog'], self.kwargs['wheel'])
    
if __name__ == '__main__':
    
    gear = GearWrapper(cog = 11, chainring = 52, wheel = Wheel(26, 1.5)).gear()
    print(gear.gear_inches())

# end of line break