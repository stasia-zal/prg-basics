def f(cart,price_l,wallet):
    sum=0
    for bought in cart:
        for item in price_l:
            if bought==item:
                sum+=cart[bought]*price_l[item]
    if wallet>=sum:
        return True
    else: return False

if __name__=='__main__':
    print(f({'j':3,'b':1,'m':2},{'m':1.49,'j':1.19,'b':1.99,'h':1000},10))
    print(f({'j':3,'b':1,'m':2},{'m':1.49,'j':1.19,'b':1.99,'h':1000},8))
