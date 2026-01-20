def f(fnc,prods):
    res=(list(map(fnc,prods)))
    print( ','.join(res))


prods = ["water","cheese","tomato"]
fnc1 = lambda x: "id:"+x[:2]
f(fnc1,prods)
fnc2 = lambda x: (x[0]+x[-1]).upper()
f(fnc2,prods) 