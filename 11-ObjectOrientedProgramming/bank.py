class Bank:
    def __init__(self,number):
        self.number=number
        self.balance=0.0
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
    def withdraw(self,amount):
        if amount>0 and self.balance>amount:
            self.balance-=amount
        else:
            print('ERROR NOT ENOUGH MONEY')
    def display(self):
        print()
        print(f'Bank Account No: {self.number}')
        print(f'Balance: PLN {self.balance}')
        print()