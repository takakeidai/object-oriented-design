




# inheritance 2
# mix_different_classes.py


# 問題ありなコード
# ロードバイクとマウンテンバイクの２種類の自転車に対応できるようにBicycleクラスを変更した。
# プロパティを追加し、if文でロードバイクの場合とマウンテンバイクの場合に対応させた。
# こうすると将来の変更が難しくなる。
# 継承を使ってクラスを整理していく。


class Bicycle():
    def __init__(self, **kwargs):
        self.style = kwargs["style"] if "style" in kwargs.keys() else None
        self.size = kwargs["size"] if "size" in kwargs.keys() else None
        self.tape_color = kwargs["tape_color"] if "tape_color" in kwargs.keys() else None
        self.front_shock = kwargs["front_shock"] if "front_shock" in kwargs.keys() else None
        self.rear_shock = kwargs["rear_shock"] if "rear_shock" in kwargs.keys() else None
    
    @property
    def spares(self):
        if self.style == "road":
            spares_detail = {
                "chain": "10-speed",
                "tire_size":23,
                "tape_color":self.tape_color
            }
        else:
            spares_detail = {
                "chain": "10-speed",
                "tire_size":2.1,
                "tape_color":self.rear_shock
            }            
        return spares_detail
    

if __name__ == '__main__':
    bike = Bicycle(
        style = "mountain",
        size = "S", 
        front_shock = "Manitou",
        rear_shock = "Fox"
        )
    
    print(bike.size)
    print(bike.spares)
    
# end of line break