def f(fnc,prods):
    li=list(map(fnc,prods))
    res='' 
    for item in li:
        res+=item+','
    return res[0:len(res)-1]


prods = ["water", "cheese", "tomato"]

fnc1 = lambda x: "id:" + x[:2]
print(f(fnc1, prods))

fnc2 = lambda x: (x[0] + x[-1]).upper()
print(f(fnc2, prods))