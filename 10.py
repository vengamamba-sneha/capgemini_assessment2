class Electronics:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def display(self):
        print(self.brand,self.price)
class MobilePhone(Electronics):
    def __init__(self,brand,price,battery):
        super().__init__(brand,price)
        self.battery=battery
    def display(self):
        print(self.battery)
class SmartPhone(MobilePhone):
    def __init__(self, brand, price, battery,cam):
        super().__init__(brand, price, battery)
        self.cam=cam
    def display(self):
        print(self.brand,self.price,self.battery,self.cam)
    
s=SmartPhone('iphone',88888,90,64)
s.display()
        
