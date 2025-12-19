def f(arr):
    minn=min(arr)
    i=0
    maxx=max(arr)
    a=0
    for item in arr:
        if item==minn:
            i+=1
        if item==maxx:
            a+=1
        if i>1:
            return maxx
        if a>1:
            return minn

if __name__ == '__main__':
    print( f([7,7,7,7,7,5,7,7]) ) 
    print( f([7,5,7,7,7,7,7,7]) ) 