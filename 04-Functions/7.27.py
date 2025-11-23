def f(product_code):
    res=0
    if len(product_code)!=4:
        return False
    for a in product_code[:-1]:
        res+=int(a)
    fin=res%7
    if fin==int(product_code[-1]):
        return True
    else: return False

print(f("1082"))
print(f("2035"))
print(f("1114"))
print(f("7071"))

