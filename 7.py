class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Employee(Person):
    def __init__(self, name, age,eid):
        super().__init__(name, age)
        self.eid=eid
        
class Manager(Employee):
    def __init__(self, name, age, eid,dept):
        super().__init__(name, age, eid)
        self.dept=dept
    def display(self):
        print(self.name,self.age,self.eid,self.dept)
    def approve_leave(self,ename):
        print(f"{self.name} has approved {ename}'s leave")
    
m=Manager('jj',33,2222,'HR')
m.display()
m.approve_leave('harry')
    
