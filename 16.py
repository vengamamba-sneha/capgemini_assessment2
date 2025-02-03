from abc import ABC,abstractmethod
class IShape(ABC):
    @abstractmethod
    def calculatee_area(self):
        pass
class Rectangle(IShape):
    def calculatee_area(self,l,b):
        self.l=l
        self.b=b
        print(l*b)
class Circle(IShape):
    def calculatee_area(self,r):
        self.r=r
        print(3.14*r*r)
r=Rectangle()
r.calculatee_area(3,4)
c=Circle()
c.calculatee_area(3)
        
    
        
