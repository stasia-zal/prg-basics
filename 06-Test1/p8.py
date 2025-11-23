def f(hours,minutes,seconds):
    h=hours*60*60
    m=minutes*60
    if h==m and m==seconds:
        return True
    else: 
        return False


if __name__=="__main__":
    print( f(1,60,3600) )
    print( f(2,120,7200) )
    print( f(4,220,14400) )
    print( f(3,180,10600) )
    