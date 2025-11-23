def f(password):
    a=True
    if len(password)<6:
        return False
    for i in password:
        count=0
        for j in password:
            if i==j:
                if count>=1:
                    a= False
                count+=1
    return a

if __name__=="__main__":
    print( f('ax15') )
    print( f('book123') )
    print( f('A2water3') )
    print( f('qwerty') )
    print( f('') )