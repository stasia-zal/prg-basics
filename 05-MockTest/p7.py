def f(n):
    fir=0
    sec=1
    sum=0
    if n==1:
        return 0
    if n==2 or n==3:
        return 1
    for i in range(1,n-1):
        sum=fir+sec
        fir=sec
        sec=sum
    return sum

if __name__=="__main__":
    print(f(5))
    print(f(9))







