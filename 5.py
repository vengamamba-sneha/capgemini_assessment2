class Product:
    products={}
    def __init__(self,name,price,stock):
        
        self.name=name
        self.price=price
        self.stock=stock
        self.products[self.name]={'price':self.price,'stock':self.stock}
    def check_availability(self,quantity):
        if(quantity<=self.stock):
            print('available')
        else:
            print('not available')

c=Product('ss',999,6)
c.check_availability(4)