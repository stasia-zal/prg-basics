def f(name):
    res=name[0]
    for i in range(len(name)):
        if name[i]==' ':
            res+=name[i+1]
    return res

print(f("Internet of Things"))
print(f("For Your Information"))
print(f("Python"))