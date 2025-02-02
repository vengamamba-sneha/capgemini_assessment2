class Employee:
    def __init__(self,name,id,department):
        self.name=name
        self.id=id
        self.department=department
    def display(self):
        print(f'name: {self.name} id: {self.id} department: {self.department}')
name=input('enter the name: ')
id=input('enter the id: ')
department=input('enter the department: ')
e=Employee(name,id,department)
e.display()