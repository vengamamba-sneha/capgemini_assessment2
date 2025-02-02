from abc import ABC,abstractmethod
class IVehicle:
    @abstractmethod
    def start_engine(self):
        pass
    @abstractmethod
    def stop_engine(self):
        pass
class Car(IVehicle):
    def start_engine(self):
        print("Car engine started")
    def stop_engine(self):
        print("Car engine stopped")
class Bike(IVehicle):
    def start_engine(self):
        print("Bike engine started")
    def stop_engine(self):
        print("Bike engine stopped")
class Truck(IVehicle):
    def start_engine(self):
        print("Truck engine started")
    def stop_engine(self):
        print("Truck engine stopped")
car = Car()
car.start_engine()
car.stop_engine()
bike = Bike()
bike.start_engine()
bike.stop_engine()
truck = Truck()
truck.start_engine()
truck.stop_engine()