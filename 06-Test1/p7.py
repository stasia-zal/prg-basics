def f(a,b):
    sum=0
    pre=1
    cur=1
    for j in range(1,b):
        if j==1:
            pre=1
        cur+=pre
        pre=cur
    return cur
        


if __name__=="__main__":
    print( f(0,5))
    print( f(1,5) )
    print( f(6,21) )




'''



def f(a,b):
    sum=0
    pre=0
    cur=1
    for i in range(a,b+1):
        if i==1:
            cur=0
        elif i==2:
            cur=1
        else:
            cur=a
            sum+=cur
        pre=cur
    return sum
        
    

    '''