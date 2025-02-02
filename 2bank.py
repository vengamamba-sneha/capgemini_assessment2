class BankAccount:
    def __init__(self):
        self.money= 555
    def balance(self):     
        return self.money
        
    def deposit(self,dmoney): 
        self.money+=dmoney
        return self.money
    
    def withdraw(self,wmoney):
        if wmoney>self.money:
            print('insufficient balance')
            return self.money
        self.money-=wmoney
        return self.money

def main():
    b=BankAccount()
    while True:
        print('1. deposit 2. withdraw 3.balance 4.break')
        option=int(input('enter your option'))
        if option==1:
            print('enter amount to deposit')
            dmoney=int(input())
            new_bal=b.deposit(dmoney)
            print(new_bal)
        elif option==2:
            print('enter amount to withdraw')
            wmoney=int(input())
            new_bal=b.withdraw(wmoney)
            print(new_bal)
        elif option==3:           
            print(b.balance())
        elif option==4:
            break
        else:
            print('enter correct option')
main()

           





