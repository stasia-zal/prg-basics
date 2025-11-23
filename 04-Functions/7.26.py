def f(text):
    res=''
    for i in range(len(text)):
        res+=text[i]
        if i<len(text)-1:
            res+='-'
    return res

print(f("Univesity"))
print(f("UE"))
print(f("x"))
print(f(""))