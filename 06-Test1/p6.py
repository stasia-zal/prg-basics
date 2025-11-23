def f(student1,student2):
    st1=0
    st2=0
    for i in student1:
        if i==',':
            continue
        if int(i)>2:
            st1+=1
    for i in student2:
        if i==',':
            continue
        if int(i)>2:
            st2+=1
    if st1>st2:
        return 1
    elif st1<st2:
        return 2
    elif st1==st2:
        return 0


if __name__=="__main__":
    print( f('3,4,5','4,3') )
    print( f('3,2,5','5,5,2,5') )
    print( f('3,2,5,2,2','4,4') )