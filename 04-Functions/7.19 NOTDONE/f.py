def f(number):
    sum=0
    for i in str(number):
        x=0
        for a in str(number):
            if i==a:
                x+=1
            if i==a and x>1:
                sum+=int(a)
    return sum
