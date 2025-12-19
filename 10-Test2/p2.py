''' 
c=a+b
a=b
b=c   '''

def f(number):
    a=0
    b=1
    c=0
    seq=[]
    for i in range(number+20):
        c=a+b
        a=b
        b=c
        seq.append(c)
    if number in seq:
        return True
    else:
        return False

if __name__=='__main__':
    print(f(5))
    print(f(4))