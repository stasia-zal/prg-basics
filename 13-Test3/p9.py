def f(uid):
    s=set(uid)
    if len(uid)!=len(s):
        return False
    else: return True


print(f(["john5", "ann123", "JOHN5", "xxx", "abc333", "a10"]))
print(f(["abc123", "ann", "abc123", "a10"]))
print(f([]))
print(f(["a"]))
print(f(["A", "A"]))
