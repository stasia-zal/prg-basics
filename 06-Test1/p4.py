def f(n):
    res=''
    for i in range(n):
        res+='*'
        if i>=0 and i<(n-1):
            res+='/'
    return res




if __name__=="__main__":
    print( f(4) )
    print( f(1) )
    print( f(0) )