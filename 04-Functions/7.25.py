def f(x,y):
    sum=0
    for i in range(x,y+1):
        if i%6==0 and not i%4==0:
            sum+=i
    return sum

print(f(1,20))
print(f(10,30))