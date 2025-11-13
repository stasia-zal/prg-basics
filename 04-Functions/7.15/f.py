def f(detector):
    sum=0
    a=False
    for i in detector:
        if i=='+':
            sum+=1
        elif i=='-':
            sum-=1
        if sum>=3:
            a=True
    return a


