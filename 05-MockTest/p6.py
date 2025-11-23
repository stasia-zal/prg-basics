def f(number,even):
    res=0
    if even==True:
        for i in str(number):
            if int(i)%2==0:
                res+=int(i)
    if even==False:
        for i in str(number):
            if int(i)%2!=0:
                res+=int(i)  
    return res  

if __name__=="__main__":
    print(f(3124,True))
    print(f(3124,False))
    print(f(20576,False))
    print(f(20576,True))
    print(f(131313,True))

