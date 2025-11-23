def f(password):
    if len(password)<6:
        a=False
    else:
        letters=[]
        a=True
        count=0
        for i in password:
            if i in letters:
                count+=1
                if count>=1:
                    a=False
            letters.append(i)
    return a


print(f("ax15"))
print(f("book123"))
print(f("A2water3"))
print(f("qwerty"))
print(f(""))                
