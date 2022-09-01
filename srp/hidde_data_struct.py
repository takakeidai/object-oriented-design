




# srp 2
# hidde_data_struct.py

# 悪い例
# データ構造に依存した実装をしているとデータ構造が変わったり形式が変化したときに変更がしづらくなる。
class Gear_Bad():
    
    def __init__(self, data):
        self.data = data
    
    
    # 特定のデータ構造(リスト)などに頼った実装をしない。
    # リストの添字が変わったりした途端にコードが動かなくなる。
    # データ構造は別のメソッドなどを用意して隠蔽する。    
    def diameters(self):
        diameters = []
        for i in range(len(self.data)):
            diameter = self.data[i][0] + (self.data[i][1] * 2)
            diameters.append(diameter)
            
        return diameters
    

# 良い例

# このようにデータ構造を扱うオブジェクトと、そのデータ自体を扱うオブジェクトをはっきり分けることで、
# のちにデータ構造が変化しても片方のオブジェクトを直せば全て綺麗に修正できる。
class Data():
    def __init__(self, data):
        self.data = data
    
    # この@propertyがないと、data.rimやdata.tireとすることによるインスタンス変数のアクセスができない。
    # つまり、@propertyはメソッドをあたかもプロパティのように扱うためのデコレーター
    @property
    def rim(self):
        rims = []
        for i in range(len(self.data)):
            rims.append(self.data[i][0])
        return rims
    
    @property
    def tire(self):
        tires = []
        for i in range(len(self.data)):
            tires.append(self.data[i][1])
        return tires     
        

class Gear():
    def __init__(self, data):
        self.data = data
            
    def diameters(self):
        diamaters = []
        data_obj = Data(self.data)
        for i in range(len(data_obj.rim)):
            diamater = data_obj.rim[i] + (data_obj.tire[i] * 2)
            diamaters.append(diamater)   
        return diamaters


if __name__ == '__main__':
    
    data = [[622, 20], [622, 23], [559, 30], [559, 40]]
    
    Obs = Gear_Bad(data)
    print(Obs.diameters())
    
    Revl = Gear(data)
    print(Revl.diameters())

# end of line break

