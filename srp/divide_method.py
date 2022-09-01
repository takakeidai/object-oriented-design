




# srp 1
# divide_method.py

# メソッドにも単一責任の原則を用いる。
# そのメソッドで2つ以上の計算がされていないか、その計算をクラスに含めることは適切か、を考える。

class Gear_Bad():
    def __init__(self, chainring, cog, rim, tire):
        self.chainring = chainring
        self.cog = cog
        self.rim = rim
        self.tire = tire
        
    def ratio(self):
        return self.chainring / self.cog
    
    def gear_inches(self):
        gear_inches = self.ratio() * (self.rim + (self.tire * 2))
        return gear_inches
    
    # gear_inchesメソッドにおいて、(self.rim + (self.tire * 2))はdiamaterの計算になるが、
    # gear_inchesメソッドは、inche計算とdiamater計算の2つの作業をしてしまっていることになるから分離する必要がある。
    # また、このdiamater計算はGearクラスに含めるべきだろうか？
    # これはギアクラスではなくて、車輪クラスを用意してそのオブジェクトをギアクラスに渡すべき。
    

# 良い例
# メソッドにも単一責任を！！
class Gear():
    def __init__(self, chainring, cog, rim, tire, wheel_object):
        self.chainring = chainring
        self.cog = cog
        self.wheel_object = wheel_object
        
    def ratio(self):
        return self.chainring / self.cog
    
    def gear_inches(self):
        # このように別のオブジェクトとしてdiamaterを計算してget_inchesで実行する。
        gear_inches = self.ratio() * self.wheel_object.diamater
        return gear_inches

class Wheel():
    def __init__(self, rim, tire):
        self.rim = rim
        self.tire = tire
    
    @property
    def diamater(self):
        diamater = self.rim + (self.tire * 2)
        return diamater

# end of line break