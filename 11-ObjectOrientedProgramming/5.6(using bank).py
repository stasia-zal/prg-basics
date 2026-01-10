from bank import Bank 
def main():
    bank=Bank('12 3456 5555 9090 1111 0000 7722')
    bank.display()
    bank.deposit(25.30)
    bank.display()
    bank.withdraw(31.70)
    bank.display()
    bank.withdraw(14)
    bank.display()

if __name__=='__main__':
    main()