import re
def f(mnumbers):
    pattern=r'^[+-]?[a-dA-D1-7]+$'
    count=0
    for num in mnumbers:
        if re.match(pattern,num):
            count+=1
    return count


print(f(["A15", "-31", "7abC", "+D1", "-g4"]))
print(f(["A05", "-3+1", "7ab8C", "+Bb7", "-22c55"]))
print(f(["+a", "-D7", "1234567", "abcd", "ABCD"]))
print(f(["", "+", "-", "0", "8", "a0", "a8", "a+1", "1-2"]))