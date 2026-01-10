def f(value1):
    return lambda value2:value1*value2



times_five = f(5)
print(times_five(8))
times_three = f(3)
print(times_three(7))
print(f(0)(999))
print(f(-2)(11))