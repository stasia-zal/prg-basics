def f(fnc,res):
    li=list(filter(fnc,res))
    return max(li)-min(li)






res = [95, 90, 20, 50, 70]

fnc1 = lambda x: x > 50
print(f(fnc1, res))# [95,90,70] => 95-70

fnc2 = lambda x: x > 30 and x < 90
print(f(fnc2, res))  # [50,70] => 70-50

# jeszcze jedno: filtr łapie większy zbiór
fnc3 = lambda x: x >= 20
print(f(fnc3, res)) # max=95 min=20