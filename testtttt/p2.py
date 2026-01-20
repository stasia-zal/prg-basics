def f(d):
    a=0
    for item in d:
        if item=='+':
            a+=1
        elif item=='-':
            a-=1
    return a



if __name__=='__main__':
    print(f(''))
    print(f('+-+'))
    print(f('+-+++-+---'))
    print(f('+-+++++-'))