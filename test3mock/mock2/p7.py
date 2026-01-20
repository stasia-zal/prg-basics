def f(d):
    lis=set()
    for name, what in d:
        if what=='in':
            lis.add(name)
        elif what=='out' and name in lis:
            lis.remove(name)
    return sorted(lis)




cars = [["KR234","in"],["BA123","in"],["GX444","in"],["KR234","out"],
["BA111","in"],["BA123","out"],["KR234","in"]]
print(f(cars))  # → ["BA111","GX444","KR234"]
cars1 = [["KR234","in"],["KR234","out"]]
print(f(cars1))  # → []