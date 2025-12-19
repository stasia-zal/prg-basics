

def f(comp,smart):
    comp=set(comp)
    smart=set(smart)
    everyone=comp|smart
    return len(everyone)



if __name__=='__main__':
    print(f({'j','p',},{'p','f','a'}))
    print(f({'Breeze','Hunter','Walker','Chaser','Campet','Owl'},{'Breeze','Owl','Storm','Walker'}))