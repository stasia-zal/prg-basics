import re

def f(vname):
    pattern=r'^[A-z_]\w{0,4}$'
    return bool(re.fullmatch(pattern,vname))


print(f("abc"))     # True
print(f("Abc"))     # True
print(f("aBC"))     # True
print(f("_ab_c"))   # True
print(f("abcdef")) # False
print(f("8abc"))    # False
print(f("_aB8_"))   # True
print(f("_4x"))     # True