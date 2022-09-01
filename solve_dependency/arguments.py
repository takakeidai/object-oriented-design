




# solve_dependency 1
# arguments.py

# このように**kwargsで可変長引数として引数を取ればどのような順番がどうであれ受け取れる。
class Gear():
    def __init__(self, **kwargs):
        self.chainring = kwargs['chainring']
        self.cog = kwargs['cog']
        self.wheel = kwargs['wheel']
        
    @property
    def ratio(self):
        ratio = self.chainring / self.cog
        return ratio
     
    def gear_inches(self):
        inche = self.ratio * self.diamater()
        return inche

    def diamater(self):
        return self.wheel.diamater


class Wheel():
    def __init__(self, rim, tire):
        self.rim = rim
        self.tire = tire
    
    @property
    def diamater(self):
        diamater = self.rim + (self.tire *2)
        return diamater
       

if __name__ == '__main__':
    gear = Gear(cog=11, chainring=52, wheel=Wheel(26, 1.5))
    print(gear.chainring)
    print(gear.gear_inches())

# end of line break