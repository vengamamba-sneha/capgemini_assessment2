class Car:
    def move(self):    
        print('road')
class defAirplane:
    def move(self):
        print('air')
class FlyingCar(Car,defAirplane):
    def move(self):
        print('road,air')

        
f=FlyingCar()
f.move()


