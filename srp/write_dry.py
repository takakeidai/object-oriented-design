




# srp 3
# write_dry.py

# DRYなコードを書く。

# 悪い例
class Gear_Bad():
    
    # Don't Repeat Yourselfなコードを書こう。
    # インスタンス変数は、1箇所にまとめて変更可能にする
    def ratio(self, chainring, cog):
        return chainring / cog
    
    def gear_inches(self, chainring, cog, rim, tire):
        ratio = self.ratio(chainring, cog)
        gear_inche = ratio * (rim + (tire * 2))
        return gear_inche


# 良い例
# chainring, cog, rim, tireの値が変化しても、変更が容易
class Gear():
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

# end of line break