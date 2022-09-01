




# duck_typing 3
# DuckTyping.py

class Trip():
    def __init__(self, bicycles, customer, vehicle):
        self.bicycles = bicycles
        self.customer = customer
        self.vehicle = vehicle
    
    # ダックタイピング
    def prepare(self, preparer):
        preparer.prepare_trip()
        
                
# すべての準備者はpreparerは、prepare_tripに応答するダックである。
# このprepare_tripメソッドのインターフェイスの統一は、
# 変更に強く、追加のpreparerクラスを必要としても簡単に追加できる。
class Mechanic():
    
    def prepare_trip(self, trip):
        self.prepare_bicycle(trip.bicycles)
        # bicycles and self.prepare_bicycle are used inside.
        pass
    
    def prepare_bicycle(self, bicycles):
        pass
    
    
class TripCoordinator():
    def buy_food(self, customer):
        pass
    
    def prepare_trip(self, trip):
        self.buy_food(trip.customer)
        pass
    
class Driver():
    def prepare_trip(self, trip):
        vehicle = trip.vehicle
        self.gas_up(vehicle)
        self.fill_water_tank(vehicle)
        pass
    
    def gas_up(self, vehicle):
        pass
    
    def fill_water_tank(self, vehicle):
        pass
        
# end of line break