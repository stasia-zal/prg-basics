def f(expression):
    res=int(expression[0])
    for i in range(len(expression)):
        if expression[i]=='+':
            res+=int(expression[i+1])
        elif expression[i]=='-':
            res-=int(expression[i+1])
    return res

print(f("2+3"))
print(f("3+8+1"))
print(f("2+3-4+5-0"))