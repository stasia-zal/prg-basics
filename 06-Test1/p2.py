def f(thing_to_wash, extra_rinse,extra_spin):
    result=0
    if thing_to_wash=='j' or thing_to_wash=='J':
        result+=40
    elif thing_to_wash=='u' or thing_to_wash=='U':
        result+=70
    elif thing_to_wash=='s' or thing_to_wash=='S':
        result+=20
    if extra_rinse==True:
        result+=15
    if extra_spin==True:
        result+=9
    return result



if __name__=="__main__":
    print( f('U',False,True) )
    print( f('J',True,True) )
    print( f('S',False,False) )