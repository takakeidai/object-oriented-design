




# inheritance 1
# Bicycle_class.py

class Bicycle():
    def __init__(self, **kwargs):
        self.size = kwargs["size"]
        self.tape_color = kwargs["tape_color"]
    
    @property
    def spares(self):
        spares_detail = {
            "chain": "10-speed",
            "tire_size":23,
            "tape_color":self.tape_color
        }
        return spares_detail
    

if __name__ == '__main__':
    bike = Bicycle(size = "M", tape_color = "red")
    print(bike.size)
    print(bike.spares)

# end of line break