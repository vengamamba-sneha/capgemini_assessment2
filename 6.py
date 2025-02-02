#Implement a multi-level inheritance example where `Vehicle` is a base class, `Car` and `Bike` inherit from `Vehicle`, and `ElectricCar` inherits from `Car`.
class Vehicle:
    def __init__(self,name,model):
        self.name=name
        self.model=model
    def details(self):
        print(self.name,self.model)

class Car(Vehicle):
    def __init__(self, name, model,price,year):
        super().__init__(name, model)
        self.price=price
        self.year=year
    def details(self):
        print(self.name,self.model,self.price,self.year)
class Bike(Vehicle):
    def __init__(self, name, model,price,year,numberplate):
        super().__init__(name, model)
        self.price=price
        self.year=year
        self.numberplate=numberplate
    def details(self):
        print(self.name,self.model,self.price,self.year,self.numberplate)
class Electriccar(Car):
    def __init__(self, name, model, price, year,charge):
        super().__init__(name, model, price, year)
        self.charge=charge
    def details(self):
         print(self.name,self.model,self.price,self.year,self.charge)
        
c=Car('maruthi suzuki','swift',8888888,3333)
c.details()
b=Bike('honda','splender',3333,3333,3388)
b.details()
e=Electriccar('dd','dd',2222,3333333,33)
e.details()

    
    

