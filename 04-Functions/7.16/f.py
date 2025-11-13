def f(n):
    a=0
    r=1
    for i in range(n-2):
        r+=a
        a=r-a
    return r
    




