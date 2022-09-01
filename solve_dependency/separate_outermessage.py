




# solve_dependency 2
# separate_outermessage.py

# 外部メッセージのカプセル化　
# 外部へのメッセージは専用のメソッドを用意してカプセル化してしまう。
# こうすることで、DRYなコードに近づけることも可能。

class Wheel():
    def __init__(self, rim, tire):
        self.rim = rim
        self.tire = tire
    
    @property
    def diamater(self):
        diamater = self.rim + (self.tire *2)
        return diamater


class Gear_Bad():
    def __init__(self, chainring, cog, wheel):
        self.chainring = chainring
        self.cog = cog
        self.wheel = wheel
    
    @property
    def ratio(self):
        ratio = self.chainring / self.cog
        return ratio
     
    def gear_inches(self):
        #ここでdiamaterは外で定義されているWheelクラスを参照している(外へメッセージを送っている)。
        inche = self.ratio * self.wheel.diamater
        return inche


class Gear():
    def __init__(self, chainring, cog, wheel):
        self.chainring = chainring
        self.cog = cog
        self.wheel = wheel
    
    @property
    def ratio(self):
        ratio = self.chainring / self.cog
        return ratio
     
    def gear_inches(self):
        # そうすればこのdiamaterメソッドは自分へのメッセージになる。
        inche = self.ratio * self.diamater()
        return inche

    # このように外部へのメッセージを新しいメソッドとしてカプセル化する。
    # そうすることで、メソッドが1箇所にまとまりDRYなコードにもなるし、外部メッセージが自分自身へのメッセージになる。
    def diamater(self):
        return self.wheel.diamater
    
    
if __name__ == '__main__':
    
    gear = Gear(52, 11, Wheel(26, 1.5))
    print(gear.gear_inches())

# end of line break