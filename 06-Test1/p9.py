def f(sizes):
    s=0
    m=0
    l=0
    for i in sizes:
        if i=='S':
            s+=1
        elif i=='M':
            m+=1
        elif i=='L':
            l+=1
    if s<=m and s<=l:
        return 'S'
    if m<=s and m<=l:
        return 'M'
    if l<=s and l<=m:
        return 'L'


if __name__=="__main__":
    print( f('L,S,L,M,L,S,S,L') )
    print( f('M,L,L,L,M') )
    print( f('M,L,M,L,S,S,S') )