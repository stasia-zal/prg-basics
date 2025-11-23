def f(amount_to_pay):
    coins=0
    while amount_to_pay>0:
        a=[5,2,1]
        for i in a:
            while amount_to_pay>=i:
                amount_to_pay-=i
                coins+=1
    return coins

if __name__=="__main__":
    print(f(23))
    print(f(8))