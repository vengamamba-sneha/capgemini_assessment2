#from abc import ABC,abstractmethod
class Shape:
    #@abstractmethod
    def area(self):
        pass
class Square(Shape):
    def __init__(self,s):
        self.s=s    
    def area(self):    
        print(f'area: {self.s*self.s}')
class Triangle(Shape):
    def __init__(self,b,h):
        self.b=b
        self.h=h    
    def area(self):  
        print(f'area: {0.5*self.b*self.h}')
def fun(onj):
    onj.area()
a=Square(4)
fun(a)
b=Triangle(3,4)
fun(b)


    
