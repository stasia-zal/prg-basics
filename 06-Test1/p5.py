def f(a,b):
    res=0
    for i in range(a,b+1):
        if len(str(i))==2:
            res+=i
    return res


if __name__=="__main__":
    print( f(8,12) )
    print( f(98,105) )