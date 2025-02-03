from abc import ABC,abstractmethod
class IDatabaseoperations(ABC):
    def __init__(self):
        self.datalist=[]
    @abstractmethod
    def insert(self,data):
        pass
    @abstractmethod
    def update(self,data):
        pass
    @abstractmethod
    def delete(self,data):
        pass
class SQLDatabase(IDatabaseoperations):
    def __init__(self):
        super().__init__()
    def insert(self,data):
        self.datalist.append(data)
        print(f'inserting data {data}')
        print(self.datalist)
    def update(self,data):
        self.datalist.append(data)
        print(f'updating data {data}')
        print(self.datalist)
    def delete(self,data):
        
        if data in self.datalist:
            self.datalist.remove(data)
            print(f'deleting data {data}')
            
        else:
            print('not found')
        print(self.datalist)

class NoSQLDatabase(IDatabaseoperations):

    def __init__(self):
        super().__init__()
    def insert(self,data):
        self.datalist.append(data)
        print(f'inserting data {data}')
        print(self.datalist)
    def update(self,data):
        self.datalist.append(data)
        print(f'updating data {data}')
        print(self.datalist)
    def delete(self,data):
        
        if data in self.datalist:
            self.datalist.remove(data)
            print(f'deleting data {data}')
            
        else:
            print('not found')
        print(self.datalist)

s=SQLDatabase()
s.insert('ex1')
s.update('ex2')
s.delete('ex1')

n=NoSQLDatabase()
n.insert('ex1')
n.update('ex2')
n.delete('ex1')
